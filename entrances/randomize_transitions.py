from typing import TYPE_CHECKING

from BaseClasses import Region
from Options import OptionError
from ..options import DeathsDoorPlandoConnections, EntranceRandomization
from .scene_transitions import two_way_scene_transitions, one_way_scene_transitions
from entrance_rando import EntranceType
from .entrance_class import DeathsDoorEntrance

if TYPE_CHECKING:
    from .. import DeathsDoorWorld


def create_er_targets_and_exits(
    world: "DeathsDoorWorld",
    entrances_to_randomize: list[tuple[DeathsDoorEntrance, DeathsDoorEntrance | None]],
):
    for A_to_B, B_to_A in entrances_to_randomize:
        A_region = world.multiworld.get_region(
            A_to_B.starting_region.value, world.player
        )
        B_region = world.multiworld.get_region(A_to_B.ending_region.value, world.player)

        exit_A = A_region.create_exit(A_to_B.name)
        if A_to_B.rule is not None:
            resolved_rule = world.resolve_rule(A_to_B.rule)
            world.register_rule_dependencies(resolved_rule)
            if resolved_rule:
                exit_A.access_rule = resolved_rule
                if resolved_rule is not None:
                    world.register_rule_connections(resolved_rule, exit_A)
        if B_to_A is not None:
            er_target_A = A_region.create_er_target(A_to_B.name)
            er_target_B = B_region.create_er_target(B_to_A.name)
            exit_B = B_region.create_exit(B_to_A.name)
            if B_to_A.rule is not None:
                resolved_rule = world.resolve_rule(B_to_A.rule)
                world.register_rule_dependencies(resolved_rule)
                if resolved_rule:
                    exit_B.access_rule = resolved_rule
                    if resolved_rule is not None:
                        world.register_rule_connections(resolved_rule, exit_B)

            exit_A.randomization_type = EntranceType.TWO_WAY
            er_target_A.randomization_type = EntranceType.TWO_WAY
            er_target_B.randomization_type = EntranceType.TWO_WAY
            exit_B.randomization_type = EntranceType.TWO_WAY
        else:
            # One-way
            er_target_B = B_region.create_er_target(A_to_B.name)
            er_target_B.randomization_type = EntranceType.ONE_WAY
            exit_A.randomization_type = EntranceType.ONE_WAY
            er_target_B.randomization_group = 1
            exit_A.randomization_group = 1


def connect_plando(
    world: "DeathsDoorWorld", plando_connections: DeathsDoorPlandoConnections
) -> None:
    # Credit to alwaysintreble's Messenger code
    def remove_dangling_exit(region: Region) -> None:
        # find the disconnected exit and remove references to it
        for _exit in region.exits:
            if not _exit.connected_region:
                break
        else:
            raise ValueError(
                f"Unable to find randomized transition for {plando_connection}"
            )
        region.exits.remove(_exit)

    def remove_dangling_entrance(region: Region) -> None:
        # find the disconnected entrance and remove references to it
        for _entrance in region.entrances:
            if not _entrance.parent_region:
                break
        else:
            raise ValueError(f"Invalid target region for {plando_connection}")
        region.entrances.remove(_entrance)

    for plando_connection in plando_connections:
        if plando_connection.direction == "exit":
            ## Switch connections to be in entrance direction
            temp_exit = plando_connection.exit
            plando_connection.exit = plando_connection.entrance
            plando_connection.entrance = temp_exit
        entrance, two_way = find_scene_transition_plando(plando_connection.entrance)
        exit, _ = find_scene_transition_plando(plando_connection.exit)
        coupled = (
            world.options.entrance_randomization == EntranceRandomization.option_coupled
        )
        if plando_connection.direction != "both" and coupled and two_way:
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

        if (coupled or plando_connection.direction == "both") and two_way:
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


def find_scene_transition_plando(name: str) -> tuple[DeathsDoorEntrance, bool]:
    scene_transition_pair = next(
        pair
        for pair in two_way_scene_transitions
        if pair[0].name == name or pair[1].name == name
    )
    if scene_transition_pair[0].name == name:
        return [scene_transition_pair[0], scene_transition_pair[1] != None]
    elif scene_transition_pair[1].name == name:
        return [scene_transition_pair[1], True]
    else:
        raise OptionError(
            f"Provided name of entrance or exit {name} in plando_connections is not valid."
        )


def find_transition_name(region_name: str, entrance: bool):
    if entrance:
        found = next(
            (
                transition_pair[0].name
                for transition_pair in two_way_scene_transitions
                if transition_pair[0].starting_region.value == region_name
            ),
            "",
        )
        if not found:
            found = next(
                (
                    transition_pair[1].name
                    for transition_pair in two_way_scene_transitions
                    if transition_pair[1].starting_region.value == region_name
                ),
                "",
            )
    else:
        found = next(
            (
                transition_pair[0].name
                for transition_pair in two_way_scene_transitions
                if transition_pair[0].ending_region.value == region_name
            ),
            "",
        )
        if not found:
            found = next(
                (
                    transition_pair[1].name
                    for transition_pair in two_way_scene_transitions
                    if transition_pair[1].ending_region.value == region_name
                ),
                "",
            )
    return found


def randomize_one_ways(world: "DeathsDoorWorld", coupled: bool):
    # Randomize these separately so that GER doesn't choke
    # TODO: remove entrances/exits that have been plando'd
    # TODO: clean up the loose ends too
    entrances = one_way_scene_transitions.copy()
    world.random.shuffle(entrances)
    exits = one_way_scene_transitions.copy()
    world.random.shuffle(exits)

    for entrance, exit in zip(entrances, exits):
        connection = world.get_region(entrance[0].starting_region.value).connect(
            world.get_region(exit[0].ending_region.value)
        )
        world.entrance_pairings[entrance[0].name] = exit[0].name
        if entrance[0].rule is not None:
            resolved_rule = world.resolve_rule(entrance[0].rule)
            world.register_rule_dependencies(resolved_rule)
            if resolved_rule:
                connection.access_rule = resolved_rule
                if resolved_rule is not None:
                    world.register_rule_connections(resolved_rule, connection)
