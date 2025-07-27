from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has, NoJefferson
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R

# TODO Change main region to door connections to require Door (instead of Scene transition)


scene_transition_entrances: list[DeathsDoorEntrance] = [
    #########################
    ### SCENE TRANSITIONS ### (Separated for Entrance Rando purposes)
    DeathsDoorEntrance(R.DOOR_TO_GROVE_OF_SPIRITS, R.GROVE_OF_SPIRITS_DOOR, None),
    DeathsDoorEntrance(
        R.GROVE_OF_SPIRITS_DOOR,
        R.DOOR_TO_GROVE_OF_SPIRITS,
        Has(I.GROVE_OF_SPIRITS_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(R.DOOR_TO_LOST_CEMETERY, R.LOST_CEMETERY_DOOR, None),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_DOOR,
        R.DOOR_TO_LOST_CEMETERY,
        Has(I.LOST_CEMETERY_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.DOOR_TO_ESTATE_OF_THE_URN_WITCH, R.ESTATE_OF_THE_URN_WITCH_DOOR, None
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_DOOR,
        R.DOOR_TO_ESTATE_OF_THE_URN_WITCH,
        Has(I.ESTATE_OF_THE_URN_WITCH_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(R.DOOR_TO_CERAMIC_MANOR, R.CERAMIC_MANOR_DOOR, None),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_DOOR,
        R.DOOR_TO_CERAMIC_MANOR,
        Has(I.CERAMIC_MANOR_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(R.DOOR_TO_INNER_FURNACE, R.INNER_FURNACE_DOOR, None),
    DeathsDoorEntrance(
        R.INNER_FURNACE_DOOR,
        R.DOOR_TO_INNER_FURNACE,
        Has(I.INNER_FURNACE_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.DOOR_TO_URN_WITCHS_LABORATORY, R.URN_WITCHS_LABORATORY_DOOR, None
    ),
    DeathsDoorEntrance(
        R.URN_WITCHS_LABORATORY_DOOR,
        R.DOOR_TO_URN_WITCHS_LABORATORY,
        Has(I.THE_URN_WITCHS_LABORATORY_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(R.DOOR_TO_OVERGROWN_RUINS, R.OVERGROWN_RUINS_DOOR, None),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_DOOR,
        R.DOOR_TO_OVERGROWN_RUINS,
        Has(I.OVERGROWN_RUINS_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(R.DOOR_TO_MUSHROOM_DUNGEON, R.MUSHROOM_DUNGEON_DOOR, None),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_DOOR,
        R.DOOR_TO_MUSHROOM_DUNGEON,
        Has(I.MUSHROOM_DUNGEON_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(R.DOOR_TO_FLOODED_FORTRESS, R.FLOODED_FORTRESS_DOOR, None),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_DOOR,
        R.DOOR_TO_FLOODED_FORTRESS,
        Has(I.FLOODED_FORTRESS_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.DOOR_TO_THRONE_OF_THE_FROG_KING, R.THRONE_OF_THE_FROG_KING_DOOR, None
    ),
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING_DOOR,
        R.DOOR_TO_THRONE_OF_THE_FROG_KING,
        Has(I.THRONE_OF_THE_FROG_KING_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(R.DOOR_TO_STRANDED_SAILOR, R.STRANDED_SAILOR_DOOR, None),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_DOOR,
        R.DOOR_TO_STRANDED_SAILOR,
        Has(I.STRANDED_SAILOR_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(R.DOOR_TO_CASTLE_LOCKSTONE, R.CASTLE_LOCKSTONE_DOOR, None),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_DOOR,
        R.DOOR_TO_CASTLE_LOCKSTONE,
        Has(I.CASTLE_LOCKSTONE_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.DOOR_TO_CAMP_OF_THE_FREE_CROWS, R.CAMP_OF_THE_FREE_CROWS_DOOR, None
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_DOOR,
        R.DOOR_TO_CAMP_OF_THE_FREE_CROWS,
        Has(I.CAMP_OF_THE_FREE_CROWS_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(R.DOOR_TO_OLD_WATCHTOWERS, R.OLD_WATCHTOWERS_DOOR, None),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_DOOR,
        R.DOOR_TO_OLD_WATCHTOWERS,
        Has(I.OLD_WATCHTOWERS_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(R.DOOR_TO_BETTYS_LAIR, R.BETTYS_LAIR_DOOR, None),
    DeathsDoorEntrance(
        R.BETTYS_LAIR_DOOR,
        R.DOOR_TO_BETTYS_LAIR,
        Has(I.BETTYS_LAIR_DOOR) & NoJefferson(),
    ),
    DeathsDoorEntrance(
        R.GROVE_OF_SPIRITS_EXIT_TO_LOST_CEMETERY,
        R.LOST_CEMETERY_EXIT_TO_GROVE_OF_SPIRITS,
        None,
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_EXIT_TO_GROVE_OF_SPIRITS,
        R.GROVE_OF_SPIRITS_EXIT_TO_LOST_CEMETERY,
        None,
    ),  ## The backwards transition here is not meaningful for now because you can't get back to the exit from the main part of Lost Cemetery, but would be meaningful in decoupled entrance rando
    DeathsDoorEntrance(
        R.LOST_CEMETERY_EXIT_TO_CRYPT,
        R.CRYPT_EXIT_TO_LOST_CEMETERY,
        None,
    ),
    DeathsDoorEntrance(
        R.CRYPT_EXIT_TO_LOST_CEMETERY,
        R.LOST_CEMETERY_EXIT_TO_CRYPT,
        None,
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS,
        R.OVERGROWN_RUINS_EXIT_TO_LOST_CEMETERY,
        Has(I.FIRE),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_EXIT_TO_LOST_CEMETERY,
        R.LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS,
        None,
    ),
    DeathsDoorEntrance(
        R.CRYPT_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CRYPT,
        None,
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CRYPT,
        R.CRYPT_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        None,
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CERAMIC_MANOR,
        R.CERAMIC_MANOR_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        None,
    ),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CERAMIC_MANOR,
        None,
    ),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
        R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_CERAMIC_MANOR,
        None,
    ),
    DeathsDoorEntrance(
        R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_CERAMIC_MANOR,
        R.CERAMIC_MANOR_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
        None,
    ),
    DeathsDoorEntrance(
        R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_INNER_FURNACE,
        R.INNER_FURNACE_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
        None,
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
        R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_INNER_FURNACE,
        None,
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_EXIT_TO_URN_WITCHS_LABORATORY,
        R.URN_WITCHS_LABORATORY_EXIT_TO_INNER_FURNACE,
        None,
    ),
    DeathsDoorEntrance(
        R.URN_WITCHS_LABORATORY_EXIT_TO_INNER_FURNACE,
        R.INNER_FURNACE_EXIT_TO_URN_WITCHS_LABORATORY,
        None,
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_EXIT_TO_STRANDED_SAILOR,
        R.STRANDED_SAILOR_CAVES_EXIT_TO_LOST_CEMETERY,
        None,
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_CAVES_EXIT_TO_LOST_CEMETERY,
        R.LOST_CEMETERY_EXIT_TO_STRANDED_SAILOR,
        None,
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_CAVES_EXIT_TO_STRANDED_SAILOR,
        R.STRANDED_SAILOR_EXIT_TO_STRANDED_SAILOR_CAVES,
        None,
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_EXIT_TO_STRANDED_SAILOR_CAVES,
        R.STRANDED_SAILOR_CAVES_EXIT_TO_STRANDED_SAILOR,
        None,
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_EXIT_TO_CASTLE_LOCKSTONE,
        R.CASTLE_LOCKSTONE_EXIT_TO_STRANDED_SAILOR,
        None,
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EXIT_TO_STRANDED_SAILOR,
        R.STRANDED_SAILOR_EXIT_TO_CASTLE_LOCKSTONE,
        None,
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EXIT_TO_CAMP,
        R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_CASTLE_LOCKSTONE,
        None,
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_CASTLE_LOCKSTONE,
        R.CASTLE_LOCKSTONE_EXIT_TO_CAMP,
        None,
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_OLD_WATCHTOWERS,
        R.OLD_WATCHTOWERS_EXIT_TO_CAMP_OF_THE_FREE_CROWS,
        None,
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_EXIT_TO_CAMP_OF_THE_FREE_CROWS,
        R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_OLD_WATCHTOWERS,
        None,
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_EXIT_TO_BETTYS_LAIR,
        R.BETTYS_LAIR_EXIT_TO_OLD_WATCHTOWERS,
        None,
    ),
    DeathsDoorEntrance(
        R.BETTYS_LAIR_EXIT_TO_OLD_WATCHTOWERS,
        R.OLD_WATCHTOWERS_EXIT_TO_BETTYS_LAIR,
        None,
    ),
    # DeathsDoorEntrance(
    #     R.OVERGROWN_RUINS_EXIT_TO_MUSHROOM_DUNGEON_MAIN,
    #     R.MUSHROOM_DUNGEON_EXIT_TO_OVERGROWN_RUINS_MAIN,
    #     None,
    # ),
    # DeathsDoorEntrance(
    #     R.MUSHROOM_DUNGEON_EXIT_TO_OVERGROWN_RUINS_MAIN,
    #     R.OVERGROWN_RUINS_EXIT_TO_MUSHROOM_DUNGEON_MAIN,
    #     None,
    # ), ##TODO: set up meaningful scene transition entrances for Mushroom Dungeon <-> Overgrown Ruins
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_EXIT_TO_FLOODED_FORTRESS,
        R.FLOODED_FORTRESS_EXIT_TO_MUSHROOM_DUNGEON,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_EXIT_TO_MUSHROOM_DUNGEON,
        R.MUSHROOM_DUNGEON_EXIT_TO_FLOODED_FORTRESS,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_EXIT_TO_THRONE_OF_THE_FROG_KING,
        R.THRONE_OF_THE_FROG_KING_EXIT_TO_FLOODED_FORTRESS,
        None,
    ),
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING_EXIT_TO_FLOODED_FORTRESS,
        R.FLOODED_FORTRESS_EXIT_TO_THRONE_OF_THE_FROG_KING,
        None,
    ),
    # Ancient Doors
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_ANCIENT_DOOR,
        R.FIRE_AVARICE,
        NoJefferson(),
    ),  # No return journey (I think)
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_ANCIENT_DOOR,
        R.HOOKSHOT_AVARICE,
        NoJefferson(),
    ),  # No return journey (I think)
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_ANCIENT_DOOR,
        R.BOMB_AVARICE,
        NoJefferson(),
    ),  # No return journey (I think)
]
