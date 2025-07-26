from typing import TYPE_CHECKING, NamedTuple

try:
    from rule_builder import Rule, False_
except ModuleNotFoundError:
    from .rule_builder import Rule, False_
from .rule_builder_overrides import Has, HasAny, HasAll, CanReachRegion, NoJefferson
from .items import DeathsDoorItemName as I
from .regions import DeathsDoorRegionName as R
from .events import DeathsDoorEventName as E

if TYPE_CHECKING:
    from . import DeathsDoorWorld


class DeathsDoorEntrance(NamedTuple):
    starting_region: R
    ending_region: R
    rule: Rule["DeathsDoorWorld"] | None


# TODO Change main region to door connections to require Door (instead of Scene transition)

deathsdoor_entrances: list[DeathsDoorEntrance] = [
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
    # Door Check regions
    DeathsDoorEntrance(
        R.DOOR_TO_GROVE_OF_SPIRITS, R.DOOR_CHECK_FOR_GROVE_OF_SPIRITS, None
    ),
    DeathsDoorEntrance(
        R.GROVE_OF_SPIRITS_DOOR, R.DOOR_CHECK_FOR_GROVE_OF_SPIRITS, None
    ),  # Right now, this would be immpossible to do. TODO: CHECK if possible in glitch settings?
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
    # Entrances in Grove of Spirits
    DeathsDoorEntrance(R.GROVE_OF_SPIRITS_DOOR, R.GROVE_OF_SPIRITS, None),
    DeathsDoorEntrance(
        R.GROVE_OF_SPIRITS, R.GROVE_OF_SPIRITS_EXIT_TO_LOST_CEMETERY, None
    ),
    # Entrances in Lost Cemetery
    DeathsDoorEntrance(
        R.LOST_CEMETERY_EXIT_TO_GROVE_OF_SPIRITS,
        R.LOST_CEMETERY_NEAR_GROVE_OF_SPIRITS_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_NEAR_GROVE_OF_SPIRITS_DOOR,
        R.LOST_CEMETERY_EXIT_TO_GROVE_OF_SPIRITS,
        None,
    ),  ##TODO: Figure out what region the hookshot route connects to
    DeathsDoorEntrance(
        R.LOST_CEMETERY_NEAR_GROVE_OF_SPIRITS_DOOR, R.LOST_CEMETERY_CENTRAL, None
    ),  ## TODO: Check to see if reversable
    DeathsDoorEntrance(R.LOST_CEMETERY_DOOR, R.LOST_CEMETERY_CENTRAL, None),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_CENTRAL, R.LOST_CEMETERY_DOOR, Has(I.LOST_CEMETERY_DOOR)
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_STEADHONE, R.LOST_CEMETERY_CENTRAL, Has(I.LEVER_CATACOMBS_TOWER)
    ),
    DeathsDoorEntrance(R.LOST_CEMETERY_RIGHT_ARENA, R.LOST_CEMETERY_CENTRAL, None),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_NEAR_GROVE_OF_SPIRITS_DOOR,
        R.LOST_CEMETERY_RIGHT_ARENA,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS,
        R.LOST_CEMETERY_RIGHT_ARENA,
        Has(I.LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_RIGHT_ARENA,
        R.LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS,
        Has(I.LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_SUMMIT,
        R.LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS,
        None,
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_CENTRAL,
        R.LOST_CEMETERY_RIGHT_ARENA,
        HasAny(I.LEVER_GUARDIAN_OF_THE_DOOR_ACCESS, I.LEVER_CATACOMBS_TOWER),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_EXIT_TO_STRANDED_SAILOR,
        R.LOST_CEMETERY_NEAR_EXIT_TO_STRANDED_SAILOR,
        None,
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_NEAR_EXIT_TO_STRANDED_SAILOR,
        R.LOST_CEMETERY_EXIT_TO_STRANDED_SAILOR,
        None,
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_NEAR_EXIT_TO_STRANDED_SAILOR,
        R.LOST_CEMETERY_STEADHONE,
        Has(E.LOST_CEMETERY_OPENED_EXIT_TO_SAILOR),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_STEADHONE,
        R.LOST_CEMETERY_NEAR_EXIT_TO_STRANDED_SAILOR,
        Has(E.LOST_CEMETERY_OPENED_EXIT_TO_SAILOR),
    ),  ## TODO: this event seems not possible from the stranded sailor side, but maybe a glitch makes it possible
    DeathsDoorEntrance(R.LOST_CEMETERY_BELLTOWER, R.LOST_CEMETERY_STEADHONE, None),
    DeathsDoorEntrance(R.LOST_CEMETERY_EXIT_TO_CRYPT, R.LOST_CEMETERY_BELLTOWER, None),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_SUMMIT, R.LOST_CEMETERY_BELLTOWER, Has(I.PINK_KEY, 5)
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_STEADHONE,
        R.LOST_CEMETERY_BELLTOWER,
        Has(I.LEVER_CEMETERY_EXIT_TO_ESTATE),
    ),
    DeathsDoorEntrance(R.LOST_CEMETERY_BELLTOWER, R.LOST_CEMETERY_EXIT_TO_CRYPT, None),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_SUMMIT, R.LOST_CEMETERY_STEADHONE, Has(I.LEVER_CEMETERY_SEWER)
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_CENTRAL,
        R.LOST_CEMETERY_STEADHONE,
        Has(I.PINK_KEY, 5) | Has(I.LEVER_CATACOMBS_TOWER),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_CENTRAL,
        R.LOST_CEMETERY_SUMMIT,
        Has(I.LEVER_GUARDIAN_OF_THE_DOOR_ACCESS),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_STEADHONE, R.LOST_CEMETERY_SUMMIT, Has(I.LEVER_CEMETERY_SEWER)
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        Has(I.LEVER_CEMETERY_EAST_TREE),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_RIGHT_ARENA,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        HasAll(I.LEVER_CEMETERY_EAST_TREE, I.LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_SUMMIT, R.LOST_CEMETERY_EAST_TREE_BRIDGE, Has(I.FIRE)
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_CENTRAL,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        HasAny(I.FIRE, I.LEVER_CATACOMBS_EXIT),
    ),
    # Entrances in Crypt
    DeathsDoorEntrance(R.CRYPT_EXIT_TO_LOST_CEMETERY, R.CRYPT_MAIN_ROOM, None),
    DeathsDoorEntrance(R.CRYPT_MAIN_ROOM, R.CRYPT_EXIT_TO_LOST_CEMETERY, None),
    DeathsDoorEntrance(
        R.CRYPT_MAIN_ROOM,
        R.CRYPT_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        HasAll(I.LEVER_ESTATE_ELEVATOR_LEFT, I.LEVER_ESTATE_ELEVATOR_RIGHT),
    ),
    DeathsDoorEntrance(
        R.CRYPT_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        R.CRYPT_MAIN_ROOM,
        HasAll(I.LEVER_ESTATE_ELEVATOR_LEFT, I.LEVER_ESTATE_ELEVATOR_RIGHT),
    ),  ##TODO Check this connection is valid! (Not in base randomizer I think)
    # Entrances in Estate of the Urn Witch
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CRYPT, R.ESTATE_OF_THE_URN_WITCH_SOUTH, None
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_SOUTH, R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CRYPT, None
    ),  ###TODO : CHECK THAT THIS CONNECTION IS POSSIBLE
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        R.ESTATE_OF_THE_URN_WITCH_DOOR,
        Has(I.ESTATE_OF_THE_URN_WITCH_DOOR),
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_DOOR, R.ESTATE_OF_THE_URN_WITCH_SOUTH, None
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        HasAll(I.LEVER_GARDEN_OF_JOY, I.LEVER_GARDEN_OF_PEACE, I.BOMB),
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        HasAll(I.LEVER_GARDEN_OF_JOY, I.LEVER_GARDEN_OF_PEACE, I.BOMB),
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CERAMIC_MANOR,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        None,
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CERAMIC_MANOR,
        None,
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        R.ESTATE_OF_THE_URN_WITCH_URN_SHED,
        HasAny(I.HOOKSHOT, I.LEVER_ESTATE_UNDERGROUND_URN_SHED),
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        R.ESTATE_OF_THE_URN_WITCH_GARDEN_OF_LIFE_END,
        HasAny(I.LEVER_GARDEN_OF_LIFE_LANTERNS, I.LEVER_GARDEN_OF_LIFE_END),
    ),
    # Entrances in Ceramic Manor
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        None,
    ),
    DeathsDoorEntrance(R.CERAMIC_MANOR_DOOR, R.CERAMIC_MANOR_MAIN_LOBBY, None),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY, R.CERAMIC_MANOR_DOOR, Has(I.CERAMIC_MANOR_DOOR)
    ),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY,
        R.CERAMIC_MANOR_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        False_(),
    ),  ## TODO Glitch logic
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY,
        R.CERAMIC_MANOR_LEFT,
        Has(I.YELLOW_KEY, 3) | Has(I.LEVER_MANOR_BIG_POT_ARENA),
    ),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY, R.CERAMIC_MANOR_LIBRARY, Has(I.YELLOW_KEY, 3)
    ),
    # TODO: Base randomizer has a confusing "entrance" here from the Ancient Door back to Ceramic Manor... Omitting for now
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY,
        R.CERAMIC_MANOR_ANCIENT_DOOR,
        HasAll(
            E.ACCESS_TO_DAY,
            I.CROW_MANOR_AFTER_TORCH_PUZZLE,
            I.CROW_MANOR_BEDROOM,
            I.CROW_MANOR_IMP_LOFT,
            I.CROW_MANOR_IMP_LOFT,
        ),
    ),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY,
        R.CERAMIC_MANOR_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
        Has(I.YELLOW_KEY, 3) & Has(I.FIRE),
    ),
    ## TODO: Check if can return from furnace observation rooms without it being opened, not in base rando
    # Entrances in Furnace Observation Rooms
    DeathsDoorEntrance(
        R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_CERAMIC_MANOR,
        R.FURNACE_OBSERVATION_ROOMS,
        None,
    ),
    DeathsDoorEntrance(
        R.FURNACE_OBSERVATION_ROOMS,
        R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_CERAMIC_MANOR,
        None,
    ),
    DeathsDoorEntrance(
        R.FURNACE_OBSERVATION_ROOMS,
        R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_INNER_FURNACE,
        Has(I.FIRE),
    ),
    DeathsDoorEntrance(
        R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_INNER_FURNACE,
        R.FURNACE_OBSERVATION_ROOMS,
        None,
    ),
    # Entrances in Inner Furnace
    DeathsDoorEntrance(
        R.INNER_FURNACE_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
        R.INNER_FURNACE_ENTRANCE,
        None,
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_ENTRANCE,
        R.INNER_FURNACE_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
        None,
    ),
    DeathsDoorEntrance(R.INNER_FURNACE_DOOR, R.INNER_FURNACE_ENTRANCE, None),
    DeathsDoorEntrance(
        R.INNER_FURNACE_ENTRANCE, R.INNER_FURNACE_DOOR, Has(I.INNER_FURNACE_DOOR)
    ),
    DeathsDoorEntrance(R.INNER_FURNACE_POST_BURNER_1, R.INNER_FURNACE_ENTRANCE, None),
    DeathsDoorEntrance(R.INNER_FURNACE_POST_BURNER_2, R.INNER_FURNACE_ENTRANCE, None),
    DeathsDoorEntrance(R.INNER_FURNACE_POST_BURNER_3, R.INNER_FURNACE_ENTRANCE, None),
    DeathsDoorEntrance(R.INNER_FURNACE_POST_BURNER_4, R.INNER_FURNACE_ENTRANCE, None),
    DeathsDoorEntrance(R.INNER_FURNACE_POST_BURNER_7, R.INNER_FURNACE_ENTRANCE, None),
    DeathsDoorEntrance(
        R.INNER_FURNACE_ENTRANCE,
        R.INNER_FURNACE_POST_BURNER_1,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_2, R.INNER_FURNACE_POST_BURNER_1, None
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_1,
        R.INNER_FURNACE_POST_BURNER_2,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_2,
        R.INNER_FURNACE_POST_BURNER_3,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_3,
        R.INNER_FURNACE_POST_BURNER_4,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_5, R.INNER_FURNACE_POST_BURNER_4, None
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_4,
        R.INNER_FURNACE_POST_BURNER_5,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_5,
        R.INNER_FURNACE_POST_BURNER_6,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_6,
        R.INNER_FURNACE_POST_BURNER_7,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_8, R.INNER_FURNACE_POST_BURNER_7, None
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_7,
        R.INNER_FURNACE_POST_BURNER_8,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_9, R.INNER_FURNACE_POST_BURNER_8, None
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_8,
        R.INNER_FURNACE_POST_BURNER_9,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_EXIT_TO_URN_WITCHS_LABORATORY,
        R.INNER_FURNACE_POST_BURNER_9,
        None,
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_9,
        R.INNER_FURNACE_EXIT_TO_URN_WITCHS_LABORATORY,
        None,
    ),
    # Entrances in Urn Witch's Laboratory
    DeathsDoorEntrance(R.URN_WITCHS_LABORATORY_DOOR, R.URN_WITCHS_LABORATORY, None),
    DeathsDoorEntrance(
        R.URN_WITCHS_LABORATORY,
        R.URN_WITCHS_LABORATORY_DOOR,
        Has(I.THE_URN_WITCHS_LABORATORY_DOOR),
    ),
    DeathsDoorEntrance(
        R.URN_WITCHS_LABORATORY,
        R.URN_WITCHS_LABORATORY_EXIT_TO_INNER_FURNACE,
        None,
    ),
    DeathsDoorEntrance(
        R.URN_WITCHS_LABORATORY_EXIT_TO_INNER_FURNACE,
        R.URN_WITCHS_LABORATORY,
        None,
    ),
    # Entrances in Stranded Sailor Caves
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_CAVES_EXIT_TO_LOST_CEMETERY, R.STRANDED_SAILOR_CAVES, None
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_CAVES_EXIT_TO_STRANDED_SAILOR, R.STRANDED_SAILOR_CAVES, None
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_CAVES, R.STRANDED_SAILOR_CAVES_EXIT_TO_LOST_CEMETERY, None
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_CAVES, R.STRANDED_SAILOR_CAVES_EXIT_TO_STRANDED_SAILOR, None
    ),
    # Entrances in Stranded Sailor
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_EXIT_TO_STRANDED_SAILOR_CAVES, R.STRANDED_SAILOR, None
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR, R.STRANDED_SAILOR_EXIT_TO_STRANDED_SAILOR_CAVES, None
    ),
    DeathsDoorEntrance(R.STRANDED_SAILOR_DOOR, R.STRANDED_SAILOR, None),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR, R.STRANDED_SAILOR_DOOR, Has(I.STRANDED_SAILOR_DOOR)
    ),
    DeathsDoorEntrance(R.STRANDED_SAILOR_UPPER, R.STRANDED_SAILOR, Has(I.BOMB)),
    DeathsDoorEntrance(R.STRANDED_SAILOR, R.STRANDED_SAILOR_JEFFERSON, None),
    DeathsDoorEntrance(R.STRANDED_SAILOR_JEFFERSON, R.STRANDED_SAILOR, None),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_JEFFERSON,
        R.STRANDED_SAILOR_JEFFERSON_QUEST_START,
        HasAll(E.ACCESS_TO_NIGHT, I.INK_COVERED_TEDDY_BEAR),
    ),  ##TODO: Jefferson's quest/pathing is not implemented yet
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_JEFFERSON_QUEST_START,
        R.STRANDED_SAILOR_JEFFERSON,
        None,
    ),  ##TODO: Jefferson's quest/pathing is not implemented yet
    DeathsDoorEntrance(R.STRANDED_SAILOR, R.STRANDED_SAILOR_UPPER, Has(I.BOMB)),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_UPPER, R.STRANDED_SAILOR_EXIT_TO_CASTLE_LOCKSTONE, None
    ),
    # Entrances in Castle Lockstone
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EXIT_TO_STRANDED_SAILOR, R.CASTLE_LOCKSTONE_ENTRANCE, None
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_ENTRANCE, R.CASTLE_LOCKSTONE_EXIT_TO_STRANDED_SAILOR, None
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_ENTRANCE,
        Has(I.LEVER_LOCKSTONE_ENTRANCE),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_ENTRANCE,
        R.CASTLE_LOCKSTONE_CENTRAL,
        Has(I.LEVER_LOCKSTONE_ENTRANCE),
    ),
    DeathsDoorEntrance(R.CASTLE_LOCKSTONE_DOOR, R.CASTLE_LOCKSTONE_CENTRAL, None),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_DOOR,
        Has(I.CASTLE_LOCKSTONE_DOOR),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_SOUTHWEST_CROW, R.CASTLE_LOCKSTONE_ENTRANCE, None
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_SOUTHWEST_CROW,
        Has(I.LEVER_LOCKSTONE_DUAL_LASER_PUZZLE),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL, R.CASTLE_LOCKSTONE_SOUTHWEST_UPPER, Has(I.HOOKSHOT)
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_LORD_OPENGATE, R.CASTLE_LOCKSTONE_SOUTHWEST_CROW, None
    ),  # TODO: See if this connection should require Fire (implicit with current connection)
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_EAST,
        Has(I.LEVER_LOCKSTONE_EAST_LOWER),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_EAST_UPPER,
        HasAny(I.HOOKSHOT, I.LEVER_LOCKSTONE_UPPER_SHORTCUT),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EAST_UPPER,
        R.CASTLE_LOCKSTONE_EAST_UPPER_KEYED_DOOR,
        HasAll(
            I.HOOKSHOT, I.LEVER_LOCKSTONE_UPPER_PUZZLE
        ),  ##TODO: base rando notes that lever can be skipped?
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_LIBRARY,
        R.CASTLE_LOCKSTONE_ENTRANCE,
        Has(I.LEVER_LOCKSTONE_EAST_START_SHORTCUT),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_ENTRANCE,
        R.CASTLE_LOCKSTONE_LIBRARY,
        Has(I.LEVER_LOCKSTONE_EAST_START_SHORTCUT),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_LORD_DEADBOLT,  ## TODO: Check if this connection needs Fire, because Deadbolt region has it built in (might need to split lamp from region)
        R.CASTLE_LOCKSTONE_LIBRARY,
        None,
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL, R.CASTLE_LOCKSTONE_JAILED_SEED, Has(I.HOOKSHOT)
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_ROOF, R.CASTLE_LOCKSTONE_CENTRAL, None
    ),  # Fall down the elevator
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_ROOF,
        CanReachRegion(R.CASTLE_LOCKSTONE_LORD_DEADBOLT)
        & CanReachRegion(R.CASTLE_LOCKSTONE_LORD_LOCKSTONE)
        & CanReachRegion(R.CASTLE_LOCKSTONE_LORD_THEODOOR)
        & CanReachRegion(R.CASTLE_LOCKSTONE_LORD_OPENGATE),
    ),  # Can summon elevator ##TODO: See if lord lamps can be turned into events instead!
    DeathsDoorEntrance(R.CASTLE_LOCKSTONE_EXIT_TO_CAMP, R.CASTLE_LOCKSTONE_ROOF, None),
    DeathsDoorEntrance(R.CASTLE_LOCKSTONE_ROOF, R.CASTLE_LOCKSTONE_EXIT_TO_CAMP, None),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EAST_UPPER_KEYED_DOOR,
        R.CASTLE_LOCKSTONE_LORD_THEODOOR_ROOM,
        Has(I.PINK_KEY, 5)
        & HasAll(I.HOOKSHOT, I.LEVER_LOCKSTONE_UPPER_DUAL_LASER_PUZZLE),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_ANCIENT_DOOR,
        HasAll(
            E.ACCESS_TO_DAY,
            I.CROW_LOCKSTONE_EAST,
            I.CROW_LOCKSTONE_WEST,
            I.CROW_LOCKSTONE_SOUTH_WEST,
            I.CROW_LOCKSTONE_WEST_LOCKED,
        ),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL, R.CASTLE_LOCKSTONE_LORD_LOCKSTONE, Has(I.FIRE)
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_LORD_OPENGATE,
        HasAll(I.FIRE, I.HOOKSHOT, I.LEVER_LOCKSTONE_HOOKSHOT_PUZZLE),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EAST_UPPER_KEYED_DOOR,
        R.CASTLE_LOCKSTONE_LORD_DEADBOLT,
        HasAll(I.FIRE, I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_LORD_THEODOOR_ROOM,
        R.CASTLE_LOCKSTONE_LORD_THEODOOR,
        Has(I.FIRE),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_LORD_THEODOOR_ROOM,
        R.CASTLE_LOCKSTONE_EAST_CROW,
        None,
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EAST,
        R.CASTLE_LOCKSTONE_EAST_CROW,
        HasAll(
            I.LEVER_LOCKSTONE_VERTICAL_LASER_PUZZLE,
            I.LEVER_LOCKSTONE_TRACKING_BEAM_PUZZLE,
        ),
    ),
    # Entrances in Camp of the Free Crows
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_CASTLE_LOCKSTONE,
        R.CAMP_OF_THE_FREE_CROWS_CASTLE_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_CASTLE_DOOR,
        R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_CASTLE_LOCKSTONE,
        None,
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        R.CAMP_OF_THE_FREE_CROWS_CASTLE_DOOR,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_CASTLE_DOOR,
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_DOOR, R.CAMP_OF_THE_FREE_CROWS_VILLAGE, None
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        R.CAMP_OF_THE_FREE_CROWS_DOOR,
        Has(I.CAMP_OF_THE_FREE_CROWS_DOOR),
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        Has(I.HOOKSHOT),
    ),  # TODO Check if keys can be used as an alternative
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_OLD_WATCHTOWERS,
        None,
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_OLD_WATCHTOWERS,
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        None,
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        Has(I.PINK_KEY, 5),
    ),
    # Entrances in Old Watchtowers
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_EXIT_TO_CAMP_OF_THE_FREE_CROWS,
        R.OLD_WATCHTOWERS_ENTRANCE,
        None,
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ENTRANCE,
        R.OLD_WATCHTOWERS_EXIT_TO_CAMP_OF_THE_FREE_CROWS,
        None,
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_DOOR,
        R.OLD_WATCHTOWERS_ENTRANCE,
        None,
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ENTRANCE,
        R.OLD_WATCHTOWERS_DOOR,
        Has(I.OLD_WATCHTOWERS_DOOR),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_JAMMING_START,
        R.OLD_WATCHTOWERS_ENTRANCE,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ENTRANCE,
        R.OLD_WATCHTOWERS_JAMMING_START,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        R.OLD_WATCHTOWERS_JAMMING_START,
        HasAll(I.HOOKSHOT, I.LEVER_WATCHTOWERS_AFTER_BOOMERS),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_JAMMING_START,
        R.OLD_WATCHTOWERS_FIRST_POT_AREA,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_JAMMING_START,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        HasAll(I.HOOKSHOT, I.LEVER_WATCHTOWERS_AFTER_BOOMERS),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_FIRST_POT_AREA,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ICE_SKATING_START,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        R.OLD_WATCHTOWERS_LASERS_ARENA,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        # From base rando: When coming from the Barb elevator, the lever can be skipped by hooking
        # over the gate from the ledge around the top of the elevator.
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        R.OLD_WATCHTOWERS_ICE_SKATING_START,
        HasAll(I.HOOKSHOT, I.LEVER_WATCHTOWERS_BEFORE_ICE_ARENA),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        R.OLD_WATCHTOWERS_ICE_SKATING_START,
        Has(I.LEVER_WATCHTOWERS_BEFORE_ICE_ARENA),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ICE_SKATING_START,
        R.OLD_WATCHTOWERS_ICE_SKATING_END,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ICE_SKATING_START,
        R.OLD_WATCHTOWERS_BOOMERS,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_FIRST_POT_AREA,
        R.OLD_WATCHTOWERS_BOOMERS,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_LASERS_ARENA,
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ICE_SKATING_START,
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        Has(I.LEVER_WATCHTOWERS_BEFORE_ICE_ARENA),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ICE_SKATING_END,
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        Has(I.LEVER_WATCHTOWERS_AFTER_ICE_SKATING),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_CAVE_ENTRANCE,
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        Has(I.LEVER_WATCHTOWERS_AFTER_ICE_SKATING),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        R.OLD_WATCHTOWERS_CAVE_ENTRANCE,
        Has(I.LEVER_WATCHTOWERS_AFTER_ICE_SKATING),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_EXIT_TO_BETTYS_LAIR,
        R.OLD_WATCHTOWERS_CAVE_ENTRANCE,
        None,
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_CAVE_ENTRANCE,
        R.OLD_WATCHTOWERS_EXIT_TO_BETTYS_LAIR,
        None,
    ),
    # Entrances in Betty's Lair
    DeathsDoorEntrance(
        R.BETTYS_LAIR_DOOR,
        R.BETTYS_LAIR,
        None,
    ),
    DeathsDoorEntrance(
        R.BETTYS_LAIR,
        R.BETTYS_LAIR_DOOR,
        Has(I.BETTYS_LAIR_DOOR),
    ),
    DeathsDoorEntrance(
        R.BETTYS_LAIR_EXIT_TO_OLD_WATCHTOWERS,
        R.BETTYS_LAIR,
        None,
    ),
    DeathsDoorEntrance(
        R.BETTYS_LAIR,
        R.BETTYS_LAIR_EXIT_TO_OLD_WATCHTOWERS,
        None,
    ),
    # Entrances in Overgrown Ruins
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_EXIT_TO_LOST_CEMETERY,
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        None,
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        R.OVERGROWN_RUINS_EXIT_TO_LOST_CEMETERY,
        None,
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        Has(I.LEVER_RUINS_MAIN_GATE),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        Has(I.LEVER_RUINS_MAIN_GATE),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_DOOR,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        None,
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        R.OVERGROWN_RUINS_DOOR,
        Has(I.OVERGROWN_RUINS_DOOR),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        None,
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        Has(I.GREEN_KEY, 3) | Has(I.LEVER_RUINS_ENTRANCE_LADDER_SHORTCUT),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        None,
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        Has(I.LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW),
    ),
    # Entrances in Mushroom Dungeon
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_DOOR,
        R.MUSHROOM_DUNGEON_LOBBY,
        None,
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_LOBBY,
        R.MUSHROOM_DUNGEON_DOOR,
        Has(I.MUSHROOM_DUNGEON_DOOR),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        R.MUSHROOM_DUNGEON_LOBBY,
        Has(E.MUSHROOM_DUNGEON_MAIN_GATE),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        R.MUSHROOM_DUNGEON_LOBBY,
        HasAny(I.LEVER_DUNGEON_ENTRANCE_LEFT_GATE, I.LEVER_DUNGEON_ENTRANCE_RIGHT_GATE),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_LOBBY,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        Has(I.FIRE),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        Has(I.LEVER_RUINS_UPPER_DUNGEON_ENTRANCE),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_EXIT_TO_FLOODED_FORTRESS,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        R.MUSHROOM_DUNGEON_EXIT_TO_FLOODED_FORTRESS,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        None,
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        None,
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        None,
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_LOBBY,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        HasAny(I.LEVER_DUNGEON_ENTRANCE_LEFT_GATE, I.LEVER_DUNGEON_ENTRANCE_RIGHT_GATE),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        HasAny(I.LEVER_RUINS_UPPER_DUNGEON_ENTRANCE),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        Has(I.GREEN_KEY, 4),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        R.MUSHROOM_DUNGEON_ANCIENT_DOOR,
        HasAll(
            E.ACCESS_TO_DAY,
            I.CROW_DUNGEON_COBWEB,
            I.CROW_DUNGEON_HALL,
            I.CROW_DUNGEON_RIGHTMOST,
            I.CROW_DUNGEON_WATER_ARENA,
        ),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        Has(I.GREEN_KEY, 4),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        Has(I.LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        R.MUSHROOM_DUNGEON_THUNDER_HAMMER,
        Has(I.LEVER_RUINS_UPPER_DUNGEON_ENTRANCE),
    ),  # TODO: This is a scene transition
    # TODO: In ER, this would provide new access to Mushroom Dungeon, and would need to be connected to the dungeon. Omitting for now
    # Entrances in Flooded Fortress
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_EXIT_TO_MUSHROOM_DUNGEON,
        R.FLOODED_FORTRESS_ENTRANCE,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_ENTRANCE,
        R.FLOODED_FORTRESS_EXIT_TO_MUSHROOM_DUNGEON,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_ENTRANCE,
        R.FLOODED_FORTRESS_WATCHTOWER_LOWER,
        Has(I.LEVER_FORTRESS_WATCHTOWER_LOWER),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_ENTRANCE,
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_DOOR,
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        R.FLOODED_FORTRESS_DOOR,
        Has(I.FLOODED_FORTRESS_DOOR),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        HasAll(I.LEVER_FORTRESS_STATUE, I.LEVER_FORTRESS_PRE_MAIN_GATE),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        R.FLOODED_FORTRESS_INSIDE_MAIN_GATE,
        Has(I.LEVER_FORTRESS_MAIN_GATE) & HasAny(I.BOMB, I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_INSIDE_MAIN_GATE,
        R.FLOODED_FORTRESS_U_TURN,
        HasAll(I.BOMB, I.LEVER_FORTRESS_CENTRAL_SHORTCUT),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_U_TURN,
        R.FLOODED_FORTRESS_BREAKABLE_BRIDGES,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_BREAKABLE_BRIDGES,
        R.FLOODED_FORTRESS_BRIDGE,
        Has(I.LEVER_FORTRESS_BRIDGE),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_BRIDGE,
        R.FLOODED_FORTRESS_EXIT,
        Has(I.LEVER_FORTRESS_NORTH_WEST),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_EXIT,
        R.FLOODED_FORTRESS_EXIT_TO_THRONE_OF_THE_FROG_KING,
        None,
    ),
    # Entrances in Throne of the Frog King
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING_EXIT_TO_FLOODED_FORTRESS,
        R.THRONE_OF_THE_FROG_KING,
        None,
    ),
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING,
        R.THRONE_OF_THE_FROG_KING_EXIT_TO_FLOODED_FORTRESS,
        None,
    ),
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING_DOOR,
        R.THRONE_OF_THE_FROG_KING,
        None,
    ),
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING,
        R.THRONE_OF_THE_FROG_KING_DOOR,
        Has(I.THRONE_OF_THE_FROG_KING_DOOR),
    ),
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
    # ),
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
