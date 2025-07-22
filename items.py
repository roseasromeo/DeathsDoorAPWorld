from enum import Enum

from typing import NamedTuple, Dict, List, Set
from BaseClasses import ItemClassification

class ItemGroup(str, Enum):
    Spell = "Spell"
    Weapon = "Weapon"
    Key = "Key"
    Giant_Soul = "Giant Soul"
    Shiny_Thing = "Shiny Thing"
    Tablet = "Tablet"
    Lever = "Lever"
    Door = "Door"
    Lost_Crow = "Lost Crow"

class DeathsDoorItemName(str, Enum):
    Fire = "Fire"
    Bomb = "Bomb"
    Hookshot = "Hookshot"
    Bow = "Arrow Upgrade"
    Rogue_Daggers = "Rogue Daggers"
    Discarded_Umbrella = "Discarded Umbrella"
    Reapers_Greatsword = "Reaper's Greatsword"
    Thunder_Hammer = "Thunder Hammer"
    Vitality_Shard = "Vitality Shard"
    Magic_Shard = "Magic Shard"
    Life_Seed = "Life Seed"
    Souls = "100 Souls"
    Pink_Key = "Pink Key"
    Green_Key = "Green Key"
    Yellow_Key = "Yellow Key"
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
    Red_Ancient_Tablet_of_Knowledge = "Red Ancient Tablet of Knowledge"
    Yellow_Ancient_Tablet_of_Knowledge = "Yellow Ancient Tablet of Knowledge"
    Green_Ancient_Tablet_of_Knowledge = "Green Ancient Tablet of Knowledge"
    Cyan_Ancient_Tablet_of_Knowledge = "Cyan Ancient Tablet of Knowledge"
    Blue_Ancient_Tablet_of_Knowledge = "Blue Ancient Tablet of Knowledge"
    Purple_Ancient_Tablet_of_Knowledge = "Purple Ancient Tablet of Knowledge"
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
    Lever_Ruins_Ladder_Left_of_Lord_of_Doors_Arena = "Lever-Ruins Ladder Left of Lord of Doors Arena"
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
    Giant_Soul_of_The_Urn_Witch = "Giant Soul of The Urn Witch"
    Giant_Soul_of_The_Frog_King = "Giant Soul of The Frog King"
    Giant_Soul_of_Betty = "Giant Soul of Betty"
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


class DeathsDoorEventName(str, Enum):
    VICTORY = "Goal Complete",
    OOL = "Out of Logic Item"

class DeathsDoorItemData(NamedTuple):
    name: DeathsDoorItemName
    item_id: int | None
    classification: ItemClassification
    base_quantity_in_item_pool: int 
    item_groups: List[ItemGroup]

