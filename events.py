from enum import Enum
from typing import List, NamedTuple

from .regions import DeathsDoorRegionName as R


class DeathsDoorEventName(str, Enum):
    VICTORY = "Goal Complete"
    LOST_CEMETERY_OPENED_EXIT_TO_SAILOR = "Lost Cemetery Opened Exit to Sailor"
    ACCESS_TO_NIGHT = "Access to Night"
    ACCESS_TO_DAY = "Access to Day"
    GREY_CROW_BOSS = "Can Defeat Grey Crow Boss"
    ACTIVATED_FURNACE_BURNERS = "Can Activate First Furnace Burner"
    LIT_WATCHTOWER_TORCH = "Can Light a Watchtower Burner"
    MUSHROOM_DUNGEON_MAIN_GATE = "Can Open the Mushroom Dungeon Main Gate"
    RESCUE_GRUNT = "Can Rescue Grunt"
    PLANTED_SEED = "Can Plant a Seed"
    OOL = "Out of Logic Item"  # For Universal Tracker


class DeathsDoorEventLocationName(str, Enum):
    VICTORY = "Defeat the Lord of Doors"
    LOST_CEMETERY_OPENED_EXIT_TO_SAILOR = "Lost Cemetery Lamp Switch Exit to Sailor"
    ACCESS_TO_NIGHT = "Access to Night"
    ACCESS_TO_DAY = "Access to Day"
    GREY_CROW_BOSS = "Grey Crow Boss"
    ACTIVATED_FURNACE_BURNERS = "First Furnace Burner"
    WATCHTOWER_ENTRANCE_TORCH = "Watchtower Entrance Torch"
    WATCHTOWER_JAMMING_START_TORCH = "Watchtower Jamming Start Torch"
    WATCHTOWER_BOXES_TORCH = "Watchtower Boxes Torch"
    WATCHTOWER_FIRST_POT_TORCH = "Watchtower First Pot Area Torch"
    WATCHTOWER_BOOMERS_TORCH_1 = "Watchtower Boomers Torch 1"
    WATCHTOWER_BOOMERS_TORCH_2 = "Watchtower Boomers Torch 2"
    MUSHROOM_DUNGEON_MAIN_GATE = "Mushroom Dungeon Main Gate"
    RESCUE_GRUNT = "Mushroom Dungeon Grunt Rescue"
    POT_OUTSIDE_CATACOMBS_EXIT = "Pot-Outside_Catacombs_Exit"
    POT_CATACOMBS_ROOM_2 = "Pot-Catacombs_Room_2"
    POT_CEMETERY_RIGHT_ARENA = "Pot-Cemetery_Right_Arena"
    POT_BOMB_SILENT_SERVANT = "Pot-Bomb_Silent_Servant"
    POT_CEMETERY_SUMMIT = "Pot-Cemetery_Summit"
    POT_CEMETERY_CENTRAL_ARENA = "Pot-Cemetery_Central_Arena"
    POT_FIRE_SILENT_SERVANT = "Pot-Fire_Silent_Servant"
    POT_ESTATE_DOOR = "Pot-Estate_Door"
    POT_GARDEN_OF_JOY = "Pot-Garden_of_Joy"
    POT_GARDEN_OF_PEACE = "Pot-Garden_of_Peace"
    POT_GARDEN_OF_LOVE_ENTRANCE = "Pot-Garden_of_Love_Entrance"
    POT_GARDEN_OF_LOVE_HIDDEN_LEFT = "Pot-Garden_of_Love_Hidden_Left"
    POT_GARDEN_OF_LOVE_HIDDEN_RIGHT = "Pot-Garden_of_Love_Hidden_Right"
    POT_GARDEN_OF_LIFE = "Pot-Garden_of_Life"
    POT_MANOR_LOBBY = "Pot-Manor_Lobby"
    POT_MANOR_RAFTERS = "Pot-Manor_Rafters"
    POT_MANOR_IMP_LOFT = "Pot-Manor_Imp_Loft"
    POT_MANOR_POST_DINING = "Pot-Manor_Post_Dining"
    POT_MANOR_LIBRARY = "Pot-Manor_Library"
    POT_MANOR_BEDROOM = "Pot-Manor_Bedroom"
    POT_INNER_FURNACE_BURNER_2 = "Pot-Inner_Furnace_Burner_2"
    POT_INNER_FURNACE_BURNER_3 = "Pot-Inner_Furnace_Burner_3"
    POT_INNER_FURNACE_ISLANDS = "Pot-Inner_Furnace_Islands"
    POT_INNER_FURNACE_BURNER_8 = "Pot-Inner_Furnace_Burner_8"
    POT_INNER_FURNACE_FINAL = "Pot-Inner_Furnace_Final"
    POT_HOOKSHOT_SILENT_SERVANT = "Pot-Hookshot_Silent_Servant"
    POT_LOCKSTONE_WEST_CROW = "Pot-Lockstone_West_Crow"
    POT_LOCKSTONE_WEST_KEYED_CROW = "Pot-Lockstone_West_Keyed_Crow"
    POT_LOCKSTONE_ENTRANCE = "Pot-Lockstone_Entrance"
    POT_LOCKSTONE_EAST_CROW = "Pot-Lockstone_East_Crow"
    POT_CAMP_CASTLE_DOOR = "Pot-Camp_Castle_Door"
    POT_WATCHTOWERS_FIRST = "Pot-Watchtowers_First"
    POT_WATCHTOWERS_BARB_ELEVATOR = "Pot-Watchtowers_Barb_Elevator"
    POT_WATCHTOWERS_LASERS_ARENA = "Pot-Watchtowers_Lasers_Arena"
    POT_WATCHTOWERS_OWL = "Pot-Watchtowers_Owl"
    POT_WATCHTOWERS_CAVE_ENTRANCE = "Pot-Watchtowers_Cave_Entrance"
    POT_RUINS_KEY = "Pot-Ruins_Key"
    POT_RUINS_FIRE_PLANT_CORRIDOR = "Pot-Ruins_Fire_Plant_Corridor"
    POT_RUINS_RIGHT_ARENA = "Pot-Ruins_Right_Arena"
    POT_RUINS_SEWER = "Pot-Ruins_Sewer"
    POT_RUINS_LEFT_OF_LORD_OF_DOORS_ARENA = "Pot-Ruins_Left_of_Lord_of_Doors_Arena"
    POT_DUNGEON_COBWEB_ROOM = "Pot-Dungeon_Cobweb_Room"
    POT_DUNGEON_WATER_ARENA = "Pot-Dungeon_Water_Arena"
    POT_DUNGEON_HALL = "Pot-Dungeon_Hall"
    POT_DUNGEON_RIGHTMOST_CROW = "Pot-Dungeon_Rightmost_Crow"
    POT_FORTRESS_MAIN_GATE = "Pot-Fortress_Main_Gate"
    POT_FORTRESS_U_TURN = "Pot-Fortress_U_Turn"
    POT_FORTRESS_BREAKABLE_BRIDGES = "Pot-Fortress_Breakable_Bridges"
    POT_FORTRESS_BRIDGE = "Pot-Fortress_Bridge"
    POT_FORTRESS_EXIT = "Pot-Fortress_Exit"


