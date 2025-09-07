from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from Options import OptionError
from Utils import visualize_regions
from ..options import DeathsDoorPlandoConnections, EntranceRandomization
from .scene_transitions import two_way_scene_transitions, one_way_scene_transitions
from entrance_rando import (
    ERPlacementState,
    EntranceRandomizationError,
    EntranceType,
    randomize_entrances,
    disconnect_entrance_for_randomization,
)
from .entrance_class import DeathsDoorEntrance, DeathsDoorConnectionGroup
from ..regions import DeathsDoorRegionName as R
from ..jefferson import create_jefferson_vanilla_connections, jefferson_tag

if TYPE_CHECKING:
    from .. import DeathsDoorWorld


def create_vanilla_entrances(world: "DeathsDoorWorld"):
    # Create vanilla entrances
    all_scene_transitions = two_way_scene_transitions + one_way_scene_transitions
    for scene_transition_pair in all_scene_transitions:
        entrance_type = (
            EntranceType.ONE_WAY
            if scene_transition_pair[1] == None
            else EntranceType.TWO_WAY
        )
        entrance_group = (
            DeathsDoorConnectionGroup.ONE_WAY
            if scene_transition_pair[1] == None
            else DeathsDoorConnectionGroup.STANDARD
        )
        for scene_transition in scene_transition_pair:
            if scene_transition is not None:
                start_region = world.multiworld.get_region(
                    scene_transition.starting_region.value, world.player
                )
                end_region = world.multiworld.get_region(
                    scene_transition.ending_region.value, world.player
                )
                new_entrance = world.create_entrance(
                    start_region, end_region, scene_transition.rule
                )
                new_entrance.randomization_type = entrance_type
                new_entrance.randomization_group = entrance_group

    create_jefferson_vanilla_connections(world)


def connect_plando(
    world: "DeathsDoorWorld",
    plando_connections: DeathsDoorPlandoConnections,
    coupled: bool,
) -> None:
    for plando_connection in plando_connections:
        if plando_connection.direction == "exit":
            ## Switch connections to be in entrance direction
            temp_exit = plando_connection.exit
            plando_connection.exit = plando_connection.entrance
            plando_connection.entrance = temp_exit
        entrance, two_way_entrance = find_scene_transition_from_name(
            plando_connection.entrance
        )
        exit, two_way_exit = find_scene_transition_from_name(plando_connection.exit)
        if two_way_exit != two_way_entrance:
            raise OptionError(
                f"One-ways (Avarices) cannot be plando'd to two-ways. Plando connection {plando_connection.entrance} to {plando_connection.exit} is invalid."
            )
        if plando_connection.direction != "both" and coupled and two_way_entrance:
            raise Warning(
                f"If entrance randomization is set to coupled, all two-way plando_connections will be forced to be both. Plando connection {plando_connection.entrance} to {plando_connection.exit} has direction {plando_connection.direction}"
            )

        from_region = world.multiworld.get_region(
            entrance.starting_region.value, world.player
        )
        to_region = world.multiworld.get_region(exit.ending_region.value, world.player)
        remove_dangling_exit(from_region)
        remove_dangling_entrance(to_region)
        from_to_to = from_region.connect(to_region)
        world.entrance_pairings[entrance.name] = exit.name
        if entrance.rule is not None:
            resolved_rule = world.resolve_rule(entrance.rule)
            world.register_rule_dependencies(resolved_rule)
            if resolved_rule:
                from_to_to.access_rule = resolved_rule
                if resolved_rule is not None:
                    world.register_rule_connections(resolved_rule, from_to_to)

        if (coupled or plando_connection.direction == "both") and two_way_entrance:
            remove_dangling_exit(to_region)
            remove_dangling_entrance(from_region)
            to_to_from = to_region.connect(from_region)
            world.entrance_pairings[entrance.name] = exit.name
            if exit.rule is not None:
                resolved_rule = world.resolve_rule(exit.rule)
                world.register_rule_dependencies(resolved_rule)
                if resolved_rule:
                    from_to_to.access_rule = resolved_rule
                    if resolved_rule is not None:
                        world.register_rule_connections(resolved_rule, to_to_from)


def find_scene_transition_from_name(name: str) -> tuple[DeathsDoorEntrance, bool]:
    try:
        scene_transition_pair = next(
            pair
            for pair in two_way_scene_transitions
            if pair[0].name == name or pair[1].name == name
        )
        if scene_transition_pair[0].name == name:
            return [scene_transition_pair[0], scene_transition_pair[1] != None]
        elif scene_transition_pair[1].name == name:
            return [scene_transition_pair[1], True]
    except StopIteration:
        try:
            scene_transition_pair = next(
                pair for pair in one_way_scene_transitions if pair[0].name == name
            )
            if scene_transition_pair[0].name == name:
                return [scene_transition_pair[0], False]
        except StopIteration:
            raise OptionError(
                f"Provided name of entrance or exit {name} in plando_connections is not valid."
            )
    raise OptionError(
        f"Provided name of entrance or exit {name} in plando_connections is not valid."
    )