item_table: List[DeathsDoorItemData] = [
    DeathsDoorItemData(DeathsDoorItemName.Fire, 0, ItemClassification.progression, 1, [ItemGroup.Spell] ),
    DeathsDoorItemData(DeathsDoorItemName.Bomb, 0, ItemClassification.progression, 1, [ItemGroup.Spell] ),
    DeathsDoorItemData(DeathsDoorItemName.Hookshot, 0, ItemClassification.progression, 1, [ItemGroup.Spell] ),
    DeathsDoorItemData(DeathsDoorItemName.Bow, 0, ItemClassification.progression, 1, [ItemGroup.Spell] ),
    DeathsDoorItemData(DeathsDoorItemName.Rogue_Daggers, 0, ItemClassification.progression, 1, [ItemGroup.Weapon] ),
    DeathsDoorItemData(DeathsDoorItemName.Discarded_Umbrella, 0, ItemClassification.progression, 1, [ItemGroup.Weapon] ),
    DeathsDoorItemData(DeathsDoorItemName.Reapers_Greatsword, 0, ItemClassification.progression, 1, [ItemGroup.Weapon] ),
    DeathsDoorItemData(DeathsDoorItemName.Thunder_Hammer, 0, ItemClassification.progression, 1, [ItemGroup.Weapon] ),
    DeathsDoorItemData(DeathsDoorItemName.Vitality_Shard, 0, ItemClassification.progression, 1, [] ),
    DeathsDoorItemData(DeathsDoorItemName.Magic_Shard, 0, ItemClassification.progression, 1, [] ),
    DeathsDoorItemData(DeathsDoorItemName.Life_Seed, 0, ItemClassification.progression, 1, [] ),
    DeathsDoorItemData(DeathsDoorItemName.Souls, 0, ItemClassification.progression, 1, [] ),
    DeathsDoorItemData(DeathsDoorItemName.Pink_Key, 0, ItemClassification.progression, 1, [ItemGroup.Key] ),
    DeathsDoorItemData(DeathsDoorItemName.Green_Key, 0, ItemClassification.progression, 1, [ItemGroup.Key] ),
    DeathsDoorItemData(DeathsDoorItemName.Yellow_Key, 0, ItemClassification.progression, 1, [ItemGroup.Key] ),
    DeathsDoorItemData(DeathsDoorItemName.Engagement_Ring, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Old_Compass, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Incense, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Undying_Blossom, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Old_Photograph, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Sludge_Filled_Urn, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Token_of_Death, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Rusty_Garden_Trowel, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Captains_Log, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Giant_Arrowhead, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Malformed_Seed, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Corrupted_Antler, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Magical_Forest_Horn, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Ancient_Crown, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Grunts_Old_Mask, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Ancient_Door_Scale_Model, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Modern_Door_Scale_Model, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Rusty_Belltower_Key, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Surveillance_Device, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Shiny_Medallion, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Ink_Covered_Teddy_Bear, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Deaths_Contract, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Makeshift_Soul_Key, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Mysterious_Locket, 0, ItemClassification.progression, 1, [ItemGroup.Shiny_Thing] ),
    DeathsDoorItemData(DeathsDoorItemName.Red_Ancient_Tablet_of_Knowledge, 0, ItemClassification.progression, 1, [ItemGroup.Tablet] ),
    DeathsDoorItemData(DeathsDoorItemName.Yellow_Ancient_Tablet_of_Knowledge, 0, ItemClassification.progression, 1, [ItemGroup.Tablet] ),
    DeathsDoorItemData(DeathsDoorItemName.Green_Ancient_Tablet_of_Knowledge, 0, ItemClassification.progression, 1, [ItemGroup.Tablet] ),
    DeathsDoorItemData(DeathsDoorItemName.Cyan_Ancient_Tablet_of_Knowledge, 0, ItemClassification.progression, 1, [ItemGroup.Tablet] ),
    DeathsDoorItemData(DeathsDoorItemName.Blue_Ancient_Tablet_of_Knowledge, 0, ItemClassification.progression, 1, [ItemGroup.Tablet] ),
    DeathsDoorItemData(DeathsDoorItemName.Purple_Ancient_Tablet_of_Knowledge, 0, ItemClassification.progression, 1, [ItemGroup.Tablet] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Bomb_Exit, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Cemetery_Sewer, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Guardian_of_the_Door_Access, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Cemetery_Shortcut_to_East_Tree, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Cemetery_East_Tree, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Catacombs_Tower, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Cemetery_Exit_to_Estate, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Catacombs_Exit, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Hookshot_Silent_Servant, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Sailor_Turncam_Upper, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Sailor_Turncam_Lower, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Sailor_Greatsword_Gate, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Lockstone_East_Start_Shortcut, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Lockstone_Entrance, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Lockstone_East_Lower, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Lockstone_Upper_Shortcut, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Lockstone_Dual_Laser_Puzzle, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Lockstone_Tracking_Beam_Puzzle, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Lockstone_Vertical_Laser_Puzzle, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Lockstone_North_Puzzle, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Lockstone_Shrine, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Lockstone_Hookshot_Puzzle, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Lockstone_Upper_Puzzle, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Lockstone_Upper_Dual_Laser_Puzzle, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Watchtowers_Before_Ice_Arena, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Watchtowers_After_Ice_Skating, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Watchtowers_After_Boomers, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Ruins_Settlement_Gate, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Ruins_Upper_Dungeon_Entrance, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Ruins_Ladder_Left_of_Lord_of_Doors_Arena, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Ruins_Entrance_Ladder_Shortcut, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Ruins_Main_Gate, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Dungeon_Entrance_Right_Gate, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Dungeon_Entrance_Left_Gate, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Dungeon_Above_Rightmost_Crow, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Fortress_Bomb, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Fortress_Main_Gate, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Fortress_Central_Shortcut, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Fortress_Statue, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Fortress_Watchtower_Lower, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Fortress_Bridge, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Fortress_Pre_Main_Gate, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Fortress_Watchtower_Upper, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Fortress_North_West, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Estate_Elevator_Left, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Estate_Elevator_Right, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Garden_of_Love, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Garden_of_Life_End, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Garden_of_Peace, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Garden_of_Joy, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Garden_of_Love_Turncam, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Garden_of_Life_Lanterns, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Estate_Underground_Urn_Shed, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Manor_Big_Pot_Arena, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Lever_Manor_Bookshelf_Shortcut, 0, ItemClassification.progression, 1, [ItemGroup.Lever] ),
    DeathsDoorItemData(DeathsDoorItemName.Grove_of_Spirits_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Lost_Cemetery_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Stranded_Sailor_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Castle_Lockstone_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Camp_of_the_Free_Crows_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Old_Watchtowers_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Bettys_Lair_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Overgrown_Ruins_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Mushroom_Dungeon_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Flooded_Fortress_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Throne_of_the_Frog_King_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Estate_of_the_Urn_Witch_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Ceramic_Manor_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Inner_Furnace_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.The_Urn_Witchs_Laboratory_Door, 0, ItemClassification.progression, 1, [ItemGroup.Door] ),
    DeathsDoorItemData(DeathsDoorItemName.Giant_Soul_of_The_Urn_Witch, 0, ItemClassification.progression, 1, [ItemGroup.Giant_Soul] ),
    DeathsDoorItemData(DeathsDoorItemName.Giant_Soul_of_The_Frog_King, 0, ItemClassification.progression, 1, [ItemGroup.Giant_Soul] ),
    DeathsDoorItemData(DeathsDoorItemName.Giant_Soul_of_Betty, 0, ItemClassification.progression, 1, [ItemGroup.Giant_Soul] ),
    DeathsDoorItemData(DeathsDoorItemName.Crow_Manor_After_Torch_Puzzle, 0, ItemClassification.progression, 1, [ItemGroup.Lost_Crow] ),
    DeathsDoorItemData(DeathsDoorItemName.Crow_Manor_Imp_Loft, 0, ItemClassification.progression, 1, [ItemGroup.Lost_Crow] ),
    DeathsDoorItemData(DeathsDoorItemName.Crow_Manor_Library, 0, ItemClassification.progression, 1, [ItemGroup.Lost_Crow] ),
    DeathsDoorItemData(DeathsDoorItemName.Crow_Manor_Bedroom, 0, ItemClassification.progression, 1, [ItemGroup.Lost_Crow] ),
    DeathsDoorItemData(DeathsDoorItemName.Crow_Dungeon_Hall, 0, ItemClassification.progression, 1, [ItemGroup.Lost_Crow] ),
    DeathsDoorItemData(DeathsDoorItemName.Crow_Dungeon_Water_Arena, 0, ItemClassification.progression, 1, [ItemGroup.Lost_Crow] ),
    DeathsDoorItemData(DeathsDoorItemName.Crow_Dungeon_Cobweb, 0, ItemClassification.progression, 1, [ItemGroup.Lost_Crow] ),
    DeathsDoorItemData(DeathsDoorItemName.Crow_Dungeon_Rightmost, 0, ItemClassification.progression, 1, [ItemGroup.Lost_Crow] ),
    DeathsDoorItemData(DeathsDoorItemName.Crow_Lockstone_East, 0, ItemClassification.progression, 1, [ItemGroup.Lost_Crow] ),
    DeathsDoorItemData(DeathsDoorItemName.Crow_Lockstone_West, 0, ItemClassification.progression, 1, [ItemGroup.Lost_Crow] ),
    DeathsDoorItemData(DeathsDoorItemName.Crow_Lockstone_West_Locked, 0, ItemClassification.progression, 1, [ItemGroup.Lost_Crow] ),
    DeathsDoorItemData(DeathsDoorItemName.Crow_Lockstone_South_West, 0, ItemClassification.progression, 1, [ItemGroup.Lost_Crow] ),
]

item_name_to_id: Dict[str, int] = {
    data.name.value: data.item_id for data in item_table
}

filler_items: List[str] = [
    data.name.value
    for data in item_table
    if data.classification == ItemClassification.filler
]


# Items can be grouped using their names to allow easy checking if any item
# from that group has been collected. Group names can also be used for !hint
def items_for_group(group: ItemGroup) -> List[str]:
    item_names = []
    for data in item_table:
        if group in data.item_groups:
            item_names.append(data.name.value)
    return item_names


item_name_groups: Dict[str, Set[str]] = {}
for group in ItemGroup:
    item_name_groups[group.value] = items_for_group(group)


