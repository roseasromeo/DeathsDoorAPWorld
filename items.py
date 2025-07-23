from enum import Enum

from typing import NamedTuple, Dict, List, Set
from BaseClasses import ItemClassification


class ItemGroup(str, Enum):
    SPELL = "Spell"
    WEAPON = "Weapon"
    KEY = "Key"
    GIANT_SOUL = "Giant Soul"
    SHINY_THING = "Shiny Thing"
    TABLET = "Tablet"
    LEVER = "Lever"
    DOOR = "Door"
    LOST_CROW = "Lost Crow"


class DeathsDoorItemName(str, Enum):
    FIRE = "Fire"
    BOMB = "Bomb"
    HOOKSHOT = "Hookshot"
    BOW = "Arrow Upgrade"
    ROGUE_DAGGERS = "Rogue Daggers"
    DISCARDED_UMBRELLA = "Discarded Umbrella"
    REAPERS_GREATSWORD = "Reaper's Greatsword"
    THUNDER_HAMMER = "Thunder Hammer"
    VITALITY_SHARD = "Vitality Shard"
    MAGIC_SHARD = "Magic Shard"
    LIFE_SEED = "Life Seed"
    SOULS = "100 Souls"
    PINK_KEY = "Pink Key"
    GREEN_KEY = "Green Key"
    YELLOW_KEY = "Yellow Key"
    ENGAGEMENT_RING = "Engagement Ring"
    OLD_COMPASS = "Old Compass"
    INCENSE = "Incense"
    UNDYING_BLOSSOM = "Undying Blossom"
    OLD_PHOTOGRAPH = "Old Photograph"
    SLUDGE_FILLED_URN = "Sludge-Filled Urn"
    TOKEN_OF_DEATH = "Token of Death"
    RUSTY_GARDEN_TROWEL = "Rusty Garden Trowel"
    CAPTAINS_LOG = "Captain's Log"
    GIANT_ARROWHEAD = "Giant Arrowhead"
    MALFORMED_SEED = "Malformed Seed"
    CORRUPTED_ANTLER = "Corrupted Antler"
    MAGICAL_FOREST_HORN = "Magical Forest Horn"
    ANCIENT_CROWN = "Ancient Crown"
    GRUNTS_OLD_MASK = "Grunt's Old Mask"
    ANCIENT_DOOR_SCALE_MODEL = "Ancient Door Scale Model"
    MODERN_DOOR_SCALE_MODEL = "Modern Door Scale Model"
    RUSTY_BELLTOWER_KEY = "Rusty Belltower Key"
    SURVEILLANCE_DEVICE = "Surveillance Device"
    SHINY_MEDALLION = "Shiny Medallion"
    INK_COVERED_TEDDY_BEAR = "Ink-Covered Teddy Bear"
    DEATHS_CONTRACT = "Death's Contract"
    MAKESHIFT_SOUL_KEY = "Makeshift Soul Key"
    MYSTERIOUS_LOCKET = "Mysterious Locket"
    RED_ANCIENT_TABLET_OF_KNOWLEDGE = "Red Ancient Tablet of Knowledge"
    YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE = "Yellow Ancient Tablet of Knowledge"
    GREEN_ANCIENT_TABLET_OF_KNOWLEDGE = "Green Ancient Tablet of Knowledge"
    CYAN_ANCIENT_TABLET_OF_KNOWLEDGE = "Cyan Ancient Tablet of Knowledge"
    BLUE_ANCIENT_TABLET_OF_KNOWLEDGE = "Blue Ancient Tablet of Knowledge"
    PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE = "Purple Ancient Tablet of Knowledge"
    LEVER_BOMB_EXIT = "Lever-Bomb Exit"
    LEVER_CEMETERY_SEWER = "Lever-Cemetery Sewer"
    LEVER_GUARDIAN_OF_THE_DOOR_ACCESS = "Lever-Guardian of the Door Access"
    LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE = "Lever-Cemetery Shortcut to East Tree"
    LEVER_CEMETERY_EAST_TREE = "Lever-Cemetery East Tree"
    LEVER_CATACOMBS_TOWER = "Lever-Catacombs Tower"
    LEVER_CEMETERY_EXIT_TO_ESTATE = "Lever-Cemetery Exit to Estate"
    LEVER_CATACOMBS_EXIT = "Lever-Catacombs Exit"
    LEVER_HOOKSHOT_SILENT_SERVANT = "Lever-Hookshot Silent Servant"
    LEVER_SAILOR_TURNCAM_UPPER = "Lever-Sailor Turncam Upper"
    LEVER_SAILOR_TURNCAM_LOWER = "Lever-Sailor Turncam Lower"
    LEVER_SAILOR_GREATSWORD_GATE = "Lever-Sailor Greatsword Gate"
    LEVER_LOCKSTONE_EAST_START_SHORTCUT = "Lever-Lockstone East Start Shortcut"
    LEVER_LOCKSTONE_ENTRANCE = "Lever-Lockstone Entrance"
    LEVER_LOCKSTONE_EAST_LOWER = "Lever-Lockstone East Lower"
    LEVER_LOCKSTONE_UPPER_SHORTCUT = "Lever-Lockstone Upper Shortcut"
    LEVER_LOCKSTONE_DUAL_LASER_PUZZLE = "Lever-Lockstone Dual Laser Puzzle"
    LEVER_LOCKSTONE_TRACKING_BEAM_PUZZLE = "Lever-Lockstone Tracking Beam Puzzle"
    LEVER_LOCKSTONE_VERTICAL_LASER_PUZZLE = "Lever-Lockstone Vertical Laser Puzzle"
    LEVER_LOCKSTONE_NORTH_PUZZLE = "Lever-Lockstone North Puzzle"
    LEVER_LOCKSTONE_SHRINE = "Lever-Lockstone Shrine"
    LEVER_LOCKSTONE_HOOKSHOT_PUZZLE = "Lever-Lockstone Hookshot Puzzle"
    LEVER_LOCKSTONE_UPPER_PUZZLE = "Lever-Lockstone Upper Puzzle"
    LEVER_LOCKSTONE_UPPER_DUAL_LASER_PUZZLE = "Lever-Lockstone Upper Dual Laser Puzzle"
    LEVER_WATCHTOWERS_BEFORE_ICE_ARENA = "Lever-Watchtowers Before Ice Arena"
    LEVER_WATCHTOWERS_AFTER_ICE_SKATING = "Lever-Watchtowers After Ice Skating"
    LEVER_WATCHTOWERS_AFTER_BOOMERS = "Lever-Watchtowers After Boomers"
    LEVER_RUINS_SETTLEMENT_GATE = "Lever-Ruins Settlement Gate"
    LEVER_RUINS_UPPER_DUNGEON_ENTRANCE = "Lever-Ruins Upper Dungeon Entrance"
    LEVER_RUINS_LADDER_LEFT_OF_LORD_OF_DOORS_ARENA = (
        "Lever-Ruins Ladder Left of Lord of Doors Arena"
    )
    LEVER_RUINS_ENTRANCE_LADDER_SHORTCUT = "Lever-Ruins Entrance Ladder Shortcut"
    LEVER_RUINS_MAIN_GATE = "Lever-Ruins Main Gate"
    LEVER_DUNGEON_ENTRANCE_RIGHT_GATE = "Lever-Dungeon Entrance Right Gate"
    LEVER_DUNGEON_ENTRANCE_LEFT_GATE = "Lever-Dungeon Entrance Left Gate"
    LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW = "Lever-Dungeon Above Rightmost Crow"
    LEVER_FORTRESS_BOMB = "Lever-Fortress Bomb"
    LEVER_FORTRESS_MAIN_GATE = "Lever-Fortress Main Gate"
    LEVER_FORTRESS_CENTRAL_SHORTCUT = "Lever-Fortress Central Shortcut"
    LEVER_FORTRESS_STATUE = "Lever-Fortress Statue"
    LEVER_FORTRESS_WATCHTOWER_LOWER = "Lever-Fortress Watchtower Lower"
    LEVER_FORTRESS_BRIDGE = "Lever-Fortress Bridge"
    LEVER_FORTRESS_PRE_MAIN_GATE = "Lever-Fortress Pre-Main Gate"
    LEVER_FORTRESS_WATCHTOWER_UPPER = "Lever-Fortress Watchtower Upper"
    LEVER_FORTRESS_NORTH_WEST = "Lever-Fortress North West"
    LEVER_ESTATE_ELEVATOR_LEFT = "Lever-Estate Elevator Left"
    LEVER_ESTATE_ELEVATOR_RIGHT = "Lever-Estate Elevator Right"
    LEVER_GARDEN_OF_LOVE = "Lever-Garden of Love"
    LEVER_GARDEN_OF_LIFE_END = "Lever-Garden of Life End"
    LEVER_GARDEN_OF_PEACE = "Lever-Garden of Peace"
    LEVER_GARDEN_OF_JOY = "Lever-Garden of Joy"
    LEVER_GARDEN_OF_LOVE_TURNCAM = "Lever-Garden of Love Turncam"
    LEVER_GARDEN_OF_LIFE_LANTERNS = "Lever-Garden of Life Lanterns"
    LEVER_ESTATE_UNDERGROUND_URN_SHED = "Lever-Estate Underground Urn Shed"
    LEVER_MANOR_BIG_POT_ARENA = "Lever-Manor Big Pot Arena"
    LEVER_MANOR_BOOKSHELF_SHORTCUT = "Lever-Manor Bookshelf Shortcut"
    GROVE_OF_SPIRITS_DOOR = "Grove of Spirits Door"
    LOST_CEMETERY_DOOR = "Lost Cemetery Door"
    STRANDED_SAILOR_DOOR = "Stranded Sailor Door"
    CASTLE_LOCKSTONE_DOOR = "Castle Lockstone Door"
    CAMP_OF_THE_FREE_CROWS_DOOR = "Camp of the Free Crows Door"
    OLD_WATCHTOWERS_DOOR = "Old Watchtowers Door"
    BETTYS_LAIR_DOOR = "Betty's Lair Door"
    OVERGROWN_RUINS_DOOR = "Overgrown Ruins Door"
    MUSHROOM_DUNGEON_DOOR = "Mushroom Dungeon Door"
    FLOODED_FORTRESS_DOOR = "Flooded Fortress Door"
    THRONE_OF_THE_FROG_KING_DOOR = "Throne of the Frog King Door"
    ESTATE_OF_THE_URN_WITCH_DOOR = "Estate of the Urn Witch Door"
    CERAMIC_MANOR_DOOR = "Ceramic Manor Door"
    INNER_FURNACE_DOOR = "Inner Furnace Door"
    THE_URN_WITCHS_LABORATORY_DOOR = "The Urn Witch's Laboratory Door"
    GIANT_SOUL_OF_THE_URN_WITCH = "Giant Soul of The Urn Witch"
    GIANT_SOUL_OF_THE_FROG_KING = "Giant Soul of The Frog King"
    GIANT_SOUL_OF_BETTY = "Giant Soul of Betty"
    CROW_MANOR_AFTER_TORCH_PUZZLE = "Crow-Manor After Torch Puzzle"
    CROW_MANOR_IMP_LOFT = "Crow-Manor Imp Loft"
    CROW_MANOR_LIBRARY = "Crow-Manor Library"
    CROW_MANOR_BEDROOM = "Crow-Manor Bedroom"
    CROW_DUNGEON_HALL = "Crow-Dungeon Hall"
    CROW_DUNGEON_WATER_ARENA = "Crow-Dungeon Water Arena"
    CROW_DUNGEON_COBWEB = "Crow-Dungeon Cobweb"
    CROW_DUNGEON_RIGHTMOST = "Crow-Dungeon Rightmost"
    CROW_LOCKSTONE_EAST = "Crow-Lockstone East"
    CROW_LOCKSTONE_WEST = "Crow-Lockstone West"
    CROW_LOCKSTONE_WEST_LOCKED = "Crow-Lockstone West Locked"
    CROW_LOCKSTONE_SOUTH_WEST = "Crow-Lockstone South West"


