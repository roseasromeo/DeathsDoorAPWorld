import dataclasses
from typing import TYPE_CHECKING, Any, Iterable, override

from BaseClasses import CollectionState

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
    )


if TYPE_CHECKING:
    from . import DeathsDoorWorld

jefferson_present_attr = "jefferson_present"

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

@dataclasses.dataclass()
class NoJefferson(Rule["DeathsDoorWorld"], game="Death's Door"):
    def _instantiate(self, world: "DeathsDoorWorld") -> Rule.Resolved:
        return self.Resolved(player=world.player)
    
    class Resolved(Rule.Resolved):
        def _evaluate(self, state: CollectionState) -> bool:
            return not getattr(state, jefferson_present_attr, False)
        
@dataclasses.dataclass()
class CanJeffersonTraverse(Rule["DeathsDoorWorld"], game="Death's Door"):
    def _instantiate(self, world: "DeathsDoorWorld") -> Rule.Resolved:
        return self.Resolved(world, player=world.player)
    
    class Resolved(Rule.Resolved):
        world: "DeathsDoorWorld"
        
        def _evaluate(self, state: CollectionState) -> bool:
            jefferson_start_region_str = R.STRANDED_SAILOR_JEFFERSON_QUEST_START.value
            jefferson_start_region = self.world.get_region(jefferson_start_region_str)
            if not state.can_reach_region(jefferson_start_region_str, self.player):
                return False
            temp_state = state.copy()
            setattr(temp_state, jefferson_present_attr, True)
            temp_state.stale[self.player] = True
            temp_state.reachable_regions[self.player] = set()
            temp_state.reachable_regions[self.player].add(jefferson_start_region)
            temp_state.blocked_connections[self.player] = set()
            temp_state.blocked_connections[self.player].update(jefferson_start_region.exits)
            temp_state.update_reachable_regions(self.player)
            return temp_state.can_reach_region(R.FLOODED_FORTRESS_ENTRANCE, self.player)
        
        ##TODO: region dependencies??