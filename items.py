from enum import Enum

from typing import NamedTuple
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
    def __str__(self) -> str:
        return self.value

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
    LEVER_BOMB_EXIT = "Hall of Doors Bomb Exit Lever"
    LEVER_CEMETERY_SEWER = "Lost Cemetery Sewer Lever"
    LEVER_GUARDIAN_OF_THE_DOOR_ACCESS = "Lost Cemetery Guardian of the Door Access Lever"
    LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE = "Lost Cemetery Shortcut to East Tree Lever"
    LEVER_CEMETERY_EAST_TREE = "Lost Cemetery East Tree Lever"
    LEVER_CATACOMBS_TOWER = "Lost Cemetery Catacombs Tower Lever"
    LEVER_CEMETERY_EXIT_TO_ESTATE = "Lost Cemetery Exit to Estate Lever"
    LEVER_CATACOMBS_EXIT = "Lost Cemetery Catacombs Exit Lever"
    LEVER_HOOKSHOT_SILENT_SERVANT = "Stranded Sailor Caves Hookshot Silent Servant Lever"
    LEVER_SAILOR_TURNCAM_UPPER = "Stranded Sailor Turncam Upper Lever"
    LEVER_SAILOR_TURNCAM_LOWER = "Stranded Sailor Turncam Lower Lever"
    LEVER_SAILOR_GREATSWORD_GATE = "Stranded Sailor Greatsword Gate Lever"
    LEVER_LOCKSTONE_EAST_START_SHORTCUT = "Castle Lockstone East Start Shortcut Lever"
    LEVER_LOCKSTONE_ENTRANCE = "Castle Lockstone Entrance Lever"
    LEVER_LOCKSTONE_EAST_LOWER = "Castle Lockstone East Lower Lever"
    LEVER_LOCKSTONE_UPPER_SHORTCUT = "Castle Lockstone Upper Shortcut Lever"
    LEVER_LOCKSTONE_DUAL_LASER_PUZZLE = "Castle Lockstone Dual Laser Puzzle Lever"
    LEVER_LOCKSTONE_TRACKING_BEAM_PUZZLE = "Castle Lockstone Tracking Beam Puzzle Lever"
    LEVER_LOCKSTONE_VERTICAL_LASER_PUZZLE = "Castle Lockstone Vertical Laser Puzzle Lever"
    LEVER_LOCKSTONE_NORTH_PUZZLE = "Castle Lockstone North Puzzle Lever"
    LEVER_LOCKSTONE_SHRINE = "Castle Lockstone Shrine Lever"
    LEVER_LOCKSTONE_HOOKSHOT_PUZZLE = "Castle Lockstone Hookshot Puzzle Lever"
    LEVER_LOCKSTONE_UPPER_PUZZLE = "Castle Lockstone Upper Puzzle Lever"
    LEVER_LOCKSTONE_UPPER_DUAL_LASER_PUZZLE = "Castle Lockstone Upper Dual Laser Puzzle Lever"
    LEVER_WATCHTOWERS_BEFORE_ICE_ARENA = "Old Watchtowers Before Ice Arena Lever"
    LEVER_WATCHTOWERS_AFTER_ICE_SKATING = "Old Watchtowers After Ice Skating Lever"
    LEVER_WATCHTOWERS_AFTER_BOOMERS = "Old Watchtowers After Boomers Lever"
    LEVER_RUINS_SETTLEMENT_GATE = "Overgrown Ruins Settlement Gate Lever"
    LEVER_RUINS_UPPER_DUNGEON_ENTRANCE = "Overgrown Ruins Upper Dungeon Entrance Lever"
    LEVER_RUINS_LADDER_LEFT_OF_LORD_OF_DOORS_ARENA = (
        "Overgrown Ruins Ladder Left of Lord of Doors Arena Lever"
    )
    LEVER_RUINS_ENTRANCE_LADDER_SHORTCUT = "Overgrown Ruins Entrance Ladder Shortcut Lever"
    LEVER_RUINS_MAIN_GATE = "Overgrown Ruins Main Gate Lever"
    LEVER_DUNGEON_ENTRANCE_RIGHT_GATE = "Mushroom Dungeon Entrance Right Gate Lever"
    LEVER_DUNGEON_ENTRANCE_LEFT_GATE = "Mushroom Dungeon Entrance Left Gate Lever"
    LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW = "Mushroom Dungeon Above Rightmost Crow Lever"
    LEVER_FORTRESS_BOMB = "Flooded Fortress Bomb Lever"
    LEVER_FORTRESS_MAIN_GATE = "Flooded Fortress Main Gate Lever"
    LEVER_FORTRESS_CENTRAL_SHORTCUT = "Flooded Fortress Central Shortcut Lever"
    LEVER_FORTRESS_STATUE = "Flooded Fortress Statue Lever"
    LEVER_FORTRESS_WATCHTOWER_LOWER = "Flooded Fortress Watchtower Lower Lever"
    LEVER_FORTRESS_BRIDGE = "Flooded Fortress Bridge Lever"
    LEVER_FORTRESS_PRE_MAIN_GATE = "Flooded Fortress Pre-Main Gate Lever"
    LEVER_FORTRESS_WATCHTOWER_UPPER = "Flooded Fortress Watchtower Upper Lever"
    LEVER_FORTRESS_NORTH_WEST = "Flooded Fortress North West Lever"
    LEVER_ESTATE_ELEVATOR_LEFT = "Estate of the Urn Witch Elevator Left Lever"
    LEVER_ESTATE_ELEVATOR_RIGHT = "Estate of the Urn Witch Elevator Right Lever"
    LEVER_GARDEN_OF_LOVE = "Garden of Love Lever"
    LEVER_GARDEN_OF_LIFE_END = "Garden of Life End Lever"
    LEVER_GARDEN_OF_PEACE = "Garden of Peace Lever"
    LEVER_GARDEN_OF_JOY = "Garden of Joy Lever"
    LEVER_GARDEN_OF_LOVE_TURNCAM = "Garden of Love Turncam Lever"
    LEVER_GARDEN_OF_LIFE_LANTERNS = "Garden of Life Lanterns Lever"
    LEVER_ESTATE_UNDERGROUND_URN_SHED = "Estate of the Urn Witch Underground Urn Shed Lever"
    LEVER_MANOR_BIG_POT_ARENA = "Ceramic Manor Big Pot Arena Lever"
    LEVER_MANOR_BOOKSHELF_SHORTCUT = "Ceramic Manor Bookshelf Shortcut Lever"
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
    CROW_MANOR_AFTER_TORCH_PUZZLE = "Ceramic Manor After Torch Puzzle Crow"
    CROW_MANOR_IMP_LOFT = "Ceramic Manor Imp Loft Crow"
    CROW_MANOR_LIBRARY = "Ceramic Manor Library Crow"
    CROW_MANOR_BEDROOM = "Ceramic Manor Bedroom Crow"
    CROW_DUNGEON_HALL = "Mushroom Dungeon Hall Crow"
    CROW_DUNGEON_WATER_ARENA = "Mushroom Dungeon Water Arena Crow"
    CROW_DUNGEON_COBWEB = "Mushroom Dungeon Cobweb Crow"
    CROW_DUNGEON_RIGHTMOST = "Mushroom Dungeon Rightmost Crow"
    CROW_LOCKSTONE_EAST = "Castle Lockstone East Crow"
    CROW_LOCKSTONE_WEST = "Castle Lockstone West Crow"
    CROW_LOCKSTONE_WEST_LOCKED = "Castle Lockstone West Locked Crow"
    CROW_LOCKSTONE_SOUTH_WEST = "Castle Lockstone South West Crow"


