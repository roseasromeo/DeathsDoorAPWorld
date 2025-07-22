from enum import Enum
from typing import TYPE_CHECKING, List, NamedTuple
from .regions import DeathsDoorRegionName as R
from .rules import Has, HasAll, can_complete_game
from .items import DeathsDoorItemName as I
from .options import StartDayOrNight

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


class DeathsDoorEventName(str, Enum):
    VICTORY = "Goal Complete"
    LOST_CEMETERY_OPENED_EXIT_TO_SAILOR = "Lost Cemetery Opened Exit to Sailor"
    ACCESS_TO_NIGHT = "Access to Night"
    ACCESS_TO_DAY = "Access to Day"
    GREY_CROW_BOSS = "Can Defeat Grey Crow Boss"
    ACTIVATED_FURNACE_BURNERS = "Activated First Furnace Burner"
    PLANTED_SEED = "Can Plant a Seed"
    OOL = "Out of Logic Item"  # For Universal Tracker


class DeathsDoorEventLocationName(str, Enum):
    VICTORY = "Defeat the Lord of Doors"
    LOST_CEMETERY_OPENED_EXIT_TO_SAILOR = "Lost Cemetery Lamp Switch Exit to Sailor"
    ACCESS_TO_NIGHT = "Access to Night"
    ACCESS_TO_DAY = "Access to Day"
    GREY_CROW_BOSS = "Grey Crow Boss"
    ACTIVATED_FURNACE_BURNERS = "First Furnace Burner"
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
        DeathsDoorEventLocationName.VICTORY, R.GOAL, DeathsDoorEventName.VICTORY
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
]

pot_table: List[DeathsDoorEventLocationData] = [
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_OUTSIDE_CATACOMBS_EXIT, R.LOST_CEMETERY_CENTRAL, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_CATACOMBS_ROOM_2, R.LOST_CEMETERY_CATACOMBS_ROOM_1, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_CEMETERY_RIGHT_ARENA, R.LOST_CEMETERY_RIGHT_ARENA, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_BOMB_SILENT_SERVANT, R.LOST_CEMETERY_EAST_TREE_BRIDGE, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_CEMETERY_SUMMIT, R.LOST_CEMETERY_SUMMIT, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_CEMETERY_CENTRAL_ARENA, R.LOST_CEMETERY_STEADHONE, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_FIRE_SILENT_SERVANT, R.CRYPT_MAIN_ROOM, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_ESTATE_DOOR, R.ESTATE_OF_THE_URN_WITCH_SOUTH, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_GARDEN_OF_JOY, R.ESTATE_OF_THE_URN_WITCH_SOUTH, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_GARDEN_OF_PEACE, R.ESTATE_OF_THE_URN_WITCH_SOUTH, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_GARDEN_OF_LOVE_ENTRANCE, R.ESTATE_OF_THE_URN_WITCH_NORTH, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_GARDEN_OF_LOVE_HIDDEN_LEFT, R.ESTATE_OF_THE_URN_WITCH_NORTH, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_GARDEN_OF_LOVE_HIDDEN_RIGHT, R.ESTATE_OF_THE_URN_WITCH_NORTH, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_GARDEN_OF_LIFE, R.ESTATE_OF_THE_URN_WITCH_NORTH, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_MANOR_LOBBY, R.CERAMIC_MANOR_MAIN_LOBBY, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_MANOR_RAFTERS, R.CERAMIC_MANOR_LEFT, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_MANOR_IMP_LOFT, R.CERAMIC_MANOR_MAIN_LOBBY, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_MANOR_POST_DINING, R.CERAMIC_MANOR_MAIN_LOBBY, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_MANOR_LIBRARY, R.CERAMIC_MANOR_LIBRARY, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_MANOR_BEDROOM, R.CERAMIC_MANOR_LEFT, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_INNER_FURNACE_BURNER_2, R.INNER_FURNACE_POST_BURNER_2, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_INNER_FURNACE_BURNER_3, R.INNER_FURNACE_POST_BURNER_3, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_INNER_FURNACE_ISLANDS, R.INNER_FURNACE_POST_BURNER_6, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_INNER_FURNACE_BURNER_8, R.INNER_FURNACE_POST_BURNER_8, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_INNER_FURNACE_FINAL, R.INNER_FURNACE_POST_BURNER_9, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_HOOKSHOT_SILENT_SERVANT, R.STRANDED_SAILOR_CAVES, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_LOCKSTONE_WEST_CROW, R.CASTLE_LOCKSTONE_CENTRAL, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_LOCKSTONE_WEST_KEYED_CROW, R.CASTLE_LOCKSTONE_CENTRAL, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_LOCKSTONE_ENTRANCE, R.CASTLE_LOCKSTONE_CENTRAL, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_LOCKSTONE_EAST_CROW, R.CASTLE_LOCKSTONE_EAST_CROW, DeathsDoorEventName.PLANTED_SEED),
    DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_CAMP_CASTLE_DOOR, R.CAMP_OF_THE_FREE_CROWS_CASTLE_DOOR, DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_WATCHTOWERS_FIRST, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_WATCHTOWERS_BARB_ELEVATOR, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_WATCHTOWERS_LASERS_ARENA, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_WATCHTOWERS_OWL, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_WATCHTOWERS_CAVE_ENTRANCE, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_RUINS_KEY, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_RUINS_FIRE_PLANT_CORRIDOR, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_RUINS_RIGHT_ARENA, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_RUINS_SEWER, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_RUINS_LEFT_OF_LORD_OF_DOORS_ARENA, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_DUNGEON_COBWEB_ROOM, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_DUNGEON_WATER_ARENA, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_DUNGEON_HALL, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_DUNGEON_RIGHTMOST_CROW, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_FORTRESS_MAIN_GATE, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_FORTRESS_U_TURN, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_FORTRESS_BREAKABLE_BRIDGES, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_FORTRESS_BRIDGE, R., DeathsDoorEventName.PLANTED_SEED),
    # DeathsDoorEventLocationData(DeathsDoorEventLocationName.POT_FORTRESS_EXIT, R., DeathsDoorEventName.PLANTED_SEED),
]

