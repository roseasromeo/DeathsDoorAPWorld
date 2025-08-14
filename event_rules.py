from typing import TYPE_CHECKING
from .rule_builder_overrides import Has, HasAll, CanReachLocation, CanReachRegion
from .items import DeathsDoorItemName as I
from .locations import DeathsDoorLocationName as L
from .regions import DeathsDoorRegionName as R
from .options import StartDayOrNight
from .events import (
    DeathsDoorEventLocationName as EL,
    DeathsDoorEventName as E,
    event_location_table,
    pot_table,
)

try:
    from rule_builder import (
        Rule,
        True_,
        OptionFilter,
    )
except ModuleNotFoundError:
    from .rule_builder import (
        Rule,
        True_,
        OptionFilter,
    )

if TYPE_CHECKING:
    from . import DeathsDoorWorld


pot_specific_rules: dict[EL, Rule["DeathsDoorWorld"]] = {
    EL.POT_CATACOMBS_ROOM_2: Has(I.FIRE),
    EL.POT_BOMB_SILENT_SERVANT: Has(I.BOMB),
    EL.POT_MANOR_IMP_LOFT: Has(I.FIRE),  ##TODO: Check?
    EL.POT_HOOKSHOT_SILENT_SERVANT: Has(I.LEVER_HOOKSHOT_SILENT_SERVANT),
    EL.POT_LOCKSTONE_WEST_KEYED_CROW: Has(I.PINK_KEY, 5),
    EL.POT_FORTRESS_MAIN_GATE: Has(I.BOMB),
}


deaths_door_event_rules: dict[EL, Rule["DeathsDoorWorld"] | None] = {
    EL.LORD_OF_DOORS: CanReachLocation(L.RUSTY_BELLTOWER_KEY),  # TODO: Goals
    EL.LOST_CEMETERY_OPENED_EXIT_TO_SAILOR: Has(I.FIRE),
    EL.ACCESS_TO_NIGHT: True_(options=[OptionFilter(StartDayOrNight, 1)])
    | (Has(I.RUSTY_BELLTOWER_KEY) & CanReachRegion(R.LOST_CEMETERY_BELLTOWER)),
    EL.ACCESS_TO_DAY: True_(options=[OptionFilter(StartDayOrNight, 0)])
    | (Has(I.RUSTY_BELLTOWER_KEY) & CanReachRegion(R.LOST_CEMETERY_BELLTOWER)),
    EL.GREY_CROW_BOSS: HasAll(
        I.GIANT_SOUL_OF_BETTY,
        I.GIANT_SOUL_OF_THE_FROG_KING,
        I.GIANT_SOUL_OF_THE_URN_WITCH,
    ),
    EL.ACTIVATED_FURNACE_BURNERS: Has(I.FIRE),
    EL.WATCHTOWER_ENTRANCE_TORCH: HasAll(
        I.FIRE, E.ACCESS_TO_NIGHT
    ),
    EL.WATCHTOWER_JAMMING_START_TORCH: HasAll(
        I.FIRE, E.ACCESS_TO_NIGHT
    ),
    EL.WATCHTOWER_BOXES_TORCH: HasAll(
        I.FIRE, E.ACCESS_TO_NIGHT
    ),
    EL.WATCHTOWER_FIRST_POT_TORCH: HasAll(
        I.FIRE, E.ACCESS_TO_NIGHT
    ),
    EL.WATCHTOWER_BOOMERS_TORCH: HasAll(
        I.FIRE, E.ACCESS_TO_NIGHT
    ),
    EL.WATCHTOWER_BEFORE_ICE_SKATING_TORCH: HasAll(
        I.FIRE, E.ACCESS_TO_NIGHT
    ),
    EL.MUSHROOM_DUNGEON_MAIN_GATE: HasAll(
        I.MAGICAL_FOREST_HORN, E.ACCESS_TO_DAY
    ),
    EL.RESCUE_GRUNT: Has(I.BOMB),
    EL.CASTLE_LOCKSTONE_LORD_LOCKSTONE: Has(I.FIRE),
    EL.CASTLE_LOCKSTONE_LORD_OPENGATE: Has(I.FIRE),
    EL.CASTLE_LOCKSTONE_LORD_DEADBOLT: Has(I.FIRE),
    EL.CASTLE_LOCKSTONE_LORD_THEODOOR: Has(I.FIRE),
}

# Add in pots to existing tables to be able to use the same infrastructure
for pot in pot_table:
    pot_rule = Has(I.LIFE_SEED, 50)  ## TODO: Make a yaml setting
    if pot.name in pot_specific_rules.keys():
        pot_rule = pot_rule & pot_specific_rules[pot.name]
    deaths_door_event_rules[pot.name] = pot_rule


def set_event_rules(world: "DeathsDoorWorld") -> None:
    for event_location_data in event_location_table:
        if event_location_data.name in deaths_door_event_rules.keys():
            event_rule = deaths_door_event_rules[event_location_data.name]
        else:
            event_rule = None
        if event_rule is not None:
            event_location = world.get_location(
                event_location_data.name.value
            )
            world.set_rule(event_location, event_rule)