def find_two_way_transition_name(region_name: str, from_region: bool):
    if from_region:
        found = next(
            (
                transition_pair[0].name
                for transition_pair in two_way_scene_transitions
                if transition_pair[0].starting_region.value == region_name
            ),
            None,
        )
        if not found:
            found = next(
                (
                    transition_pair[1].name
                    for transition_pair in two_way_scene_transitions
                    if transition_pair[1].starting_region.value == region_name
                ),
                None,
            )
    else:
        found = next(
            (
                transition_pair[0].name
                for transition_pair in two_way_scene_transitions
                if transition_pair[0].ending_region.value == region_name
            ),
            None,
        )
        if not found:
            found = next(
                (
                    transition_pair[1].name
                    for transition_pair in two_way_scene_transitions
                    if transition_pair[1].ending_region.value == region_name
                ),
                None,
            )
    if not found:
        raise Warning(f"no transition for region name {region_name} found")
    return found


def find_one_way_transition_name(region_name: str, from_region: bool):
    if from_region:
        found = next(
            (
                transition_pair[0].name
                for transition_pair in one_way_scene_transitions
                if transition_pair[0].starting_region.value == region_name
            ),
            None,
        )
    else:
        found = next(
            (
                transition_pair[0].name
                for transition_pair in one_way_scene_transitions
                if transition_pair[0].ending_region.value == region_name
            ),
            None,
        )
    if not found:
        raise Warning(f"no transition for region name {region_name} found")
    return found


def randomize_one_ways(world: "DeathsDoorWorld"):
    # Randomize these separately so that GER doesn't choke

    from_exits = sorted(
        [
            ex
            for region in world.multiworld.get_regions(world.player)
            for ex in region.exits
            if not ex.connected_region
            and ex.randomization_group == DeathsDoorConnectionGroup.ONE_WAY
        ],
        key=lambda x: x.name,
    )
    world.random.shuffle(from_exits)
    to_entrances = sorted(
        [
            entrance
            for region in world.multiworld.get_regions(world.player)
            for entrance in region.entrances
            if not entrance.parent_region
            and entrance.randomization_group == DeathsDoorConnectionGroup.ONE_WAY
        ],
        key=lambda x: x.name,
    )
    world.random.shuffle(to_entrances)

    for from_exit, to_entrance in zip(from_exits, to_entrances):
        remove_dangling_exit(from_exit.parent_region)
        remove_dangling_entrance(to_entrance.connected_region)
        from_scene_transition_name = find_one_way_transition_name(
            from_exit.parent_region.name, True
        )
        to_scene_transition_name = find_one_way_transition_name(
            to_entrance.connected_region.name, False
        )
        from_scene_transition, _ = find_scene_transition_from_name(
            from_scene_transition_name
        )
        world.entrance_pairings[from_scene_transition_name] = to_scene_transition_name
        entrance = world.create_entrance(
            from_exit.parent_region,
            to_entrance.connected_region,
            from_scene_transition.rule,
        )
        entrance.randomization_group = DeathsDoorConnectionGroup.ONE_WAY
        entrance.randomization_type = EntranceType.ONE_WAY


