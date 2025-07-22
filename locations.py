from enum import Enum, auto
from typing import Dict, NamedTuple, Set, List

from .regions import DeathsDoorRegionName as R


class LocationGroup(Enum):
    Spell = "Spell"
    Weapon = "Weapon"
    Giant_Soul = "Giant Soul"
    Shrine = "Shrine"
    Shiny_Thing = "Shiny Thing"
    Seed = "Seed"
    Soul_Orb = "Soul Orb"
    Tablet = "Tablet"
    Lever = "Lever"
    Door = "Door"
    Key = "Key"
    Lost_Crow = "Lost Crow"

class DeathsDoorLocationName(str, Enum):
    # Spells and their upgrades
    Fire_Avarice = "Fire Avarice"
    Bomb_Avarice = "Bomb Avarice"
    Hookshot_Avarice = "Hookshot Avarice"
    Fire_Silent_Servant = "Fire Silent Servant"
    Bomb_Silent_Servant = "Bomb Silent Servant"
    Hookshot_Silent_Servant = "Hookshot Silent Servant"
    Arrow_Silent_Servant = "Arrow Silent Servant"

    # Weapons
    Rogue_Daggers = "Rogue Daggers"
    Discarded_Umbrella = "Discarded Umbrella"
    Reapers_Greatsword = "Reaper's Greatsword"
    Thunder_Hammer = "Thunder Hammer"

    # Giant Souls
    Betty = "Betty"
    Frog_King = "Frog King"
    Grandma = "Grandma"

    # Shrines
    Heart_Shrine_Cemetery_Behind_Entrance = "Heart Shrine-Cemetery Behind Entrance"
    Magic_Shrine_Cemetery_After_Smough_Arena = (
        "Magic Shrine-Cemetery After Smough Arena"
    )
    Heart_Shrine_Cemetery_Winding_Bridge_End = (
        "Heart Shrine-Cemetery Winding Bridge End"
    )
    Heart_Shrine_Hookshot_Arena = "Heart Shrine-Hookshot Arena"
    Magic_Shrine_Sailor_Turncam = "Magic Shrine-Sailor Turncam"
    Magic_Shrine_Lockstone_Secret_West = "Magic Shrine-Lockstone Secret West"
    Heart_Shrine_Camp_Ice_Skating = "Heart Shrine-Camp Ice Skating"
    Magic_Shrine_Ruins_Hookshot_Arena = "Magic Shrine-Ruins Hookshot Arena"
    Magic_Shrine_Ruins_Turncam = "Magic Shrine-Ruins Turncam"
    Heart_Shrine_Dungeon_Water_Arena = "Heart Shrine-Dungeon Water Arena"
    Heart_Shrine_Ruins_Sewer = "Heart Shrine-Ruins Sewer"
    Magic_Shrine_Fortress_Bow_Secret = "Magic Shrine-Fortress Bow Secret"
    Magic_Shrine_Estate_Left_of_Manor = "Magic Shrine-Estate Left of Manor"
    Heart_Shrine_Garden_of_Life = "Heart Shrine-Garden of Life"
    Magic_Shrine_Manor_Bathroom_Puzzle = "Magic Shrine-Manor Bathroom Puzzle"
    Heart_Shrine_Furnace_Cart_Puzzle = "Heart Shrine-Furnace Cart Puzzle"

    # Shiny Things
    Engagement_Ring = "Engagement Ring"
    Old_Compass = "Old Compass"
    Incense = "Incense"
    Undying_Blossom = "Undying Blossom"
    Old_Photograph = "Old Photograph"
    Sludge_Filled_Urn = "Sludge-Filled Urn"
    Token_of_Death = "Token of Death"
    Rusty_Garden_Trowel = "Rusty Garden Trowel"
    Captains_Log = "Captain's Log"
    Giant_Arrowhead = "Giant Arrowhead"
    Malformed_Seed = "Malformed Seed"
    Corrupted_Antler = "Corrupted Antler"
    Magical_Forest_Horn = "Magical Forest Horn"
    Ancient_Crown = "Ancient Crown"
    Grunts_Old_Mask = "Grunt's Old Mask"
    Ancient_Door_Scale_Model = "Ancient Door Scale Model"
    Modern_Door_Scale_Model = "Modern Door Scale Model"
    Rusty_Belltower_Key = "Rusty Belltower Key"
    Surveillance_Device = "Surveillance Device"
    Shiny_Medallion = "Shiny Medallion"
    Ink_Covered_Teddy_Bear = "Ink-Covered Teddy Bear"
    Deaths_Contract = "Death's Contract"
    Makeshift_Soul_Key = "Makeshift Soul Key"
    Mysterious_Locket = "Mysterious Locket"

    # Seeds
    Seed_Cemetery_Broken_Bridge = "Seed-Cemetery Broken Bridge"
    Seed_Catacombs_Tower = "Seed-Catacombs Tower"
    Seed_Cemetery_Left_of_Main_Entrance = "Seed-Cemetery Left of Main Entrance"
    Seed_Cemetery_Near_Tablet_Gate = "Seed-Cemetery Near Tablet Gate"
    Seed_Between_Cemetery_and_Sailor = "Seed-Between Cemetery and Sailor"
    Seed_Sailor_Upper = "Seed-Sailor Upper"
    Seed_Lockstone_Upper_East = "Seed-Lockstone Upper East"
    Seed_Lockstone_Soul_Door = "Seed-Lockstone Soul Door"
    Seed_Lockstone_Behind_Bars = "Seed-Lockstone Behind Bars"
    Seed_Lockstone_Entrance_West = "Seed-Lockstone Entrance West"
    Seed_Lockstone_North = "Seed-Lockstone North"
    Seed_Camp_Ledge_With_Huts = "Seed-Camp Ledge With Huts"
    Seed_Camp_Stall = "Seed-Camp Stall"
    Seed_Camp_Rooftops = "Seed-Camp Rooftops"
    Seed_Watchtowers_Ice_Skating = "Seed-Watchtowers Ice Skating"
    Seed_Watchtowers_Tablet_Door = "Seed-Watchtowers Tablet Door"
    Seed_Watchtowers_Archer_Platform = "Seed-Watchtowers Archer Platform"
    Seed_Watchtowers_Boxes = "Seed-Watchtowers Boxes"
    Seed_Dungeon_Fire_Puzzle_Near_Water_Arena = (
        "Seed-Dungeon Fire Puzzle Near Water Arena"
    )
    Seed_Ruins_Lord_of_Doors_Arena = "Seed-Ruins Lord of Doors Arena"
    Seed_Ruins_Fire_Plant_Corridor = "Seed-Ruins Fire Plant Corridor"
    Seed_Dungeon_Water_Arena_Left_Exit = "Seed-Dungeon Water Arena Left Exit"
    Seed_Ruins_Right_Middle = "Seed-Ruins Right Middle"
    Seed_Ruins_On_Settlement_Wall = "Seed-Ruins On Settlement Wall"
    Seed_Ruins_Behind_Boxes = "Seed-Ruins Behind Boxes"
    Seed_Ruins_Down_Through_Bomb_Wall = "Seed-Ruins Down Through Bomb Wall"
    Seed_Dungeon_Above_Rightmost_Crow = "Seed-Dungeon Above Rightmost Crow"
    Seed_Dungeon_Right_Above_Key = "Seed-Dungeon Right Above Key"
    Seed_Dungeon_Avarice_Bridge = "Seed-Dungeon Avarice Bridge"
    Seed_Fortress_Watchtower = "Seed-Fortress Watchtower"
    Seed_Fortress_Statue = "Seed-Fortress Statue"
    Seed_Fortress_Bridge = "Seed-Fortress Bridge"
    Seed_Fortress_Intro_Crate = "Seed-Fortress Intro Crate"
    Seed_Fortress_East_After_Statue = "Seed-Fortress East After Statue"
    Seed_Estate_Family_Tomb = "Seed-Estate Family Tomb"
    Seed_Estate_Entrance = "Seed-Estate Entrance"
    Seed_Estate_Hedge_Gaps = "Seed-Estate Hedge Gaps"
    Seed_Garden_of_Joy = "Seed-Garden of Joy"
    Seed_Manor_Boxes = "Seed-Manor Boxes"
    Seed_Manor_Near_Brazier = "Seed-Manor Near Brazier"
    Seed_Manor_Below_Big_Pot_Arena = "Seed-Manor Below Big Pot Arena"
    Seed_Manor_Rafters = "Seed-Manor Rafters"
    Seed_Manor_Main_Room_Upper = "Seed-Manor Main Room Upper"
    Seed_Manor_Spinny_Pot_Room = "Seed-Manor Spinny Pot Room"
    Seed_Manor_Library_Shelf = "Seed-Manor Library Shelf"
    Seed_Cart_Puzzle = "Seed-Cart Puzzle"
    Seed_Furnace_Entrance = "Seed-Furnace Entrance"
    Seed_Inner_Furnace_Horizontal_Pistons = "Seed-Inner Furnace Horizontal Pistons"
    Seed_Inner_Furnace_Conveyor_Bridge = "Seed-Inner Furnace Conveyor Bridge"
    Seed_Inner_Furnace_Conveyor_Gauntlet = "Seed-Inner Furnace Conveyor Gauntlet"

    # Soul Orbs
    Soul_Orb_Fire_Return_Upper = "Soul Orb-Fire Return Upper"
    Soul_Orb_Hookshot_Secret = "Soul Orb-Hookshot Secret"
    Soul_Orb_Bomb_Return = "Soul Orb-Bomb Return"
    Soul_Orb_Bomb_Secret = "Soul Orb-Bomb Secret"
    Soul_Orb_Hookshot_Return = "Soul Orb-Hookshot Return"
    Soul_Orb_Fire_Return_Lower = "Soul Orb-Fire Return Lower"
    Soul_Orb_Fire_Secret = "Soul Orb-Fire Secret"
    Soul_Orb_Catacombs_Exit = "Soul Orb-Catacombs Exit"
    Soul_Orb_Cemetery_Hookshot_Towers = "Soul Orb-Cemetery Hookshot Towers"
    Soul_Orb_Cemetery_Under_Bridge = "Soul Orb-Cemetery Under Bridge"
    Soul_Orb_Cemetery_East_Tree = "Soul Orb-Cemetery East Tree"
    Soul_Orb_Cemetery_Winding_Bridge_End = "Soul Orb-Cemetery Winding Bridge End"
    Soul_Orb_Catacombs_Room_2 = "Soul Orb-Catacombs Room 2"
    Soul_Orb_Catacombs_Room_1 = "Soul Orb-Catacombs Room 1"
    Soul_Orb_Cemetery_Gated_Sewer = "Soul Orb-Cemetery Gated Sewer"
    Soul_Orb_Catacombs_Entrance = "Soul Orb-Catacombs Entrance"
    Soul_Orb_Cemetery_Cave = "Soul Orb-Cemetery Cave"
    Soul_Orb_Sailor_Turncam = "Soul Orb-Sailor Turncam"
    Soul_Orb_North_Lockstone_Sewer = "Soul Orb-North Lockstone Sewer"
    Soul_Orb_Lockstone_Hookshot_North = "Soul Orb-Lockstone Hookshot North"
    Soul_Orb_Lockstone_Exit = "Soul Orb-Lockstone Exit"
    Soul_Orb_West_Lockstone_Sewer = "Soul Orb-West Lockstone Sewer"
    Soul_Orb_Camp_Rooftops = "Soul Orb-Camp Rooftops"
    Soul_Orb_Camp_Broken_Bridge = "Soul Orb-Camp Broken Bridge"
    Soul_Orb_Watchtowers_Behind_Barb_Elevator = (
        "Soul Orb-Watchtowers Behind Barb Elevator"
    )
    Soul_Orb_Dungeon_Vine = "Soul Orb-Dungeon Vine"
    Soul_Orb_Ruins_Stump = "Soul Orb-Ruins Stump"
    Soul_Orb_Ruins_Outside_Left_Dungeon_Exit = (
        "Soul Orb-Ruins Outside Left Dungeon Exit"
    )
    Soul_Orb_Dungeon_Cobweb = "Soul Orb-Dungeon Cobweb"
    Soul_Orb_Ruins_Left_After_Key_Door = "Soul Orb-Ruins Left After Key Door"
    Soul_Orb_Ruins_Lower_Bomb_Wall = "Soul Orb-Ruins Lower Bomb Wall"
    Soul_Orb_Ruins_Lord_of_Doors_Arena_Hookshot = (
        "Soul Orb-Ruins Lord of Doors Arena Hookshot"
    )
    Soul_Orb_Dungeon_Lower_Entrance = "Soul Orb-Dungeon Lower Entrance"
    Soul_Orb_Ruins_Upper_Above_Horn = "Soul Orb-Ruins Upper Above Horn"
    Soul_Orb_Ruins_Above_Three_Plants = "Soul Orb-Ruins Above Three Plants"
    Soul_Orb_Ruins_Up_Turncam_Ladder = "Soul Orb-Ruins Up Turncam Ladder"
    Soul_Orb_Ruins_Above_Entrance_Gate = "Soul Orb-Ruins Above Entrance Gate"
    Soul_Orb_Ruins_Upper_Bomb_Wall = "Soul Orb-Ruins Upper Bomb Wall"
    Soul_Orb_Dungeon_Left_Exit_Shelf = "Soul Orb-Dungeon Left Exit Shelf"
    Soul_Orb_Ruins_Lower_Hookshot = "Soul Orb-Ruins Lower Hookshot"
    Soul_Orb_Fortress_Bomb = "Soul Orb-Fortress Bomb"
    Soul_Orb_Fortress_Hidden_Sewer = "Soul Orb-Fortress Hidden Sewer"
    Soul_Orb_Fortress_Drop = "Soul Orb-Fortress Drop"
    Soul_Orb_Estate_Access_Crypt = "Soul Orb-Estate Access Crypt"
    Soul_Orb_Estate_Balcony = "Soul Orb-Estate Balcony"
    Soul_Orb_Garden_of_Love_Turncam = "Soul Orb-Garden of Love Turncam"
    Soul_Orb_Garden_of_Life_Hookshot_Loop = "Soul Orb-Garden of Life Hookshot Loop"
    Soul_Orb_Garden_of_Love_Bomb_Walls = "Soul Orb-Garden of Love Bomb Walls"
    Soul_Orb_Garden_of_Life_Bomb_Wall = "Soul Orb-Garden of Life Bomb Wall"
    Soul_Orb_Estate_Broken_Boardwalk = "Soul Orb-Estate Broken Boardwalk"
    Soul_Orb_Estate_Secret_Cave = "Soul Orb-Estate Secret Cave"
    Soul_Orb_Estate_Twin_Benches = "Soul Orb-Estate Twin Benches"
    Soul_Orb_Estate_Sewer_Middle = "Soul Orb-Estate Sewer Middle"
    Soul_Orb_Estate_Sewer_End = "Soul Orb-Estate Sewer End"
    Soul_Orb_Garden_of_Peace = "Soul Orb-Garden of Peace"
    Soul_Orb_Manor_Imp_Loft = "Soul Orb-Manor Imp Loft"
    Soul_Orb_Manor_Library_Shelf = "Soul Orb-Manor Library Shelf"
    Soul_Orb_Manor_Chandelier = "Soul Orb-Manor Chandelier"
    Soul_Orb_Furnace_Lantern_Chain = "Soul Orb-Furnace Lantern Chain"
    Soul_Orb_Small_Room = "Soul Orb-Small Room"
    Soul_Orb_Furnace_Entrance_Sewer = "Soul Orb-Furnace Entrance Sewer"

    # Tablets
    Red_Ancient_Tablet_of_Knowledge = "Red Ancient Tablet of Knowledge"
    Yellow_Ancient_Tablet_of_Knowledge = "Yellow Ancient Tablet of Knowledge"
    Green_Ancient_Tablet_of_Knowledge = "Green Ancient Tablet of Knowledge"
    Cyan_Ancient_Tablet_of_Knowledge = "Cyan Ancient Tablet of Knowledge"
    Blue_Ancient_Tablet_of_Knowledge = "Blue Ancient Tablet of Knowledge"
    Purple_Ancient_Tablet_of_Knowledge = "Purple Ancient Tablet of Knowledge"
    Estate_Owl = "Estate Owl"
    Ruins_Owl = "Ruins Owl"
    Watchtowers_Owl = "Watchtowers Owl"

    # Levers
    Lever_Bomb_Exit = "Lever-Bomb Exit"
    Lever_Cemetery_Sewer = "Lever-Cemetery Sewer"
    Lever_Guardian_of_the_Door_Access = "Lever-Guardian of the Door Access"
    Lever_Cemetery_Shortcut_to_East_Tree = "Lever-Cemetery Shortcut to East Tree"
    Lever_Cemetery_East_Tree = "Lever-Cemetery East Tree"
    Lever_Catacombs_Tower = "Lever-Catacombs Tower"
    Lever_Cemetery_Exit_to_Estate = "Lever-Cemetery Exit to Estate"
    Lever_Catacombs_Exit = "Lever-Catacombs Exit"
    Lever_Hookshot_Silent_Servant = "Lever-Hookshot Silent Servant"
    Lever_Sailor_Turncam_Upper = "Lever-Sailor Turncam Upper"
    Lever_Sailor_Turncam_Lower = "Lever-Sailor Turncam Lower"
    Lever_Sailor_Greatsword_Gate = "Lever-Sailor Greatsword Gate"
    Lever_Lockstone_East_Start_Shortcut = "Lever-Lockstone East Start Shortcut"
    Lever_Lockstone_Entrance = "Lever-Lockstone Entrance"
    Lever_Lockstone_East_Lower = "Lever-Lockstone East Lower"
    Lever_Lockstone_Upper_Shortcut = "Lever-Lockstone Upper Shortcut"
    Lever_Lockstone_Dual_Laser_Puzzle = "Lever-Lockstone Dual Laser Puzzle"
    Lever_Lockstone_Tracking_Beam_Puzzle = "Lever-Lockstone Tracking Beam Puzzle"
    Lever_Lockstone_Vertical_Laser_Puzzle = "Lever-Lockstone Vertical Laser Puzzle"
    Lever_Lockstone_North_Puzzle = "Lever-Lockstone North Puzzle"
    Lever_Lockstone_Shrine = "Lever-Lockstone Shrine"
    Lever_Lockstone_Hookshot_Puzzle = "Lever-Lockstone Hookshot Puzzle"
    Lever_Lockstone_Upper_Puzzle = "Lever-Lockstone Upper Puzzle"
    Lever_Lockstone_Upper_Dual_Laser_Puzzle = "Lever-Lockstone Upper Dual Laser Puzzle"
    Lever_Watchtowers_Before_Ice_Arena = "Lever-Watchtowers Before Ice Arena"
    Lever_Watchtowers_After_Ice_Skating = "Lever-Watchtowers After Ice Skating"
    Lever_Watchtowers_After_Boomers = "Lever-Watchtowers After Boomers"
    Lever_Ruins_Settlement_Gate = "Lever-Ruins Settlement Gate"
    Lever_Ruins_Upper_Dungeon_Entrance = "Lever-Ruins Upper Dungeon Entrance"
    Lever_Ruins_Ladder_Left_of_Lord_of_Doors_Arena = (
        "Lever-Ruins Ladder Left of Lord of Doors Arena"
    )
    Lever_Ruins_Entrance_Ladder_Shortcut = "Lever-Ruins Entrance Ladder Shortcut"
    Lever_Ruins_Main_Gate = "Lever-Ruins Main Gate"
    Lever_Dungeon_Entrance_Right_Gate = "Lever-Dungeon Entrance Right Gate"
    Lever_Dungeon_Entrance_Left_Gate = "Lever-Dungeon Entrance Left Gate"
    Lever_Dungeon_Above_Rightmost_Crow = "Lever-Dungeon Above Rightmost Crow"
    Lever_Fortress_Bomb = "Lever-Fortress Bomb"
    Lever_Fortress_Main_Gate = "Lever-Fortress Main Gate"
    Lever_Fortress_Central_Shortcut = "Lever-Fortress Central Shortcut"
    Lever_Fortress_Statue = "Lever-Fortress Statue"
    Lever_Fortress_Watchtower_Lower = "Lever-Fortress Watchtower Lower"
    Lever_Fortress_Bridge = "Lever-Fortress Bridge"
    Lever_Fortress_Pre_Main_Gate = "Lever-Fortress Pre-Main Gate"
    Lever_Fortress_Watchtower_Upper = "Lever-Fortress Watchtower Upper"
    Lever_Fortress_North_West = "Lever-Fortress North West"
    Lever_Estate_Elevator_Left = "Lever-Estate Elevator Left"
    Lever_Estate_Elevator_Right = "Lever-Estate Elevator Right"
    Lever_Garden_of_Love = "Lever-Garden of Love"
    Lever_Garden_of_Life_End = "Lever-Garden of Life End"
    Lever_Garden_of_Peace = "Lever-Garden of Peace"
    Lever_Garden_of_Joy = "Lever-Garden of Joy"
    Lever_Garden_of_Love_Turncam = "Lever-Garden of Love Turncam"
    Lever_Garden_of_Life_Lanterns = "Lever-Garden of Life Lanterns"
    Lever_Estate_Underground_Urn_Shed = "Lever-Estate Underground Urn Shed"
    Lever_Manor_Big_Pot_Arena = "Lever-Manor Big Pot Arena"
    Lever_Manor_Bookshelf_Shortcut = "Lever-Manor Bookshelf Shortcut"

    # Doors
    Grove_of_Spirits_Door = "Grove of Spirits Door"
    Lost_Cemetery_Door = "Lost Cemetery Door"
    Stranded_Sailor_Door = "Stranded Sailor Door"
    Castle_Lockstone_Door = "Castle Lockstone Door"
    Camp_of_the_Free_Crows_Door = "Camp of the Free Crows Door"
    Old_Watchtowers_Door = "Old Watchtowers Door"
    Bettys_Lair_Door = "Betty's Lair Door"
    Overgrown_Ruins_Door = "Overgrown Ruins Door"
    Mushroom_Dungeon_Door = "Mushroom Dungeon Door"
    Flooded_Fortress_Door = "Flooded Fortress Door"
    Throne_of_the_Frog_King_Door = "Throne of the Frog King Door"
    Estate_of_the_Urn_Witch_Door = "Estate of the Urn Witch Door"
    Ceramic_Manor_Door = "Ceramic Manor Door"
    Inner_Furnace_Door = "Inner Furnace Door"
    The_Urn_Witchs_Laboratory_Door = "The Urn Witch's Laboratory Door"

    # Keys
    Key_Cemetery_Central = "Key-Cemetery Central"
    Key_Cemetery_Grey_Crow = "Key-Cemetery Grey Crow"
    Key_Camp_of_the_Free_Crows = "Key-Camp of the Free Crows"
    Key_Lockstone_West = "Key-Lockstone West"
    Key_Lockstone_North = "Key-Lockstone North"
    Key_Overgrown_Ruins = "Key-Overgrown Ruins"
    Key_Dungeon_Hall = "Key-Dungeon Hall"
    Key_Dungeon_Right = "Key-Dungeon Right"
    Key_Dungeon_Near_Water_Arena = "Key-Dungeon Near Water Arena"
    Key_Manor_Under_Dining_Room = "Key-Manor Under Dining Room"
    Key_Manor_After_Spinny_Pot_Room = "Key-Manor After Spinny Pot Room"
    Key_Manor_Library = "Key-Manor Library"

    # Crow Souls
    Crow_Manor_After_Torch_Puzzle = "Crow-Manor After Torch Puzzle"
    Crow_Manor_Imp_Loft = "Crow-Manor Imp Loft"
    Crow_Manor_Library = "Crow-Manor Library"
    Crow_Manor_Bedroom = "Crow-Manor Bedroom"
    Crow_Dungeon_Hall = "Crow-Dungeon Hall"
    Crow_Dungeon_Water_Arena = "Crow-Dungeon Water Arena"
    Crow_Dungeon_Cobweb = "Crow-Dungeon Cobweb"
    Crow_Dungeon_Rightmost = "Crow-Dungeon Rightmost"
    Crow_Lockstone_East = "Crow-Lockstone East"
    Crow_Lockstone_West = "Crow-Lockstone West"
    Crow_Lockstone_West_Locked = "Crow-Lockstone West Locked"
    Crow_Lockstone_South_West = "Crow-Lockstone South West"