class DeathsDoorEventLocationData(NamedTuple):
    name: DeathsDoorEventLocationName
    region: R
    event_name: DeathsDoorEventName


event_location_table: List[DeathsDoorEventLocationData] = [
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.VICTORY, R.HALL_OF_DOORS_LOBBY, DeathsDoorEventName.VICTORY
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.LOST_CEMETERY_OPENED_EXIT_TO_SAILOR,
        R.LOST_CEMETERY_STEADHONE,
        DeathsDoorEventName.LOST_CEMETERY_OPENED_EXIT_TO_SAILOR,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.ACCESS_TO_NIGHT,
        R.LOST_CEMETERY_BELLTOWER,
        DeathsDoorEventName.ACCESS_TO_NIGHT,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.ACCESS_TO_DAY,
        R.LOST_CEMETERY_BELLTOWER,
        DeathsDoorEventName.ACCESS_TO_DAY,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.GREY_CROW_BOSS,
        R.LOST_CEMETERY_SUMMIT,
        DeathsDoorEventName.GREY_CROW_BOSS,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.ACTIVATED_FURNACE_BURNERS,
        R.INNER_FURNACE_ENTRANCE,
        DeathsDoorEventName.ACTIVATED_FURNACE_BURNERS,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.WATCHTOWER_ENTRANCE_TORCH,
        R.OLD_WATCHTOWERS_ENTRANCE,
        DeathsDoorEventName.LIT_WATCHTOWER_TORCH,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.WATCHTOWER_JAMMING_START_TORCH,
        R.OLD_WATCHTOWERS_JAMMING_START,
        DeathsDoorEventName.LIT_WATCHTOWER_TORCH,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.WATCHTOWER_BOXES_TORCH,
        R.OLD_WATCHTOWERS_JAMMING_START,
        DeathsDoorEventName.LIT_WATCHTOWER_TORCH,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.WATCHTOWER_FIRST_POT_TORCH,
        R.OLD_WATCHTOWERS_FIRST_POT_AREA,
        DeathsDoorEventName.LIT_WATCHTOWER_TORCH,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.WATCHTOWER_BOOMERS_TORCH_1,
        R.OLD_WATCHTOWERS_BOOMERS,
        DeathsDoorEventName.LIT_WATCHTOWER_TORCH,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.WATCHTOWER_BOOMERS_TORCH_2,
        R.OLD_WATCHTOWERS_BOOMERS,
        DeathsDoorEventName.LIT_WATCHTOWER_TORCH,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.MUSHROOM_DUNGEON_MAIN_GATE,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        DeathsDoorEventName.MUSHROOM_DUNGEON_MAIN_GATE,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.RESCUE_GRUNT,
        R.MUSHROOM_DUNGEON_LOBBY,
        DeathsDoorEventName.RESCUE_GRUNT,
    ),
]

