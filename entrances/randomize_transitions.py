from collections.abc import Callable
from enum import IntEnum
import logging
import time
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from Options import Accessibility, OptionError
from ..options import DeathsDoorPlandoConnections, EntranceRandomization
from .scene_transitions import two_way_scene_transitions, one_way_scene_transitions
from entrance_rando import (
    ERPlacementState,
    EntranceLookup,
    EntranceRandomizationError,
    EntranceType,
    randomize_entrances,
)
from .entrance_class import DeathsDoorEntrance
from ..regions import DeathsDoorRegionName as R
from ..jefferson import jefferson_tag

if TYPE_CHECKING:
    from .. import DeathsDoorWorld


class DeathsDoorConnectionGroup(IntEnum):
    STANDARD = 0
    ONE_WAY = 1
    JEFFERSON = 10


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
            for e in [exit_A, exit_B, er_target_A, er_target_B]:
                e.randomization_group = DeathsDoorConnectionGroup.STANDARD
                e.randomization_type = EntranceType.TWO_WAY
        else:
            # One-way
            er_target_B = B_region.create_er_target(A_to_B.name)
            for e in [exit_A, er_target_B]:
                e.randomization_group = DeathsDoorConnectionGroup.ONE_WAY
                e.randomization_type = EntranceType.ONE_WAY

        if not A_to_B.no_jefferson:
            # Create Jefferson dangling ends
            A_region = world.multiworld.get_region(
                A_to_B.starting_region.value + jefferson_tag, world.player
            )
            B_region = world.multiworld.get_region(
                A_to_B.ending_region.value + jefferson_tag, world.player
            )

            exit_A = A_region.create_exit(A_to_B.name + jefferson_tag)
            if A_to_B.rule is not None:
                resolved_rule = world.resolve_rule(A_to_B.rule)
                world.register_rule_dependencies(resolved_rule)
                if resolved_rule:
                    exit_A.access_rule = resolved_rule
                    if resolved_rule is not None:
                        world.register_rule_connections(resolved_rule, exit_A)
            if B_to_A is not None:
                er_target_A = A_region.create_er_target(A_to_B.name + jefferson_tag)
                er_target_B = B_region.create_er_target(B_to_A.name + jefferson_tag)
                exit_B = B_region.create_exit(B_to_A.name + jefferson_tag)
                if B_to_A.rule is not None:
                    resolved_rule = world.resolve_rule(B_to_A.rule)
                    world.register_rule_dependencies(resolved_rule)
                    if resolved_rule:
                        exit_B.access_rule = resolved_rule
                        if resolved_rule is not None:
                            world.register_rule_connections(resolved_rule, exit_B)
                for e in [exit_A, exit_B, er_target_A, er_target_B]:
                    e.randomization_group = DeathsDoorConnectionGroup.JEFFERSON
                    e.randomization_type = EntranceType.TWO_WAY


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
        connection = from_exit.parent_region.connect(to_entrance.connected_region)
        remove_dangling_exit(from_exit.parent_region)
        remove_dangling_entrance(to_entrance.connected_region)
        from_scene_transition_name = find_one_way_transition_name(from_exit.parent_region.name, True)
        to_scene_transition_name = find_one_way_transition_name(to_entrance.connected_region.name, False)
        from_scene_transition, _ = find_scene_transition_from_name(
            from_scene_transition_name
        )
        world.entrance_pairings[from_scene_transition_name] = to_scene_transition_name
        if from_scene_transition.rule is not None:
            resolved_rule = world.resolve_rule(from_scene_transition.rule)
            world.register_rule_dependencies(resolved_rule)
            if resolved_rule:
                connection.access_rule = resolved_rule
                if resolved_rule is not None:
                    world.register_rule_connections(resolved_rule, connection)


