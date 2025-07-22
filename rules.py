from typing import TYPE_CHECKING, Any
from typing_extensions import override
import dataclasses

from .options import StartInventoryPool
from .items import ItemGroup as IG, DeathsDoorItemName as I
from .locations import location_table, DeathsDoorLocationName as L
from .events import DeathsDoorEventName as E
from .regions import DeathsDoorRegionName as R

try:
    from rule_builder import (
        Rule,
        True_,
        OptionFilter,
        Has as RBHas,
        HasAll as RBHasAll,
        HasAny as RBHasAny,
        HasGroup as RBHasGroup,
        CanReachLocation as RBCanReachLocation,
        CanReachRegion as RBCanReachRegion,
    )
except ModuleNotFoundError:
    from .rule_builder import (
        Rule,
        True_,
        OptionFilter,
        Has as RBHas,
        HasAll as RBHasAll,
        HasAny as RBHasAny,
        HasGroup as RBHasGroup,
        CanReachLocation as RBCanReachLocation,
        CanReachRegion as RBCanReachRegion,
    )
from collections.abc import Iterable

if TYPE_CHECKING:
    from . import DeathsDoorWorld


# Override Has, etc. to take DeathsDoorItemName enum instead of string
@dataclasses.dataclass
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
        self, *item_names: I, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(
            *tuple(item_name.value for item_name in item_names), options=options
        )


@dataclasses.dataclass()
class HasAll(RBHasAll, game="Death's Door"):

    @override
    def __init__(
        self, *item_names: I, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(
            *tuple(item_name.value for item_name in item_names), options=options
        )


@dataclasses.dataclass
class HasGroup(RBHasGroup, game="Death's Door"):

    @override
    def __init__(
        self, item_name_group: IG, count=1, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(item_name_group.value, count=count, options=options)

@dataclasses.dataclass
class CanReachLocation(RBCanReachLocation, game="Death's Door"):

    @override
    def __init__(
        self, location_name: L, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(location_name.value, options=options)

@dataclasses.dataclass
class CanReachRegion(RBCanReachRegion, game="Death's Door"):

    @override
    def __init__(
        self, region_name: R, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(region_name.value, options=options)

can_complete_game = True_()

# Key items


# option related


deaths_door_location_rules: dict[L, Rule["DeathsDoorWorld"] | None] = {
}


def set_location_rules(world: "DeathsDoorWorld") -> None:
    multiworld = world.multiworld
    player = world.player

    for location_data in location_table:
        rule = deaths_door_location_rules[location_data.name]
        if rule is not None:
            location = multiworld.get_location(location_data.name.value, player)
            world.set_rule(location, rule)