class DeathsDoorItemData(NamedTuple):
    name: DeathsDoorItemName
    item_id: int
    classification: ItemClassification
    base_quantity_in_item_pool: int
    item_groups: List[ItemGroup]


item_table: List[DeathsDoorItemData] = [
    DeathsDoorItemData(
        DeathsDoorItemName.FIRE, 0, ItemClassification.progression, 2, [ItemGroup.SPELL]
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.BOMB, 0, ItemClassification.progression, 2, [ItemGroup.SPELL]
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.HOOKSHOT,
        0,
        ItemClassification.progression,
        2,
        [ItemGroup.SPELL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.BOW, 0, ItemClassification.progression, 1, [ItemGroup.SPELL]
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ROGUE_DAGGERS,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.DISCARDED_UMBRELLA,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.REAPERS_GREATSWORD,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.THUNDER_HAMMER,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.VITALITY_SHARD, 0, ItemClassification.progression, 8, []
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MAGIC_SHARD, 0, ItemClassification.progression, 8, []
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LIFE_SEED, 0, ItemClassification.progression, 50, []
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SOULS, 0, ItemClassification.progression, 0, []
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.PINK_KEY,
        0,
        ItemClassification.progression,
        5,
        [ItemGroup.KEY],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GREEN_KEY,
        0,
        ItemClassification.progression,
        4,
        [ItemGroup.KEY],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.YELLOW_KEY,
        0,
        ItemClassification.progression,
        3,
        [ItemGroup.KEY],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ENGAGEMENT_RING,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.OLD_COMPASS,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.INCENSE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.UNDYING_BLOSSOM,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.OLD_PHOTOGRAPH,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SLUDGE_FILLED_URN,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.TOKEN_OF_DEATH,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.RUSTY_GARDEN_TROWEL,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CAPTAINS_LOG,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GIANT_ARROWHEAD,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MALFORMED_SEED,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CORRUPTED_ANTLER,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MAGICAL_FOREST_HORN,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ANCIENT_CROWN,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GRUNTS_OLD_MASK,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ANCIENT_DOOR_SCALE_MODEL,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MODERN_DOOR_SCALE_MODEL,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.RUSTY_BELLTOWER_KEY,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SURVEILLANCE_DEVICE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SHINY_MEDALLION,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.INK_COVERED_TEDDY_BEAR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.DEATHS_CONTRACT,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MAKESHIFT_SOUL_KEY,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MYSTERIOUS_LOCKET,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.RED_ANCIENT_TABLET_OF_KNOWLEDGE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GREEN_ANCIENT_TABLET_OF_KNOWLEDGE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CYAN_ANCIENT_TABLET_OF_KNOWLEDGE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.BLUE_ANCIENT_TABLET_OF_KNOWLEDGE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_BOMB_EXIT,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CEMETERY_SEWER,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GUARDIAN_OF_THE_DOOR_ACCESS,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CEMETERY_EAST_TREE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CATACOMBS_TOWER,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CEMETERY_EXIT_TO_ESTATE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CATACOMBS_EXIT,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_HOOKSHOT_SILENT_SERVANT,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_SAILOR_TURNCAM_UPPER,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_SAILOR_TURNCAM_LOWER,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_SAILOR_GREATSWORD_GATE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_EAST_START_SHORTCUT,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_ENTRANCE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_EAST_LOWER,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_UPPER_SHORTCUT,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_DUAL_LASER_PUZZLE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_TRACKING_BEAM_PUZZLE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_VERTICAL_LASER_PUZZLE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_NORTH_PUZZLE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_SHRINE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_HOOKSHOT_PUZZLE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_UPPER_PUZZLE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_UPPER_DUAL_LASER_PUZZLE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_WATCHTOWERS_BEFORE_ICE_ARENA,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_WATCHTOWERS_AFTER_ICE_SKATING,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_WATCHTOWERS_AFTER_BOOMERS,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_SETTLEMENT_GATE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_UPPER_DUNGEON_ENTRANCE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_LADDER_LEFT_OF_LORD_OF_DOORS_ARENA,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_ENTRANCE_LADDER_SHORTCUT,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_MAIN_GATE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_DUNGEON_ENTRANCE_RIGHT_GATE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_DUNGEON_ENTRANCE_LEFT_GATE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_BOMB,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_MAIN_GATE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_CENTRAL_SHORTCUT,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_STATUE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_WATCHTOWER_LOWER,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_BRIDGE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_PRE_MAIN_GATE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_WATCHTOWER_UPPER,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_NORTH_WEST,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_ESTATE_ELEVATOR_LEFT,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_ESTATE_ELEVATOR_RIGHT,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_LOVE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_LIFE_END,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_PEACE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_JOY,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_LOVE_TURNCAM,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_LIFE_LANTERNS,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_ESTATE_UNDERGROUND_URN_SHED,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_MANOR_BIG_POT_ARENA,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_MANOR_BOOKSHELF_SHORTCUT,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GROVE_OF_SPIRITS_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LOST_CEMETERY_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.STRANDED_SAILOR_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CASTLE_LOCKSTONE_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CAMP_OF_THE_FREE_CROWS_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.OLD_WATCHTOWERS_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.BETTYS_LAIR_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.OVERGROWN_RUINS_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MUSHROOM_DUNGEON_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.FLOODED_FORTRESS_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.THRONE_OF_THE_FROG_KING_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ESTATE_OF_THE_URN_WITCH_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CERAMIC_MANOR_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.INNER_FURNACE_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.THE_URN_WITCHS_LABORATORY_DOOR,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GIANT_SOUL_OF_THE_URN_WITCH,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.GIANT_SOUL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GIANT_SOUL_OF_THE_FROG_KING,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.GIANT_SOUL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GIANT_SOUL_OF_BETTY,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.GIANT_SOUL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_MANOR_AFTER_TORCH_PUZZLE,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_MANOR_IMP_LOFT,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_MANOR_LIBRARY,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_MANOR_BEDROOM,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_DUNGEON_HALL,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_DUNGEON_WATER_ARENA,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_DUNGEON_COBWEB,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_DUNGEON_RIGHTMOST,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_LOCKSTONE_EAST,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_LOCKSTONE_WEST,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_LOCKSTONE_WEST_LOCKED,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_LOCKSTONE_SOUTH_WEST,
        0,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
]

item_name_to_id: Dict[str, int] = {data.name.value: data.item_id for data in item_table}

filler_items: List[str] = [
    data.name.value
    for data in item_table
    if data.classification == ItemClassification.filler
]


# Items can be grouped using their names to allow easy checking if any item
# from that group has been collected. Group names can also be used for !hint
def items_for_group(group: ItemGroup) -> Set[str]:
    item_names = set()
    for data in item_table:
        if group in data.item_groups:
            item_names.add(data.name.value)
    return item_names


item_name_groups: Dict[str, Set[str]] = {}
for group in ItemGroup:
    item_name_groups[group.value] = items_for_group(group)