pot_specific_rules = dict[
    DeathsDoorEventLocationName, Rule["DeathsDoorWorld"]] = {
        DeathsDoorEventLocationName.POT_CATACOMBS_ROOM_2 : Has(I.FIRE),
        DeathsDoorEventLocationName.POT_BOMB_SILENT_SERVANT : Has(I.BOMB),
        DeathsDoorEventLocationName.POT_MANOR_IMP_LOFT : Has(I.FIRE), ##TODO: Check?
        DeathsDoorEventLocationName.POT_HOOKSHOT_SILENT_SERVANT : Has(I.LEVER_HOOKSHOT_SILENT_SERVANT),
        DeathsDoorEventLocationName.POT_LOCKSTONE_WEST_KEYED_CROW : Has(I.PINK_KEY, 5),
        DeathsDoorEventLocationName.POT_FORTRESS_MAIN_GATE : Has(I.BOMB),
    }



deaths_door_event_rules: dict[
    DeathsDoorEventLocationName, Rule["DeathsDoorWorld"] | None
] = {
    DeathsDoorEventLocationName.VICTORY: can_complete_game,
    DeathsDoorEventLocationName.LOST_CEMETERY_OPENED_EXIT_TO_SAILOR: Has(I.FIRE),
    DeathsDoorEventLocationName.ACCESS_TO_NIGHT: True_(
        options=[OptionFilter(StartDayOrNight, 1)]
    )
    | Has(I.RUSTY_BELLTOWER_KEY),
    DeathsDoorEventLocationName.ACCESS_TO_DAY: True_(
        options=[OptionFilter(StartDayOrNight, 0)]
    )
    | Has(I.RUSTY_BELLTOWER_KEY),
    DeathsDoorEventLocationName.GREY_CROW_BOSS: HasAll(
        [
            I.GIANT_SOUL_OF_BETTY,
            I.GIANT_SOUL_OF_THE_FROG_KING,
            I.GIANT_SOUL_OF_THE_URN_WITCH,
        ]
    ),
    DeathsDoorEventLocationName.ACTIVATED_FURNACE_BURNERS: Has(I.FIRE),
}

# Add in pots to existing tables to be able to use the same infrastructure
event_location_table = event_location_table + pot_table
for pot in pot_table:
    rule = Has(I.LIFE_SEED, 50) ## TODO: Make a yaml setting
    if pot.name in pot_specific_rules.keys:
        rule = rule & pot_specific_rules[pot.name]
    deaths_door_event_rules[pot.name] = rule


def set_event_rules(world: "DeathsDoorWorld") -> None:
    multiworld = world.multiworld
    player = world.player

    for event_location_data in event_location_table:
        rule = deaths_door_event_rules[event_location_data.name]
        if rule is not None:
            event_location = multiworld.get_location(
                event_location_data.name.value, player
            )
            world.set_rule(event_location, rule)
        
