from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .entrances import DeathsDoorEntrance
try:
    from rule_builder import Rule, False_
except ModuleNotFoundError:
    from ..rule_builder import Rule, False_
from ..rule_builder_overrides import Has, HasAny, HasAll, CanReachRegion, NoJefferson
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R
from ..events import DeathsDoorEventName as E

hall_of_doors_entrances: list[DeathsDoorEntrance] = [
# Doors in Hall of Doors
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_GROVE_OF_SPIRITS,
        Has(I.GROVE_OF_SPIRITS_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_LOST_CEMETERY,
        Has(I.LOST_CEMETERY_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_ESTATE_OF_THE_URN_WITCH,
        Has(I.ESTATE_OF_THE_URN_WITCH_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_CERAMIC_MANOR,
        Has(I.CERAMIC_MANOR_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_INNER_FURNACE,
        Has(I.INNER_FURNACE_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_URN_WITCHS_LABORATORY,
        Has(I.THE_URN_WITCHS_LABORATORY_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_OVERGROWN_RUINS,
        Has(I.OVERGROWN_RUINS_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_MUSHROOM_DUNGEON,
        Has(I.MUSHROOM_DUNGEON_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_FLOODED_FORTRESS,
        Has(I.FLOODED_FORTRESS_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_THRONE_OF_THE_FROG_KING,
        Has(I.THRONE_OF_THE_FROG_KING_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_STRANDED_SAILOR,
        Has(I.STRANDED_SAILOR_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_CASTLE_LOCKSTONE,
        Has(I.CASTLE_LOCKSTONE_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_CAMP_OF_THE_FREE_CROWS,
        Has(I.CAMP_OF_THE_FREE_CROWS_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_OLD_WATCHTOWERS,
        Has(I.OLD_WATCHTOWERS_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY,
        R.DOOR_TO_BETTYS_LAIR,
        Has(I.BETTYS_LAIR_DOOR) & NoJefferson(),
    ),
]