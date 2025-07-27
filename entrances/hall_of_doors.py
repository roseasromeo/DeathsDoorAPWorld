from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has, HasAll, NoJefferson
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R

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
     # Access from Avarices
    DeathsDoorEntrance(R.FIRE_AVARICE, R.POST_FIRE_AVARICE, Has(I.FIRE)),
    DeathsDoorEntrance(
        R.POST_FIRE_AVARICE, R.HALL_OF_DOORS_LOBBY, Has(I.FIRE)
    ),  # This entrance is probably unneccessary
    DeathsDoorEntrance(R.HOOKSHOT_AVARICE, R.POST_HOOKSHOT_AVARICE, Has(I.HOOKSHOT)),
    DeathsDoorEntrance(R.POST_HOOKSHOT_AVARICE, R.HOOKSHOT_AVARICE, Has(I.HOOKSHOT)),
    DeathsDoorEntrance(R.HALL_OF_DOORS_LOBBY, R.POST_HOOKSHOT_AVARICE, Has(I.HOOKSHOT)),
    DeathsDoorEntrance(
        R.POST_HOOKSHOT_AVARICE, R.HALL_OF_DOORS_LOBBY, Has(I.HOOKSHOT)
    ),  # This entrance is probably unneccessary
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY, R.POST_BOMB_AVARICE, HasAll(I.BOMB, I.LEVER_BOMB_EXIT)
    ),
    DeathsDoorEntrance(R.BOMB_AVARICE, R.POST_BOMB_AVARICE, Has(I.BOMB)),
    DeathsDoorEntrance(R.POST_BOMB_AVARICE, R.BOMB_AVARICE, Has(I.BOMB)),
    DeathsDoorEntrance(
        R.POST_BOMB_AVARICE, R.HALL_OF_DOORS_LOBBY, HasAll(I.BOMB, I.LEVER_BOMB_EXIT)
    ),  # This entrance is probably unneccessary
]