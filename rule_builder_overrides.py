import dataclasses
from typing import TYPE_CHECKING, Any, Iterable
from typing_extensions import override

from collections import deque

from BaseClasses import CollectionState, Region

from .items import ItemGroup as IG, DeathsDoorItemName as I
from .locations import DeathsDoorLocationName as L
from .events import DeathsDoorEventName as E
from .regions import DeathsDoorRegionName as R

try:
    from rule_builder import (
        OptionFilter,
        Has as RBHas,
        HasAll as RBHasAll,
        HasAny as RBHasAny,
        HasGroup as RBHasGroup,
        CanReachLocation as RBCanReachLocation,
        CanReachRegion as RBCanReachRegion,
        Rule,
    )
except ModuleNotFoundError:
    from .rule_builder import (
        OptionFilter,
        Has as RBHas,
        HasAll as RBHasAll,
        HasAny as RBHasAny,
        HasGroup as RBHasGroup,
        CanReachLocation as RBCanReachLocation,
        CanReachRegion as RBCanReachRegion,
        Rule,
        Rule,
    )

if TYPE_CHECKING:
    from . import DeathsDoorWorld


# Override Has, etc. to take DeathsDoorItemName enum instead of string
@dataclasses.dataclass()
class Has(RBHas, game="Death's Door"):

    @override
    def __init__(
        self, item_name: I | E, count=1, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(item_name.value, count=count, options=options)


@dataclasses.dataclass()
class HasAny(RBHasAny, game="Death's Door"):

    @override
    def __init__(
        self, *item_names: I | E, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(
            *tuple(item_name.value for item_name in item_names), options=options
        )


@dataclasses.dataclass()
class HasAll(RBHasAll, game="Death's Door"):

    @override
    def __init__(
        self, *item_names: I | E, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(
            *tuple(item_name.value for item_name in item_names), options=options
        )


@dataclasses.dataclass()
class HasGroup(RBHasGroup, game="Death's Door"):

    @override
    def __init__(
        self, item_name_group: IG, count=1, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(item_name_group.value, count=count, options=options)

@dataclasses.dataclass()
class CanReachLocation(RBCanReachLocation, game="Death's Door"):

    @override
    def __init__(
        self, location_name: L, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(location_name.value, options=options)

@dataclasses.dataclass()
class CanReachRegion(RBCanReachRegion, game="Death's Door"):

    @override
    def __init__(
        self, region_name: R, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(region_name.value, options=options)

jefferson_present_attr = "jefferson_present"
@dataclasses.dataclass()
class NoJefferson(Rule["DeathsDoorWorld"], game="Death's Door"):
    def _instantiate(self, world: "DeathsDoorWorld") -> "Resolved":
        return self.Resolved(player=world.player)
    
    class Resolved(Rule.Resolved):
        def _evaluate(self, state: CollectionState) -> bool:
            return not getattr(state, jefferson_present_attr, False)

        
@dataclasses.dataclass()
class CanJeffersonTraverse(Rule["DeathsDoorWorld"], game="Death's Door"):
    def _instantiate(self, world: "DeathsDoorWorld") -> "Resolved":
        return self.Resolved(player=world.player)
    
    class Resolved(Rule.Resolved):
        def _evaluate(self, state: CollectionState) -> bool:
            ## Copy state method
            # jefferson_start_region_str = R.STRANDED_SAILOR_JEFFERSON_QUEST_START.value
            # if not state.can_reach_region(jefferson_start_region_str, self.player):
            #     return False
            # jefferson_start_region = self.world.get_region(jefferson_start_region_str)
            # temp_state = state.copy()
            # setattr(temp_state, jefferson_present_attr, True)
            # temp_state.stale[self.player] = True
            # temp_state.reachable_regions[self.player] = set()
            # temp_state.reachable_regions[self.player].add(jefferson_start_region)
            # temp_state.blocked_connections[self.player] = set()
            # temp_state.blocked_connections[self.player].update(jefferson_start_region.exits)
            # temp_state.update_reachable_regions(self.player)
            # return temp_state.can_reach_region(R.FLOODED_FORTRESS_ENTRANCE, self.player)

            jefferson_start_region_str = R.STRANDED_SAILOR_JEFFERSON_QUEST_START.value
            if not state.can_reach_region(jefferson_start_region_str, self.player):
                return False
            jefferson_start_region = state.multiworld.get_region(jefferson_start_region_str, self.player)
            jefferson_end_region = state.multiworld.get_region(R.FLOODED_FORTRESS_ENTRANCE.value, self.player)
            temp_state = CollectionState(state.multiworld)
            temp_state.prog_items = state.prog_items
            temp_state.advancements = state.advancements # grabbing events, etc. because need lamps and switchs to be set
            setattr(temp_state, jefferson_present_attr, True)
            return can_traverse_path_with_jefferson(temp_state, jefferson_start_region, jefferson_end_region)
            
        ##TODO: region dependencies??

# This function is heavily borrowed from update_reachable_regions, but allows for short-circuiting if the final destination is reached early
def can_traverse_path_with_jefferson(state: CollectionState, start_region: Region, end_region: Region) -> bool:
    blocked_connections = set(start_region.exits)
    queue = deque(blocked_connections)
    reachable_regions = {start_region}
    # run BFS on all connections, and keep track of those blocked by missing items
    while queue:
        connection = queue.popleft()
        new_region = connection.connected_region
        if new_region == end_region:
            return True
        if new_region in reachable_regions:
            blocked_connections.remove(connection)
        elif connection.access_rule(state):
            assert new_region, f"tried to search through an Entrance \"{connection}\" with no connected Region"
            reachable_regions.add(new_region)
            blocked_connections.remove(connection)
            blocked_connections.update(new_region.exits)
            queue.extend(new_region.exits)

            # Retry connections if the new region can unblock them
            for new_entrance in state.multiworld.indirect_connections.get(new_region, set()):
                if new_entrance in blocked_connections and new_entrance not in queue:
                    queue.append(new_entrance)
    return False