class DeathsDoorItemData(NamedTuple):
    name: DeathsDoorItemName
    item_id: int
    classification: ItemClassification
    base_quantity_in_item_pool: int
    item_groups: list[ItemGroup]


item_table: list[DeathsDoorItemData] = [
    DeathsDoorItemData(
        DeathsDoorItemName.LIFE_SEED,
        1,
        ItemClassification.progression_skip_balancing,
        50,
        [],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.FIRE,
        2,
        ItemClassification.progression,
        2,
        [ItemGroup.SPELL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.BOMB,
        3,
        ItemClassification.progression,
        2,
        [ItemGroup.SPELL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.HOOKSHOT,
        4,
        ItemClassification.progression,
        2,
        [ItemGroup.SPELL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.BOW,
        5,
        ItemClassification.useful,
        1,
        [ItemGroup.SPELL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ROGUE_DAGGERS,
        6,
        ItemClassification.useful,
        1,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.DISCARDED_UMBRELLA,
        7,
        ItemClassification.useful,
        1,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.REAPERS_GREATSWORD,
        8,
        ItemClassification.useful,
        1,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.THUNDER_HAMMER,
        9,
        ItemClassification.useful,
        1,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.VITALITY_SHARD,
        10,
        ItemClassification.useful,
        8,
        [],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MAGIC_SHARD,
        11,
        ItemClassification.useful,
        8,
        [],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SOULS,
        12,
        ItemClassification.filler,
        0,
        [],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.PINK_KEY,
        13,
        ItemClassification.progression,
        5,
        [ItemGroup.KEY],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GREEN_KEY,
        14,
        ItemClassification.progression,
        4,
        [ItemGroup.KEY],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.YELLOW_KEY,
        15,
        ItemClassification.progression,
        3,
        [ItemGroup.KEY],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ENGAGEMENT_RING,
        16,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.OLD_COMPASS,
        17,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.INCENSE,
        18,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.UNDYING_BLOSSOM,
        19,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.OLD_PHOTOGRAPH,
        20,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SLUDGE_FILLED_URN,
        21,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.TOKEN_OF_DEATH,
        22,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.RUSTY_GARDEN_TROWEL,
        23,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CAPTAINS_LOG,
        24,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GIANT_ARROWHEAD,
        25,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MALFORMED_SEED,
        26,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CORRUPTED_ANTLER,
        27,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MAGICAL_FOREST_HORN,
        28,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ANCIENT_CROWN,
        29,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GRUNTS_OLD_MASK,
        30,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ANCIENT_DOOR_SCALE_MODEL,
        31,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MODERN_DOOR_SCALE_MODEL,
        32,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.RUSTY_BELLTOWER_KEY,
        33,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SURVEILLANCE_DEVICE,
        34,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SHINY_MEDALLION,
        35,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.INK_COVERED_TEDDY_BEAR,
        36,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.DEATHS_CONTRACT,
        37,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MAKESHIFT_SOUL_KEY,
        38,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MYSTERIOUS_LOCKET,
        39,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.RED_ANCIENT_TABLET_OF_KNOWLEDGE,
        40,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE,
        41,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GREEN_ANCIENT_TABLET_OF_KNOWLEDGE,
        42,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CYAN_ANCIENT_TABLET_OF_KNOWLEDGE,
        43,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.BLUE_ANCIENT_TABLET_OF_KNOWLEDGE,
        44,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE,
        45,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_BOMB_EXIT,
        46,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CEMETERY_SEWER,
        47,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GUARDIAN_OF_THE_DOOR_ACCESS,
        48,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE,
        49,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CEMETERY_EAST_TREE,
        50,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CATACOMBS_TOWER,
        51,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CEMETERY_EXIT_TO_ESTATE,
        52,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CATACOMBS_EXIT,
        53,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_HOOKSHOT_SILENT_SERVANT,
        54,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_SAILOR_TURNCAM_UPPER,
        55,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_SAILOR_TURNCAM_LOWER,
        56,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_SAILOR_GREATSWORD_GATE,
        57,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_EAST_START_SHORTCUT,
        58,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_ENTRANCE,
        59,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_EAST_LOWER,
        60,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_UPPER_SHORTCUT,
        61,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_DUAL_LASER_PUZZLE,
        62,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_TRACKING_BEAM_PUZZLE,
        63,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_VERTICAL_LASER_PUZZLE,
        64,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_NORTH_PUZZLE,
        65,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_SHRINE,
        66,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_HOOKSHOT_PUZZLE,
        67,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_UPPER_PUZZLE,
        68,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_UPPER_DUAL_LASER_PUZZLE,
        69,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_WATCHTOWERS_BEFORE_ICE_ARENA,
        70,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_WATCHTOWERS_AFTER_ICE_SKATING,
        71,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_WATCHTOWERS_AFTER_BOOMERS,
        72,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_SETTLEMENT_GATE,
        73,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_UPPER_DUNGEON_ENTRANCE,
        74,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_LADDER_LEFT_OF_LORD_OF_DOORS_ARENA,
        75,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_ENTRANCE_LADDER_SHORTCUT,
        76,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_MAIN_GATE,
        77,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_DUNGEON_ENTRANCE_RIGHT_GATE,
        78,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_DUNGEON_ENTRANCE_LEFT_GATE,
        79,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW,
        80,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_BOMB,
        81,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_MAIN_GATE,
        82,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_CENTRAL_SHORTCUT,
        83,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_STATUE,
        84,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_WATCHTOWER_LOWER,
        85,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_BRIDGE,
        86,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_PRE_MAIN_GATE,
        87,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_WATCHTOWER_UPPER,
        88,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_NORTH_WEST,
        89,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_ESTATE_ELEVATOR_LEFT,
        90,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_ESTATE_ELEVATOR_RIGHT,
        91,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_LOVE,
        92,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_LIFE_END,
        93,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_PEACE,
        94,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_JOY,
        95,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_LOVE_TURNCAM,
        96,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_LIFE_LANTERNS,
        97,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_ESTATE_UNDERGROUND_URN_SHED,
        98,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_MANOR_BIG_POT_ARENA,
        99,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_MANOR_BOOKSHELF_SHORTCUT,
        100,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GROVE_OF_SPIRITS_DOOR,
        101,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LOST_CEMETERY_DOOR,
        102,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.STRANDED_SAILOR_DOOR,
        103,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CASTLE_LOCKSTONE_DOOR,
        104,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CAMP_OF_THE_FREE_CROWS_DOOR,
        105,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.OLD_WATCHTOWERS_DOOR,
        106,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.BETTYS_LAIR_DOOR,
        107,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.OVERGROWN_RUINS_DOOR,
        108,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MUSHROOM_DUNGEON_DOOR,
        109,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.FLOODED_FORTRESS_DOOR,
        110,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.THRONE_OF_THE_FROG_KING_DOOR,
        111,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ESTATE_OF_THE_URN_WITCH_DOOR,
        112,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CERAMIC_MANOR_DOOR,
        113,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.INNER_FURNACE_DOOR,
        114,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.THE_URN_WITCHS_LABORATORY_DOOR,
        115,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GIANT_SOUL_OF_THE_URN_WITCH,
        116,
        ItemClassification.progression,
        1,
        [ItemGroup.GIANT_SOUL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GIANT_SOUL_OF_THE_FROG_KING,
        117,
        ItemClassification.progression,
        1,
        [ItemGroup.GIANT_SOUL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GIANT_SOUL_OF_BETTY,
        118,
        ItemClassification.progression,
        1,
        [ItemGroup.GIANT_SOUL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_MANOR_AFTER_TORCH_PUZZLE,
        119,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_MANOR_IMP_LOFT,
        120,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_MANOR_LIBRARY,
        121,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_MANOR_BEDROOM,
        122,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_DUNGEON_HALL,
        123,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_DUNGEON_WATER_ARENA,
        124,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_DUNGEON_COBWEB,
        125,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_DUNGEON_RIGHTMOST,
        126,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_LOCKSTONE_EAST,
        127,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_LOCKSTONE_WEST,
        128,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_LOCKSTONE_WEST_LOCKED,
        129,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_LOCKSTONE_SOUTH_WEST,
        130,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
]


item_name_to_id: dict[str, int] = {data.name.value: data.item_id for data in item_table}


# Items can be grouped using their names to allow easy checking if any item
# from that group has been collected. Group names can also be used for !hint
def items_for_group(group: ItemGroup) -> set[str]:
    item_names = set()
    for data in item_table:
        if group in data.item_groups:
            item_names.add(data.name.value)
    return item_names


item_name_groups: dict[str, set[str]] = {}
for group in ItemGroup:
    item_name_groups[group.value] = items_for_group(group)