pot_table: List[DeathsDoorEventLocationData] = [
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_OUTSIDE_CATACOMBS_EXIT,
        R.LOST_CEMETERY_CENTRAL,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_CATACOMBS_ROOM_2,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_CEMETERY_RIGHT_ARENA,
        R.LOST_CEMETERY_RIGHT_ARENA,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_BOMB_SILENT_SERVANT,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_CEMETERY_SUMMIT,
        R.LOST_CEMETERY_SUMMIT,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_CEMETERY_CENTRAL_ARENA,
        R.LOST_CEMETERY_STEADHONE,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_FIRE_SILENT_SERVANT,
        R.CRYPT_MAIN_ROOM,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_ESTATE_DOOR,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_GARDEN_OF_JOY,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_GARDEN_OF_PEACE,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_GARDEN_OF_LOVE_ENTRANCE,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_GARDEN_OF_LOVE_HIDDEN_LEFT,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_GARDEN_OF_LOVE_HIDDEN_RIGHT,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_GARDEN_OF_LIFE,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_MANOR_LOBBY,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_MANOR_RAFTERS,
        R.CERAMIC_MANOR_LEFT,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_MANOR_IMP_LOFT,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_MANOR_POST_DINING,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_MANOR_LIBRARY,
        R.CERAMIC_MANOR_LIBRARY,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_MANOR_BEDROOM,
        R.CERAMIC_MANOR_LEFT,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_INNER_FURNACE_BURNER_2,
        R.INNER_FURNACE_POST_BURNER_2,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_INNER_FURNACE_BURNER_3,
        R.INNER_FURNACE_POST_BURNER_3,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_INNER_FURNACE_ISLANDS,
        R.INNER_FURNACE_POST_BURNER_6,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_INNER_FURNACE_BURNER_8,
        R.INNER_FURNACE_POST_BURNER_8,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_INNER_FURNACE_FINAL,
        R.INNER_FURNACE_POST_BURNER_9,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_HOOKSHOT_SILENT_SERVANT,
        R.STRANDED_SAILOR_CAVES,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_LOCKSTONE_WEST_CROW,
        R.CASTLE_LOCKSTONE_CENTRAL,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_LOCKSTONE_WEST_KEYED_CROW,
        R.CASTLE_LOCKSTONE_CENTRAL,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_LOCKSTONE_ENTRANCE,
        R.CASTLE_LOCKSTONE_CENTRAL,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_LOCKSTONE_EAST_CROW,
        R.CASTLE_LOCKSTONE_EAST_CROW,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_CAMP_CASTLE_DOOR,
        R.CAMP_OF_THE_FREE_CROWS_CASTLE_DOOR,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_WATCHTOWERS_FIRST,
        R.OLD_WATCHTOWERS_FIRST_POT_AREA,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_WATCHTOWERS_BARB_ELEVATOR,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_WATCHTOWERS_LASERS_ARENA,
        R.OLD_WATCHTOWERS_LASERS_ARENA,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_WATCHTOWERS_OWL,
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_WATCHTOWERS_CAVE_ENTRANCE,
        R.OLD_WATCHTOWERS_CAVE_ENTRANCE,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_RUINS_KEY,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_RUINS_FIRE_PLANT_CORRIDOR,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_RUINS_RIGHT_ARENA,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_RUINS_SEWER,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_RUINS_LEFT_OF_LORD_OF_DOORS_ARENA,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_DUNGEON_COBWEB_ROOM,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_DUNGEON_WATER_ARENA,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_DUNGEON_HALL,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_DUNGEON_RIGHTMOST_CROW,
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_FORTRESS_MAIN_GATE,
        R.FLOODED_FORTRESS_INSIDE_MAIN_GATE,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_FORTRESS_U_TURN,
        R.FLOODED_FORTRESS_U_TURN,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_FORTRESS_BREAKABLE_BRIDGES,
        R.FLOODED_FORTRESS_BREAKABLE_BRIDGES,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_FORTRESS_BRIDGE,
        R.FLOODED_FORTRESS_BRIDGE,
        DeathsDoorEventName.PLANTED_SEED,
    ),
    DeathsDoorEventLocationData(
        DeathsDoorEventLocationName.POT_FORTRESS_EXIT,
        R.FLOODED_FORTRESS_EXIT,
        DeathsDoorEventName.PLANTED_SEED,
    ),
]

event_location_table = event_location_table + pot_table