def connect_entrances_function(world: "DeathsDoorWorld"):
    def replicate_placement_in_jefferson(placement: Entrance):
        # replicate the valid connections for the Jefferson regions
        try:
            start_region = world.get_region(
                placement.parent_region.name + jefferson_tag
            )
        except KeyError:
            start_region = None
        try:
            end_region = world.get_region(
                placement.connected_region.name + jefferson_tag
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
                find_two_way_transition_name(placement.parent_region.name, True)
            )
            world.create_entrance(start_region, end_region, scene_transition.rule)

    if world.options.entrance_randomization != EntranceRandomization.option_off:
        coupled = (
            world.options.entrance_randomization == EntranceRandomization.option_coupled
        )

        # Create all the dangling ends
        create_er_targets_and_exits(world, two_way_scene_transitions)
        create_er_targets_and_exits(world, one_way_scene_transitions)

        # Plando
        if world.options.plando_connections:
            connect_plando(world, world.options.plando_connections, coupled)

        # Randomize specifically the one-ways
        randomize_one_ways(world)

        # First phase of randomization until Jefferson has been reached
        jefferson_reached_result = randomize_entrances_until_region_reachable(
            world,
            world.get_region(R.STRANDED_SAILOR.value + jefferson_tag),
            coupled,
            {DeathsDoorConnectionGroup.STANDARD: [DeathsDoorConnectionGroup.STANDARD]},
        )
        for placement in jefferson_reached_result.placements:
            world.entrance_pairings[
                find_two_way_transition_name(placement.parent_region.name, True)
            ] = find_two_way_transition_name(placement.connected_region.name, False)
            replicate_placement_in_jefferson(placement)

        # Second phase of randomization until Jefferson's end point has been reached
        jefferson_end_result = randomize_entrances_until_region_reachable(
            world,
            world.get_region(R.FLOODED_FORTRESS_ENTRANCE_JEFFERSON.value),
            coupled,
            {
                DeathsDoorConnectionGroup.JEFFERSON: [
                    DeathsDoorConnectionGroup.JEFFERSON
                ]
            },
        )
        for placement in jefferson_end_result.placements:
            world.entrance_pairings[
                find_two_way_transition_name(
                    placement.parent_region.name.replace(jefferson_tag, ""), True
                )
            ] = find_two_way_transition_name(
                placement.connected_region.name.replace(jefferson_tag, ""), False
            )

            # replicate the connections for the non-Jefferson regions
            start_region = world.get_region(
                placement.parent_region.name.replace(jefferson_tag, "")
            )
            end_region = world.get_region(
                placement.connected_region.name.replace(jefferson_tag, "")
            )
            remove_dangling_exit(start_region)
            remove_dangling_entrance(end_region)
            scene_transition, _ = find_scene_transition_from_name(
                find_two_way_transition_name(
                    placement.parent_region.name.replace(jefferson_tag, ""), True
                )
            )
            world.create_entrance(start_region, end_region, scene_transition.rule)

        final_result = randomize_entrances(
            world,
            coupled,
            {DeathsDoorConnectionGroup.STANDARD: [DeathsDoorConnectionGroup.STANDARD]},
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
                    and ex.randomization_group == DeathsDoorConnectionGroup.STANDARD
                ],
                key=lambda x: x.name,
            ),
        )

        for placement in final_result.placements:
            world.entrance_pairings[
                find_two_way_transition_name(placement.parent_region.name, True)
            ] = find_two_way_transition_name(placement.connected_region.name, False)
            replicate_placement_in_jefferson(placement)  # to give fill more options

        if coupled:
            direction = "both"
        else:
            direction = "entrance"
        for entrance, exit in world.entrance_pairings.items():
            world.multiworld.spoiler.set_entrance(
                entrance, exit, direction, world.player
            )