class DeathsDoorEventLocationName(str, Enum):
    VICTORY = "Defeat the Lord of Doors"


class DeathsDoorLocationData(NamedTuple):
    name: DeathsDoorLocationName
    location_id: int
    region: R
    location_groups: List[LocationGroup]


location_table: List[DeathsDoorLocationData] = [
# Spells and their upgrades
    DeathsDoorLocationData(DeathsDoorLocationName.Fire_Avarice, 0, R.HALL_OF_DOORS, [LocationGroup.Spell]),
    DeathsDoorLocationData(DeathsDoorLocationName.Bomb_Avarice, 0, R.HALL_OF_DOORS, [LocationGroup.Spell]),
    DeathsDoorLocationData(DeathsDoorLocationName.Hookshot_Avarice, 0, R.HALL_OF_DOORS, [LocationGroup.Spell]),
    DeathsDoorLocationData(DeathsDoorLocationName.Fire_Silent_Servant, 0, R.LOST_CEMETERY, [LocationGroup.Spell]),
    DeathsDoorLocationData(DeathsDoorLocationName.Bomb_Silent_Servant, 0, R.LOST_CEMETERY, [LocationGroup.Spell]),
    DeathsDoorLocationData(DeathsDoorLocationName.Hookshot_Silent_Servant, 0, R.LOST_CEMETERY, [LocationGroup.Spell]),
    DeathsDoorLocationData(DeathsDoorLocationName.Arrow_Silent_Servant, 0, R.LOST_CEMETERY, [LocationGroup.Spell]),

    # Weapons
    DeathsDoorLocationData(DeathsDoorLocationName.Rogue_Daggers, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Weapon]),
    DeathsDoorLocationData(DeathsDoorLocationName.Discarded_Umbrella, 0, R.HALL_OF_DOORS, [LocationGroup.Weapon]),
    DeathsDoorLocationData(DeathsDoorLocationName.Reapers_Greatsword, 0, R.STRANDED_SAILOR, [LocationGroup.Weapon]),
    DeathsDoorLocationData(DeathsDoorLocationName.Thunder_Hammer, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Weapon]),

    # Giant Souls
    DeathsDoorLocationData(DeathsDoorLocationName.Betty, 0, R.BETTYS_LAIR, [LocationGroup.Giant_Soul]),
    DeathsDoorLocationData(DeathsDoorLocationName.Frog_King, 0, R.THRONE_OF_THE_FROG_KING, [LocationGroup.Giant_Soul]),
    DeathsDoorLocationData(DeathsDoorLocationName.Grandma, 0, R.URN_WITCHS_LABORATORY, [LocationGroup.Giant_Soul]),

    # Shrines
    DeathsDoorLocationData(DeathsDoorLocationName.Heart_Shrine_Cemetery_Behind_Entrance, 0, R.LOST_CEMETERY, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Magic_Shrine_Cemetery_After_Smough_Arena, 0, R.LOST_CEMETERY, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Heart_Shrine_Cemetery_Winding_Bridge_End, 0, R.LOST_CEMETERY, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Heart_Shrine_Hookshot_Arena, 0, R.STRANDED_SAILOR, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Magic_Shrine_Sailor_Turncam, 0, R.STRANDED_SAILOR, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Magic_Shrine_Lockstone_Secret_West, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Heart_Shrine_Camp_Ice_Skating, 0, R.CAMP_OF_THE_FREE_CROWS, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Magic_Shrine_Ruins_Hookshot_Arena, 0, R.OVERGROWN_RUINS, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Magic_Shrine_Ruins_Turncam, 0, R.OVERGROWN_RUINS, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Heart_Shrine_Dungeon_Water_Arena, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Heart_Shrine_Ruins_Sewer, 0, R.OVERGROWN_RUINS, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Magic_Shrine_Fortress_Bow_Secret, 0, R.FLOODED_FORTRESS, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Magic_Shrine_Estate_Left_of_Manor, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Heart_Shrine_Garden_of_Life, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Magic_Shrine_Manor_Bathroom_Puzzle, 0, R.CERAMIC_MANOR, [LocationGroup.Shrine]),
    DeathsDoorLocationData(DeathsDoorLocationName.Heart_Shrine_Furnace_Cart_Puzzle, 0, R.FURNACE_OBSERVATION_ROOMS, [LocationGroup.Shrine]),

    # Shiny Things
    DeathsDoorLocationData(DeathsDoorLocationName.Engagement_Ring, 0, R.CERAMIC_MANOR, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Old_Compass, 0, R.LOST_CEMETERY, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Incense, 0, R.LOST_CEMETERY, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Undying_Blossom, 0, R.LOST_CEMETERY, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Old_Photograph, 0, R.CERAMIC_MANOR, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Sludge_Filled_Urn, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Token_of_Death, 0, R.LOST_CEMETERY, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Rusty_Garden_Trowel, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Captains_Log, 0, R.STRANDED_SAILOR, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Giant_Arrowhead, 0, R.THRONE_OF_THE_FROG_KING, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Malformed_Seed, 0, R.OVERGROWN_RUINS, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Corrupted_Antler, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Magical_Forest_Horn, 0, R.OVERGROWN_RUINS, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Ancient_Crown, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Grunts_Old_Mask, 0, R.STRANDED_SAILOR, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Ancient_Door_Scale_Model, 0, R.HALL_OF_DOORS, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Modern_Door_Scale_Model, 0, R.HALL_OF_DOORS, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Rusty_Belltower_Key, 0, R.HALL_OF_DOORS, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Surveillance_Device, 0, R.HALL_OF_DOORS, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Shiny_Medallion, 0, R.CAMP_OF_THE_FREE_CROWS, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Ink_Covered_Teddy_Bear, 0, R.STRANDED_SAILOR, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Deaths_Contract, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Makeshift_Soul_Key, 0, R.GROVE_OF_SPIRITS, [LocationGroup.Shiny_Thing]),
    DeathsDoorLocationData(DeathsDoorLocationName.Mysterious_Locket, 0, R.OLD_WATCHTOWERS, [LocationGroup.Shiny_Thing]),

    # Seeds
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Cemetery_Broken_Bridge, 0, R.LOST_CEMETERY, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Catacombs_Tower, 0, R.LOST_CEMETERY, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Cemetery_Left_of_Main_Entrance, 0, R.LOST_CEMETERY, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Cemetery_Near_Tablet_Gate, 0, R.LOST_CEMETERY, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Between_Cemetery_and_Sailor, 0, R.LOST_CEMETERY, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Sailor_Upper, 0, R.STRANDED_SAILOR, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Lockstone_Upper_East, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Lockstone_Soul_Door, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Lockstone_Behind_Bars, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Lockstone_Entrance_West, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Lockstone_North, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Camp_Ledge_With_Huts, 0, R.CAMP_OF_THE_FREE_CROWS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Camp_Stall, 0, R.CAMP_OF_THE_FREE_CROWS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Camp_Rooftops, 0, R.CAMP_OF_THE_FREE_CROWS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Watchtowers_Ice_Skating, 0, R.OLD_WATCHTOWERS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Watchtowers_Tablet_Door, 0, R.OLD_WATCHTOWERS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Watchtowers_Archer_Platform, 0, R.OLD_WATCHTOWERS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Watchtowers_Boxes, 0, R.OLD_WATCHTOWERS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Dungeon_Fire_Puzzle_Near_Water_Arena, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Ruins_Lord_of_Doors_Arena, 0, R.OVERGROWN_RUINS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Ruins_Fire_Plant_Corridor, 0, R.OVERGROWN_RUINS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Dungeon_Water_Arena_Left_Exit, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Ruins_Right_Middle, 0, R.OVERGROWN_RUINS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Ruins_On_Settlement_Wall, 0, R.OVERGROWN_RUINS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Ruins_Behind_Boxes, 0, R.OVERGROWN_RUINS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Ruins_Down_Through_Bomb_Wall, 0, R.OVERGROWN_RUINS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Dungeon_Above_Rightmost_Crow, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Dungeon_Right_Above_Key, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Dungeon_Avarice_Bridge, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Fortress_Watchtower, 0, R.FLOODED_FORTRESS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Fortress_Statue, 0, R.FLOODED_FORTRESS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Fortress_Bridge, 0, R.FLOODED_FORTRESS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Fortress_Intro_Crate, 0, R.FLOODED_FORTRESS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Fortress_East_After_Statue, 0, R.FLOODED_FORTRESS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Estate_Family_Tomb, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Estate_Entrance, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Estate_Hedge_Gaps, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Garden_of_Joy, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Manor_Boxes, 0, R.CERAMIC_MANOR, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Manor_Near_Brazier, 0, R.CERAMIC_MANOR, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Manor_Below_Big_Pot_Arena, 0, R.CERAMIC_MANOR, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Manor_Rafters, 0, R.CERAMIC_MANOR, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Manor_Main_Room_Upper, 0, R.CERAMIC_MANOR, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Manor_Spinny_Pot_Room, 0, R.CERAMIC_MANOR, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Manor_Library_Shelf, 0, R.CERAMIC_MANOR, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Cart_Puzzle, 0, R.FURNACE_OBSERVATION_ROOMS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Furnace_Entrance, 0, R.FURNACE_OBSERVATION_ROOMS, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Inner_Furnace_Horizontal_Pistons, 0, R.INNER_FURNACE, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Inner_Furnace_Conveyor_Bridge, 0, R.INNER_FURNACE, [LocationGroup.Seed]),
    DeathsDoorLocationData(DeathsDoorLocationName.Seed_Inner_Furnace_Conveyor_Gauntlet, 0, R.INNER_FURNACE, [LocationGroup.Seed]),

    # Soul Orbs
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Fire_Return_Upper, 0, R.HALL_OF_DOORS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Hookshot_Secret, 0, R.HALL_OF_DOORS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Bomb_Return, 0, R.HALL_OF_DOORS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Bomb_Secret, 0, R.HALL_OF_DOORS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Hookshot_Return, 0, R.HALL_OF_DOORS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Fire_Return_Lower, 0, R.HALL_OF_DOORS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Fire_Secret, 0, R.HALL_OF_DOORS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Catacombs_Exit, 0, R.LOST_CEMETERY, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Cemetery_Hookshot_Towers, 0, R.LOST_CEMETERY, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Cemetery_Under_Bridge, 0, R.LOST_CEMETERY, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Cemetery_East_Tree, 0, R.LOST_CEMETERY, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Cemetery_Winding_Bridge_End, 0, R.LOST_CEMETERY, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Catacombs_Room_2, 0, R.LOST_CEMETERY, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Catacombs_Room_1, 0, R.LOST_CEMETERY, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Cemetery_Gated_Sewer, 0, R.LOST_CEMETERY, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Catacombs_Entrance, 0, R.LOST_CEMETERY, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Cemetery_Cave, 0, R.LOST_CEMETERY, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Sailor_Turncam, 0, R.STRANDED_SAILOR, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_North_Lockstone_Sewer, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Lockstone_Hookshot_North, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Lockstone_Exit, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_West_Lockstone_Sewer, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Camp_Rooftops, 0, R.CAMP_OF_THE_FREE_CROWS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Camp_Broken_Bridge, 0, R.CAMP_OF_THE_FREE_CROWS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Watchtowers_Behind_Barb_Elevator, 0, R.OLD_WATCHTOWERS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Dungeon_Vine, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Ruins_Stump, 0, R.OVERGROWN_RUINS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Ruins_Outside_Left_Dungeon_Exit, 0, R.OVERGROWN_RUINS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Dungeon_Cobweb, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Ruins_Left_After_Key_Door, 0, R.OVERGROWN_RUINS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Ruins_Lower_Bomb_Wall, 0, R.OVERGROWN_RUINS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Ruins_Lord_of_Doors_Arena_Hookshot, 0, R.OVERGROWN_RUINS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Dungeon_Lower_Entrance, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Ruins_Upper_Above_Horn, 0, R.OVERGROWN_RUINS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Ruins_Above_Three_Plants, 0, R.OVERGROWN_RUINS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Ruins_Up_Turncam_Ladder, 0, R.OVERGROWN_RUINS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Ruins_Above_Entrance_Gate, 0, R.OVERGROWN_RUINS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Ruins_Upper_Bomb_Wall, 0, R.OVERGROWN_RUINS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Dungeon_Left_Exit_Shelf, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Ruins_Lower_Hookshot, 0, R.OVERGROWN_RUINS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Fortress_Bomb, 0, R.FLOODED_FORTRESS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Fortress_Hidden_Sewer, 0, R.FLOODED_FORTRESS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Fortress_Drop, 0, R.FLOODED_FORTRESS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Estate_Access_Crypt, 0, R.LOST_CEMETERY, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Estate_Balcony, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Garden_of_Love_Turncam, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Garden_of_Life_Hookshot_Loop, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Garden_of_Love_Bomb_Walls, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Garden_of_Life_Bomb_Wall, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Estate_Broken_Boardwalk, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Estate_Secret_Cave, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Estate_Twin_Benches, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Estate_Sewer_Middle, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Estate_Sewer_End, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Garden_of_Peace, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Manor_Imp_Loft, 0, R.CERAMIC_MANOR, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Manor_Library_Shelf, 0, R.CERAMIC_MANOR, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Manor_Chandelier, 0, R.CERAMIC_MANOR, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Furnace_Lantern_Chain, 0, R.FURNACE_OBSERVATION_ROOMS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Small_Room, 0, R.FURNACE_OBSERVATION_ROOMS, [LocationGroup.Soul_Orb]),
    DeathsDoorLocationData(DeathsDoorLocationName.Soul_Orb_Furnace_Entrance_Sewer, 0, R.FURNACE_OBSERVATION_ROOMS, [LocationGroup.Soul_Orb]),

    # Tablets
    DeathsDoorLocationData(DeathsDoorLocationName.Red_Ancient_Tablet_of_Knowledge, 0, R.FLOODED_FORTRESS, [LocationGroup.Tablet]),
    DeathsDoorLocationData(DeathsDoorLocationName.Yellow_Ancient_Tablet_of_Knowledge, 0, R.OVERGROWN_RUINS, [LocationGroup.Tablet]),
    DeathsDoorLocationData(DeathsDoorLocationName.Green_Ancient_Tablet_of_Knowledge, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Tablet]),
    DeathsDoorLocationData(DeathsDoorLocationName.Cyan_Ancient_Tablet_of_Knowledge, 0, R.LOST_CEMETERY, [LocationGroup.Tablet]),
    DeathsDoorLocationData(DeathsDoorLocationName.Blue_Ancient_Tablet_of_Knowledge, 0, R.OLD_WATCHTOWERS, [LocationGroup.Tablet]),
    DeathsDoorLocationData(DeathsDoorLocationName.Purple_Ancient_Tablet_of_Knowledge, 0, R.LOST_CEMETERY, [LocationGroup.Tablet]),
    DeathsDoorLocationData(DeathsDoorLocationName.Estate_Owl, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Tablet]),
    DeathsDoorLocationData(DeathsDoorLocationName.Ruins_Owl, 0, R.OVERGROWN_RUINS, [LocationGroup.Tablet]),
    DeathsDoorLocationData(DeathsDoorLocationName.Watchtowers_Owl, 0, R.OLD_WATCHTOWERS, [LocationGroup.Tablet]),

    # Levers
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Bomb_Exit, 0, R.HALL_OF_DOORS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Cemetery_Sewer, 0, R.LOST_CEMETERY, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Guardian_of_the_Door_Access, 0, R.LOST_CEMETERY, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Cemetery_Shortcut_to_East_Tree, 0, R.LOST_CEMETERY, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Cemetery_East_Tree, 0, R.LOST_CEMETERY, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Catacombs_Tower, 0, R.LOST_CEMETERY, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Cemetery_Exit_to_Estate, 0, R.LOST_CEMETERY, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Catacombs_Exit, 0, R.LOST_CEMETERY, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Hookshot_Silent_Servant, 0, R.LOST_CEMETERY, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Sailor_Turncam_Upper, 0, R.STRANDED_SAILOR, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Sailor_Turncam_Lower, 0, R.STRANDED_SAILOR, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Sailor_Greatsword_Gate, 0, R.STRANDED_SAILOR, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Lockstone_East_Start_Shortcut, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Lockstone_Entrance, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Lockstone_East_Lower, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Lockstone_Upper_Shortcut, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Lockstone_Dual_Laser_Puzzle, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Lockstone_Tracking_Beam_Puzzle, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Lockstone_Vertical_Laser_Puzzle, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Lockstone_North_Puzzle, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Lockstone_Shrine, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Lockstone_Hookshot_Puzzle, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Lockstone_Upper_Puzzle, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Lockstone_Upper_Dual_Laser_Puzzle, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Watchtowers_Before_Ice_Arena, 0, R.OLD_WATCHTOWERS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Watchtowers_After_Ice_Skating, 0, R.OLD_WATCHTOWERS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Watchtowers_After_Boomers, 0, R.OLD_WATCHTOWERS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Ruins_Settlement_Gate, 0, R.OVERGROWN_RUINS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Ruins_Upper_Dungeon_Entrance, 0, R.OVERGROWN_RUINS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Ruins_Ladder_Left_of_Lord_of_Doors_Arena, 0, R.OVERGROWN_RUINS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Ruins_Entrance_Ladder_Shortcut, 0, R.OVERGROWN_RUINS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Ruins_Main_Gate, 0, R.OVERGROWN_RUINS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Dungeon_Entrance_Right_Gate, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Dungeon_Entrance_Left_Gate, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Dungeon_Above_Rightmost_Crow, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Fortress_Bomb, 0, R.FLOODED_FORTRESS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Fortress_Main_Gate, 0, R.FLOODED_FORTRESS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Fortress_Central_Shortcut, 0, R.FLOODED_FORTRESS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Fortress_Statue, 0, R.FLOODED_FORTRESS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Fortress_Watchtower_Lower, 0, R.FLOODED_FORTRESS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Fortress_Bridge, 0, R.FLOODED_FORTRESS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Fortress_Pre_Main_Gate, 0, R.FLOODED_FORTRESS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Fortress_Watchtower_Upper, 0, R.FLOODED_FORTRESS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Fortress_North_West, 0, R.FLOODED_FORTRESS, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Estate_Elevator_Left, 0, R.LOST_CEMETERY, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Estate_Elevator_Right, 0, R.LOST_CEMETERY, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Garden_of_Love, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Garden_of_Life_End, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Garden_of_Peace, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Garden_of_Joy, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Garden_of_Love_Turncam, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Garden_of_Life_Lanterns, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Estate_Underground_Urn_Shed, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Manor_Big_Pot_Arena, 0, R.CERAMIC_MANOR, [LocationGroup.Lever]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lever_Manor_Bookshelf_Shortcut, 0, R.CERAMIC_MANOR, [LocationGroup.Lever]),

    # Doors
    DeathsDoorLocationData(DeathsDoorLocationName.Grove_of_Spirits_Door, 0, R.HALL_OF_DOORS, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Lost_Cemetery_Door, 0, R.LOST_CEMETERY, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Stranded_Sailor_Door, 0, R.STRANDED_SAILOR, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Castle_Lockstone_Door, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Camp_of_the_Free_Crows_Door, 0, R.CAMP_OF_THE_FREE_CROWS, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Old_Watchtowers_Door, 0, R.OLD_WATCHTOWERS, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Bettys_Lair_Door, 0, R.BETTYS_LAIR, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Overgrown_Ruins_Door, 0, R.OVERGROWN_RUINS, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Mushroom_Dungeon_Door, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Flooded_Fortress_Door, 0, R.FLOODED_FORTRESS, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Throne_of_the_Frog_King_Door, 0, R.THRONE_OF_THE_FROG_KING, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Estate_of_the_Urn_Witch_Door, 0, R.ESTATE_OF_THE_URN_WITCH, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Ceramic_Manor_Door, 0, R.CERAMIC_MANOR, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.Inner_Furnace_Door, 0, R.INNER_FURNACE, [LocationGroup.Door]),
    DeathsDoorLocationData(DeathsDoorLocationName.The_Urn_Witchs_Laboratory_Door, 0, R.URN_WITCHS_LABORATORY, [LocationGroup.Door]),

    # Keys
    DeathsDoorLocationData(DeathsDoorLocationName.Key_Cemetery_Central, 0, R.LOST_CEMETERY, [LocationGroup.Key]),
    DeathsDoorLocationData(DeathsDoorLocationName.Key_Cemetery_Grey_Crow, 0, R.LOST_CEMETERY, [LocationGroup.Key]),
    DeathsDoorLocationData(DeathsDoorLocationName.Key_Camp_of_the_Free_Crows, 0, R.CAMP_OF_THE_FREE_CROWS, [LocationGroup.Key]),
    DeathsDoorLocationData(DeathsDoorLocationName.Key_Lockstone_West, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Key]),
    DeathsDoorLocationData(DeathsDoorLocationName.Key_Lockstone_North, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Key]),
    DeathsDoorLocationData(DeathsDoorLocationName.Key_Overgrown_Ruins, 0, R.OVERGROWN_RUINS, [LocationGroup.Key]),
    DeathsDoorLocationData(DeathsDoorLocationName.Key_Dungeon_Hall, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Key]),
    DeathsDoorLocationData(DeathsDoorLocationName.Key_Dungeon_Right, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Key]),
    DeathsDoorLocationData(DeathsDoorLocationName.Key_Dungeon_Near_Water_Arena, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Key]),
    DeathsDoorLocationData(DeathsDoorLocationName.Key_Manor_Under_Dining_Room, 0, R.CERAMIC_MANOR, [LocationGroup.Key]),
    DeathsDoorLocationData(DeathsDoorLocationName.Key_Manor_After_Spinny_Pot_Room, 0, R.CERAMIC_MANOR, [LocationGroup.Key]),
    DeathsDoorLocationData(DeathsDoorLocationName.Key_Manor_Library, 0, R.CERAMIC_MANOR, [LocationGroup.Key]),

    # Crow Souls
    DeathsDoorLocationData(DeathsDoorLocationName.Crow_Manor_After_Torch_Puzzle, 0, R.CERAMIC_MANOR, [LocationGroup.Lost_Crow]),
    DeathsDoorLocationData(DeathsDoorLocationName.Crow_Manor_Imp_Loft, 0, R.CERAMIC_MANOR, [LocationGroup.Lost_Crow]),
    DeathsDoorLocationData(DeathsDoorLocationName.Crow_Manor_Library, 0, R.CERAMIC_MANOR, [LocationGroup.Lost_Crow]),
    DeathsDoorLocationData(DeathsDoorLocationName.Crow_Manor_Bedroom, 0, R.CERAMIC_MANOR, [LocationGroup.Lost_Crow]),
    DeathsDoorLocationData(DeathsDoorLocationName.Crow_Dungeon_Hall, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Lost_Crow]),
    DeathsDoorLocationData(DeathsDoorLocationName.Crow_Dungeon_Water_Arena, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Lost_Crow]),
    DeathsDoorLocationData(DeathsDoorLocationName.Crow_Dungeon_Cobweb, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Lost_Crow]),
    DeathsDoorLocationData(DeathsDoorLocationName.Crow_Dungeon_Rightmost, 0, R.MUSHROOM_DUNGEON, [LocationGroup.Lost_Crow]),
    DeathsDoorLocationData(DeathsDoorLocationName.Crow_Lockstone_East, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lost_Crow]),
    DeathsDoorLocationData(DeathsDoorLocationName.Crow_Lockstone_West, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lost_Crow]),
    DeathsDoorLocationData(DeathsDoorLocationName.Crow_Lockstone_West_Locked, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lost_Crow]),
    DeathsDoorLocationData(DeathsDoorLocationName.Crow_Lockstone_South_West, 0, R.CASTLE_LOCKSTONE, [LocationGroup.Lost_Crow]),
]

def locations_for_group(group: LocationGroup) -> List[str]:
    location_names = []
    for data in location_table:
        if group in data.location_groups:
            location_names.append(data.name.value)
    return location_names


location_name_to_id: Dict[str, int] = {
    data.name.value: data.location_id for data in location_table
}

location_name_groups: Dict[str, Set[str]] = {}
for loc_data in location_table:
    loc_group_name = loc_data.name.value.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_data.name.value)

for group in LocationGroup:
    location_name_groups[group.name] = locations_for_group(group)