def connect_entrances_function(world: "DeathsDoorWorld"):
    def on_connect(
        _: ERPlacementState,
        exits: list[Entrance],
        entrances: list[Entrance],
    ) -> bool:
        for exit, entrance in zip(exits, entrances):
                try:
                    start_region = world.get_region(
                        exit.parent_region.name + jefferson_tag
                    )
                except KeyError:
                    start_region = None
                try:
                    end_region = world.get_region(
                        entrance.connected_region.name + jefferson_tag
                    )
                except KeyError:
                    end_region = None
                if start_region:
                    try:
                        remove_dangling_exit(start_region)
                    except ValueError:
                        pass
                if end_region:
                    try:
                        remove_dangling_entrance(end_region)
                    except ValueError:
                        pass
                if start_region and end_region:
                    scene_transition, _ = find_scene_transition_from_name(
                        find_two_way_transition_name(exit.parent_region.name, True)
                    )
                    new_entrance = world.create_entrance(
                        start_region, end_region, scene_transition.rule
                    )
                    new_entrance.randomization_group = (
                        DeathsDoorConnectionGroup.JEFFERSON
                    )
                    new_entrance.randomization_type = EntranceType.TWO_WAY
        return True

    if world.options.entrance_randomization != EntranceRandomization.option_off:
        coupled = (
            world.options.entrance_randomization == EntranceRandomization.option_coupled
        )

        # Create all the dangling ends
        for scene_transition_pair in two_way_scene_transitions:
            for scene_transition in scene_transition_pair:
                for _exit in world.get_region(
                    scene_transition.starting_region
                ).get_exits():
                    if _exit.randomization_group == DeathsDoorConnectionGroup.STANDARD:
                        entrance: Entrance = _exit
                        disconnect_entrance_for_randomization(
                            entrance, entrance.randomization_group
                        )
                if scene_transition is not None and not scene_transition.no_jefferson:
                    start_region = world.multiworld.get_region(
                        scene_transition.starting_region.value + jefferson_tag,
                        world.player,
                    )
                    for _exit in start_region.get_exits():
                        if (
                            _exit.randomization_group
                            == DeathsDoorConnectionGroup.JEFFERSON
                        ):
                            entrance: Entrance = _exit
                            disconnect_entrance_for_randomization(
                                entrance, entrance.randomization_group
                            )

        for scene_transition_pair in one_way_scene_transitions:
            for _exit in world.get_region(
                scene_transition_pair[0].starting_region
            ).get_exits():
                if _exit.randomization_group == DeathsDoorConnectionGroup.ONE_WAY:
                    entrance: Entrance = _exit
                    disconnect_entrance_for_randomization(
                        entrance,
                        entrance.randomization_group,
                        scene_transition_pair[0].name,
                    )

        # Plando
        if world.options.plando_connections:
            connect_plando(world, world.options.plando_connections, coupled)

        # Randomize specifically the one-ways
        randomize_one_ways(world)

        retry_count = 0
        RETRY_MAX = 10
        successful_ER = False
        while retry_count < RETRY_MAX and not successful_ER:
            try:
                final_result = randomize_entrances(
                    world,
                    coupled,
                    {
                        DeathsDoorConnectionGroup.STANDARD: [
                            DeathsDoorConnectionGroup.STANDARD
                        ]
                    },
                    er_targets=sorted(
                        [
                            entrance
                            for region in world.multiworld.get_regions(world.player)
                            for entrance in region.entrances
                            if not entrance.parent_region
                            and entrance.randomization_group
                            == DeathsDoorConnectionGroup.STANDARD
                        ],
                        key=lambda x: x.name,
                    ),
                    exits=sorted(
                        [
                            ex
                            for region in world.multiworld.get_regions(world.player)
                            for ex in region.exits
                            if not ex.connected_region
                            and ex.randomization_group
                            == DeathsDoorConnectionGroup.STANDARD
                        ],
                        key=lambda x: x.name,
                    ),
                    on_connect=on_connect,
                )
                jefferson_region = world.get_region(R.FLOODED_FORTRESS_ENTRANCE_JEFFERSON.value)
                if (
                    not jefferson_region
                    in world.multiworld.get_all_state().reachable_regions[world.player]
                ):
                    raise EntranceRandomizationError(
                        f"Requested reachable region {jefferson_region.name} is not reachable in current state."
                    )
                
                successful_ER = True
                # print(retry_count)
            except EntranceRandomizationError as error:
                retry_count += 1
                if retry_count >= RETRY_MAX:
                    # start_region = world.get_region(world.origin_region_name)
                    # visualize_regions(
                    #     start_region,
                    #     "DD_visualization.puml",
                    #     regions_to_highlight=CollectionState(
                    #         world.multiworld
                    #     ).reachable_regions[world.player],
                    # )
                    raise EntranceRandomizationError(
                        f"Death's Door: failed GER after {RETRY_MAX} attempts. Final error: {error}"
                    )
                # Undo placements
                for region in world.get_regions():
                    for _exit in region.get_exits():
                        _exit: Entrance = _exit
                        if (
                            (
                                _exit.randomization_group
                                == DeathsDoorConnectionGroup.STANDARD
                                or _exit.randomization_group
                                == DeathsDoorConnectionGroup.JEFFERSON
                            )
                            and _exit.parent_region
                            and _exit.connected_region
                            and _exit.name not in world.entrance_pairings.keys()
                        ):
                            disconnect_entrance_for_randomization(
                                _exit, _exit.randomization_group
                            )

        for placement in final_result.placements:
            world.entrance_pairings[
                find_two_way_transition_name(placement.parent_region.name, True)
            ] = find_two_way_transition_name(placement.connected_region.name, False)

        if coupled:
            direction = "both"
        else:
            direction = "entrance"
        for entrance, exit in world.entrance_pairings.items():
            world.multiworld.spoiler.set_entrance(
                entrance, exit, direction, world.player
            )

# remove_dangling defs Credit to alwaysintreble's Messenger code
def remove_dangling_exit(region: Region) -> None:
    # find the disconnected exit and remove references to it
    for _exit in region.exits:
        if not _exit.connected_region:
            break
    else:
        raise ValueError(f"Unable to find randomized transition for {region}")
    region.exits.remove(_exit)


def remove_dangling_entrance(region: Region) -> None:
    # find the disconnected entrance and remove references to it
    for _entrance in region.entrances:
        if not _entrance.parent_region:
            break
    else:
        raise ValueError(f"Invalid target region {region}")
    region.entrances.remove(_entrance)