def randomize_entrances_until_region_reachable(
    world: "DeathsDoorWorld",
    reachable_region: Region,
    coupled: bool,
    target_group_lookup: dict[int, list[int]],
    preserve_group_order: bool = False,
    er_targets: list[Entrance] | None = None,
    exits: list[Entrance] | None = None,
    on_connect: (
        Callable[[ERPlacementState, list[Entrance], list[Entrance]], bool | None] | None
    ) = None,
) -> ERPlacementState:
    """
    Randomizes Entrances for a single world in the multiworld until a region has been reached.

    :param world: Your World instance
    :param reachable_region: the Region to reach
    :param coupled: Whether connected entrances should be coupled to go in both directions
    :param target_group_lookup: Map from each group to a list of the groups that it can be connect to. Every group
                                used on an exit must be provided and must map to at least one other group. The default
                                group is 0.
    :param preserve_group_order: Whether the order of groupings should be preserved for the returned target_groups
    :param er_targets: The list of ER targets (Entrance objects with no parent region) to use for randomization.
                       Remember to be deterministic! If not provided, automatically discovers all valid targets
                       in your world.
    :param exits: The list of exits (Entrance objects with no target region) to use for randomization.
                  Remember to be deterministic! If not provided, automatically discovers all valid exits in your world.
    :param on_connect: A callback function which allows specifying side effects after a placement is completed
                       successfully and the underlying collection state has been updated. The arguments are
                       1. The ER state
                       2. The exits placed in this placement pass
                       3. The entrances they were connected to.
                       If you use on_connect to make additional placements, you are expected to return True to inform
                       GER that an additional sweep is needed.
    """
    if not world.explicit_indirect_conditions:
        raise EntranceRandomizationError(
            "Entrance randomization requires explicit indirect conditions in order "
            + "to correctly analyze whether dead end regions can be required in logic."
        )

    start_time = time.perf_counter()
    # similar to fill, skip validity checks on entrances if the game is beatable on minimal accessibility
    perform_validity_check = True

    if not er_targets:
        er_targets = sorted(
            [
                entrance
                for region in world.multiworld.get_regions(world.player)
                for entrance in region.entrances
                if not entrance.parent_region
                and entrance.randomization_group in target_group_lookup.keys()
            ],
            key=lambda x: x.name,
        )
    if not exits:
        exits = sorted(
            [
                ex
                for region in world.multiworld.get_regions(world.player)
                for ex in region.exits
                if not ex.connected_region
                and ex.randomization_group in target_group_lookup.keys()
            ],
            key=lambda x: x.name,
        )
    if len(er_targets) != len(exits):
        raise EntranceRandomizationError(
            f"Unable to randomize entrances due to a mismatched count of "
            f"entrances ({len(er_targets)}) and exits ({len(exits)}."
        )

    # used when membership checks are needed on the exit list, e.g. speculative sweep
    exits_set = set(exits)

    er_state = ERPlacementState(
        world, EntranceLookup(world.random, coupled, exits_set, er_targets), coupled
    )
    # place the menu region and connected start region(s)
    er_state.collection_state.update_reachable_regions(world.player)

    def do_placement(source_exit: Entrance, target_entrance: Entrance) -> None:
        placed_exits, paired_entrances = er_state.connect(source_exit, target_entrance)
        # propagate new connections
        er_state.collection_state.update_reachable_regions(world.player)
        er_state.collection_state.sweep_for_advancements()
        if on_connect:
            change = on_connect(er_state, placed_exits, paired_entrances)
            if change:
                er_state.collection_state.update_reachable_regions(world.player)
                er_state.collection_state.sweep_for_advancements()

    def needs_speculative_sweep(
        dead_end: bool, require_new_exits: bool, placeable_exits: list[Entrance]
    ) -> bool:
        # speculative sweep is expensive. We currently only do it as a last resort, if we might cap off the graph
        # entirely
        if len(placeable_exits) > 1:
            return False

        # in certain stages of randomization we either expect or don't care if the search space shrinks.
        # we should never speculative sweep here.
        if dead_end or not require_new_exits or not perform_validity_check:
            return False

        # edge case - if all dead ends have pre-placed progression or indirect connections, they are pulled forward
        # into the non dead end stage. In this case, and only this case, it's possible that the last connection may
        # actually be placeable in stage 1. We need to skip speculative sweep in this case because we expect the graph
        # to get capped off.

        # check to see if we are proposing the last placement
        if not coupled:
            # in uncoupled, this check is easy as there will only be one target.
            is_last_placement = len(er_state.entrance_lookup) == 1
        else:
            # a bit harder, there may be 1 or 2 targets depending on if the exit to place is one way or two way.
            # if it is two way, we can safely assume that one of the targets is the logical pair of the exit.
            desired_target_count = (
                2
                if placeable_exits[0].randomization_type == EntranceType.TWO_WAY
                else 1
            )
            is_last_placement = len(er_state.entrance_lookup) == desired_target_count
        # if it's not the last placement, we need a sweep
        return not is_last_placement

    def find_pairing(dead_end: bool, require_new_exits: bool) -> bool:
        nonlocal perform_validity_check
        placeable_exits = er_state.find_placeable_exits(perform_validity_check, exits)
        for source_exit in placeable_exits:
            target_groups = target_group_lookup[source_exit.randomization_group]
            for target_entrance in er_state.entrance_lookup.get_targets(
                target_groups, dead_end, preserve_group_order
            ):
                # when requiring new exits, ideally we would like to make it so that every placement increases
                # (or keeps the same number of) reachable exits. The goal is to continue to expand the search space
                # so that we do not crash. In the interest of performance and bias reduction, generally, just checking
                # that we are going to a new region is a good approximation. however, we should take extra care on the
                # very last exit and check whatever exits we open up are functionally accessible.
                # this requirement can be ignored on a beaten minimal, islands are no issue there.
                exit_requirement_satisfied = (
                    not perform_validity_check
                    or not require_new_exits
                    or target_entrance.connected_region not in er_state.placed_regions
                )
                if exit_requirement_satisfied and source_exit.can_connect_to(
                    target_entrance, dead_end, er_state
                ):
                    if needs_speculative_sweep(
                        dead_end, require_new_exits, placeable_exits
                    ) and not er_state.test_speculative_connection(
                        source_exit, target_entrance, exits_set
                    ):
                        continue
                    do_placement(source_exit, target_entrance)
                    return True
        else:
            # no source exits had any valid target so this stage is deadlocked. retries may be implemented if early
            # deadlocking is a frequent issue.
            lookup = (
                er_state.entrance_lookup.dead_ends
                if dead_end
                else er_state.entrance_lookup.others
            )

            # if we're in a stage where we're trying to get to new regions, we could also enter this
            # branch in a success state (when all regions of the preferred type have been placed, but there are still
            # additional unplaced entrances into those regions)
            if require_new_exits:
                if all(e.connected_region in er_state.placed_regions for e in lookup):
                    return False

            # if we're on minimal accessibility and can guarantee the game is beatable,
            # we can prevent a failure by bypassing future validity checks. this check may be
            # expensive; fortunately we only have to do it once
            if (
                perform_validity_check
                and world.options.accessibility == Accessibility.option_minimal
                and world.multiworld.has_beaten_game(
                    er_state.collection_state, world.player
                )
            ):
                # ensure that we have enough locations to place our progression
                accessible_location_count = 0
                prog_item_count = len(
                    [
                        item
                        for item in world.multiworld.itempool
                        if item.advancement and item.player == world.player
                    ]
                )
                # short-circuit location checking in this case
                if prog_item_count == 0:
                    return True
                for region in er_state.placed_regions:
                    for loc in region.locations:
                        if not loc.item and loc.can_reach(er_state.collection_state):
                            # don't count locations with preplaced items
                            accessible_location_count += 1
                            if accessible_location_count >= prog_item_count:
                                perform_validity_check = False
                                # pretend that this was successful to retry the current stage
                                return True

            unplaced_entrances = [
                entrance
                for region in world.multiworld.get_regions(world.player)
                for entrance in region.entrances
                if not entrance.parent_region
            ]
            unplaced_exits = [
                exit_
                for region in world.multiworld.get_regions(world.player)
                for exit_ in region.exits
                if not exit_.connected_region
            ]
            entrance_kind = "dead ends" if dead_end else "non-dead ends"
            region_access_requirement = (
                "requires" if require_new_exits else "does not require"
            )
            raise EntranceRandomizationError(
                f"None of the available entrances are valid targets for the available exits.\n"
                f"Randomization stage is placing {entrance_kind} and {region_access_requirement} "
                f"new region/exit access by default\n"
                f"Placeable entrances: {lookup}\n"
                f"Placeable exits: {placeable_exits}\n"
                f"All unplaced entrances: {unplaced_entrances}\n"
                f"All unplaced exits: {unplaced_exits}"
            )

    # stage 1 - try to place all the non-dead-end entrances
    while er_state.entrance_lookup.others:
        if (
            reachable_region in er_state.collection_state.reachable_regions
            or not find_pairing(dead_end=False, require_new_exits=True)
        ):
            break
    # stage 2 - try to place all the dead-end entrances
    while er_state.entrance_lookup.dead_ends:
        if (
            reachable_region in er_state.collection_state.reachable_regions
            or not find_pairing(dead_end=True, require_new_exits=True)
        ):
            break

    running_time = time.perf_counter() - start_time
    if running_time > 1.0:
        logging.info(
            f"Took {running_time:.4f} seconds during entrance randomization to reach {reachable_region.name} for player {world.player},"
            f"named {world.multiworld.player_name[world.player]}"
        )

    return er_state


# defs Credit to alwaysintreble's Messenger code
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