from .entrance_class import DeathsDoorEntrance
from ..regions import DeathsDoorRegionName as R

door_location_entrances: list[DeathsDoorEntrance] = [
    # Door Check regions
    DeathsDoorEntrance(
        R.DOOR_TO_GROVE_OF_SPIRITS, R.DOOR_CHECK_FOR_GROVE_OF_SPIRITS, None
    ), ## not needed for now (see Hall of Doors Lobby connection below)
    DeathsDoorEntrance(
        R.GROVE_OF_SPIRITS_DOOR, R.DOOR_CHECK_FOR_GROVE_OF_SPIRITS, None
    ),  # Right now, this would be impossible to do outside of Entrance Rando. TODO: CHECK if possible in glitch settings? But also, not needed because Hall of Doors Lobby connection below
    DeathsDoorEntrance(
        R.HALL_OF_DOORS_LOBBY, R.DOOR_CHECK_FOR_GROVE_OF_SPIRITS, None
    ), ## Grants on first cutscene
    DeathsDoorEntrance(R.DOOR_TO_LOST_CEMETERY, R.DOOR_CHECK_FOR_LOST_CEMETERY, None),
    DeathsDoorEntrance(R.LOST_CEMETERY_CENTRAL, R.DOOR_CHECK_FOR_LOST_CEMETERY, None),
    DeathsDoorEntrance(
        R.DOOR_TO_ESTATE_OF_THE_URN_WITCH,
        R.DOOR_CHECK_FOR_ESTATE_OF_THE_URN_WITCH,
        None,
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        R.DOOR_CHECK_FOR_ESTATE_OF_THE_URN_WITCH,
        None,
    ),
    DeathsDoorEntrance(R.DOOR_TO_CERAMIC_MANOR, R.DOOR_CHECK_FOR_CERAMIC_MANOR, None),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY, R.DOOR_CHECK_FOR_CERAMIC_MANOR, None
    ),
    DeathsDoorEntrance(R.DOOR_TO_INNER_FURNACE, R.DOOR_CHECK_FOR_INNER_FURNACE, None),
    DeathsDoorEntrance(R.INNER_FURNACE_ENTRANCE, R.DOOR_CHECK_FOR_INNER_FURNACE, None),
    DeathsDoorEntrance(
        R.DOOR_TO_URN_WITCHS_LABORATORY,
        R.DOOR_CHECK_FOR_URN_WITCHS_LABORATORY,
        None,
    ),
    DeathsDoorEntrance(
        R.URN_WITCHS_LABORATORY,
        R.DOOR_CHECK_FOR_URN_WITCHS_LABORATORY,
        None,
    ),
    DeathsDoorEntrance(
        R.DOOR_TO_OVERGROWN_RUINS, R.DOOR_CHECK_FOR_OVERGROWN_RUINS, None
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        R.DOOR_CHECK_FOR_OVERGROWN_RUINS,
        None,
    ),
    DeathsDoorEntrance(
        R.DOOR_TO_MUSHROOM_DUNGEON, R.DOOR_CHECK_FOR_MUSHROOM_DUNGEON, None
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_LOBBY, R.DOOR_CHECK_FOR_MUSHROOM_DUNGEON, None
    ),
    DeathsDoorEntrance(
        R.DOOR_TO_FLOODED_FORTRESS, R.DOOR_CHECK_FOR_FLOODED_FORTRESS, None
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER, R.DOOR_CHECK_FOR_FLOODED_FORTRESS, None
    ),
    DeathsDoorEntrance(
        R.DOOR_TO_THRONE_OF_THE_FROG_KING,
        R.DOOR_CHECK_FOR_THRONE_OF_THE_FROG_KING,
        None,
    ),
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING, R.DOOR_CHECK_FOR_THRONE_OF_THE_FROG_KING, None
    ),
    DeathsDoorEntrance(
        R.DOOR_TO_STRANDED_SAILOR, R.DOOR_CHECK_FOR_STRANDED_SAILOR, None
    ),
    DeathsDoorEntrance(R.STRANDED_SAILOR, R.DOOR_CHECK_FOR_STRANDED_SAILOR, None),
    DeathsDoorEntrance(
        R.DOOR_TO_CASTLE_LOCKSTONE, R.DOOR_CHECK_FOR_CASTLE_LOCKSTONE, None
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL, R.DOOR_CHECK_FOR_CASTLE_LOCKSTONE, None
    ),
    DeathsDoorEntrance(
        R.DOOR_TO_CAMP_OF_THE_FREE_CROWS, R.DOOR_CHECK_FOR_CAMP_OF_THE_FREE_CROWS, None
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE, R.DOOR_CHECK_FOR_CAMP_OF_THE_FREE_CROWS, None
    ),
    DeathsDoorEntrance(
        R.DOOR_TO_OLD_WATCHTOWERS, R.DOOR_CHECK_FOR_OLD_WATCHTOWERS, None
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ENTRANCE, R.DOOR_CHECK_FOR_OLD_WATCHTOWERS, None
    ),
    DeathsDoorEntrance(R.DOOR_TO_BETTYS_LAIR, R.DOOR_CHECK_FOR_BETTYS_LAIR, None),
    DeathsDoorEntrance(R.BETTYS_LAIR, R.DOOR_CHECK_FOR_BETTYS_LAIR, None),
]
