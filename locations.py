from enum import Enum, auto
from typing import Dict, NamedTuple, Set, List

from .regions import DeathsDoorRegionName as R


class LocationGroup(Enum):
    SPELL = "Spell"
    WEAPON = "Weapon"
    GIANT_SOUL = "Giant Soul"
    SHRINE = "Shrine"
    SHINY_THING = "Shiny Thing"
    SEED = "Seed"
    SOUL_ORB = "Soul Orb"
    TABLET = "Tablet"
    LEVER = "Lever"
    DOOR = "Door"
    KEY = "Key"
    LOST_CROW = "Lost Crow"


class DeathsDoorLocationName(str, Enum):
    # Spells and their upgrades
    FIRE_AVARICE = "Fire Avarice"
    BOMB_AVARICE = "Bomb Avarice"
    HOOKSHOT_AVARICE = "Hookshot Avarice"
    FIRE_SILENT_SERVANT = "Fire Silent Servant"
    BOMB_SILENT_SERVANT = "Bomb Silent Servant"
    HOOKSHOT_SILENT_SERVANT = "Hookshot Silent Servant"
    ARROW_SILENT_SERVANT = "Arrow Silent Servant"

    # Weapons
    ROGUE_DAGGERS = "Rogue Daggers"
    DISCARDED_UMBRELLA = "Discarded Umbrella"
    REAPERS_GREATSWORD = "Reaper's Greatsword"
    THUNDER_HAMMER = "Thunder Hammer"

    # Giant Souls
    BETTY = "Betty"
    FROG_KING = "Frog King"
    GRANDMA = "Grandma"

    # Shrines
    HEART_SHRINE_CEMETERY_BEHIND_ENTRANCE = "Heart Shrine-Cemetery Behind Entrance"
    MAGIC_SHRINE_CEMETERY_AFTER_SMOUGH_ARENA = (
        "Magic Shrine-Cemetery After Smough Arena"
    )
    HEART_SHRINE_CEMETERY_WINDING_BRIDGE_END = (
        "Heart Shrine-Cemetery Winding Bridge End"
    )
    HEART_SHRINE_HOOKSHOT_ARENA = "Heart Shrine-Hookshot Arena"
    MAGIC_SHRINE_SAILOR_TURNCAM = "Magic Shrine-Sailor Turncam"
    MAGIC_SHRINE_LOCKSTONE_SECRET_WEST = "Magic Shrine-Lockstone Secret West"
    HEART_SHRINE_CAMP_ICE_SKATING = "Heart Shrine-Camp Ice Skating"
    MAGIC_SHRINE_RUINS_HOOKSHOT_ARENA = "Magic Shrine-Ruins Hookshot Arena"
    MAGIC_SHRINE_RUINS_TURNCAM = "Magic Shrine-Ruins Turncam"
    HEART_SHRINE_DUNGEON_WATER_ARENA = "Heart Shrine-Dungeon Water Arena"
    HEART_SHRINE_RUINS_SEWER = "Heart Shrine-Ruins Sewer"
    MAGIC_SHRINE_FORTRESS_BOW_SECRET = "Magic Shrine-Fortress Bow Secret"
    MAGIC_SHRINE_ESTATE_LEFT_OF_MANOR = "Magic Shrine-Estate Left of Manor"
    HEART_SHRINE_GARDEN_OF_LIFE = "Heart Shrine-Garden of Life"
    MAGIC_SHRINE_MANOR_BATHROOM_PUZZLE = "Magic Shrine-Manor Bathroom Puzzle"
    HEART_SHRINE_FURNACE_CART_PUZZLE = "Heart Shrine-Furnace Cart Puzzle"

    # Shiny Things
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

    # Seeds
    SEED_CEMETERY_BROKEN_BRIDGE = "Seed-Cemetery Broken Bridge"
    SEED_CATACOMBS_TOWER = "Seed-Catacombs Tower"
    SEED_CEMETERY_LEFT_OF_MAIN_ENTRANCE = "Seed-Cemetery Left of Main Entrance"
    SEED_CEMETERY_NEAR_TABLET_GATE = "Seed-Cemetery Near Tablet Gate"
    SEED_BETWEEN_CEMETERY_AND_SAILOR = "Seed-Between Cemetery and Sailor"
    SEED_SAILOR_UPPER = "Seed-Sailor Upper"
    SEED_LOCKSTONE_UPPER_EAST = "Seed-Lockstone Upper East"
    SEED_LOCKSTONE_SOUL_DOOR = "Seed-Lockstone Soul Door"
    SEED_LOCKSTONE_BEHIND_BARS = "Seed-Lockstone Behind Bars"
    SEED_LOCKSTONE_ENTRANCE_WEST = "Seed-Lockstone Entrance West"
    SEED_LOCKSTONE_NORTH = "Seed-Lockstone North"
    SEED_CAMP_LEDGE_WITH_HUTS = "Seed-Camp Ledge With Huts"
    SEED_CAMP_STALL = "Seed-Camp Stall"
    SEED_CAMP_ROOFTOPS = "Seed-Camp Rooftops"
    SEED_WATCHTOWERS_ICE_SKATING = "Seed-Watchtowers Ice Skating"
    SEED_WATCHTOWERS_TABLET_DOOR = "Seed-Watchtowers Tablet Door"
    SEED_WATCHTOWERS_ARCHER_PLATFORM = "Seed-Watchtowers Archer Platform"
    SEED_WATCHTOWERS_BOXES = "Seed-Watchtowers Boxes"
    SEED_DUNGEON_FIRE_PUZZLE_NEAR_WATER_ARENA = (
        "Seed-Dungeon Fire Puzzle Near Water Arena"
    )
    SEED_RUINS_LORD_OF_DOORS_ARENA = "Seed-Ruins Lord of Doors Arena"
    SEED_RUINS_FIRE_PLANT_CORRIDOR = "Seed-Ruins Fire Plant Corridor"
    SEED_DUNGEON_WATER_ARENA_LEFT_EXIT = "Seed-Dungeon Water Arena Left Exit"
    SEED_RUINS_RIGHT_MIDDLE = "Seed-Ruins Right Middle"
    SEED_RUINS_ON_SETTLEMENT_WALL = "Seed-Ruins On Settlement Wall"
    SEED_RUINS_BEHIND_BOXES = "Seed-Ruins Behind Boxes"
    SEED_RUINS_DOWN_THROUGH_BOMB_WALL = "Seed-Ruins Down Through Bomb Wall"
    SEED_DUNGEON_ABOVE_RIGHTMOST_CROW = "Seed-Dungeon Above Rightmost Crow"
    SEED_DUNGEON_RIGHT_ABOVE_KEY = "Seed-Dungeon Right Above Key"
    SEED_DUNGEON_AVARICE_BRIDGE = "Seed-Dungeon Avarice Bridge"
    SEED_FORTRESS_WATCHTOWER = "Seed-Fortress Watchtower"
    SEED_FORTRESS_STATUE = "Seed-Fortress Statue"
    SEED_FORTRESS_BRIDGE = "Seed-Fortress Bridge"
    SEED_FORTRESS_INTRO_CRATE = "Seed-Fortress Intro Crate"
    SEED_FORTRESS_EAST_AFTER_STATUE = "Seed-Fortress East After Statue"
    SEED_ESTATE_FAMILY_TOMB = "Seed-Estate Family Tomb"
    SEED_ESTATE_ENTRANCE = "Seed-Estate Entrance"
    SEED_ESTATE_HEDGE_GAPS = "Seed-Estate Hedge Gaps"
    SEED_GARDEN_OF_JOY = "Seed-Garden of Joy"
    SEED_MANOR_BOXES = "Seed-Manor Boxes"
    SEED_MANOR_NEAR_BRAZIER = "Seed-Manor Near Brazier"
    SEED_MANOR_BELOW_BIG_POT_ARENA = "Seed-Manor Below Big Pot Arena"
    SEED_MANOR_RAFTERS = "Seed-Manor Rafters"
    SEED_MANOR_MAIN_ROOM_UPPER = "Seed-Manor Main Room Upper"
    SEED_MANOR_SPINNY_POT_ROOM = "Seed-Manor Spinny Pot Room"
    SEED_MANOR_LIBRARY_SHELF = "Seed-Manor Library Shelf"
    SEED_CART_PUZZLE = "Seed-Cart Puzzle"
    SEED_FURNACE_ENTRANCE = "Seed-Furnace Entrance"
    SEED_INNER_FURNACE_HORIZONTAL_PISTONS = "Seed-Inner Furnace Horizontal Pistons"
    SEED_INNER_FURNACE_CONVEYOR_BRIDGE = "Seed-Inner Furnace Conveyor Bridge"
    SEED_INNER_FURNACE_CONVEYOR_GAUNTLET = "Seed-Inner Furnace Conveyor Gauntlet"

    # Soul Orbs
    SOUL_ORB_FIRE_RETURN_UPPER = "Soul Orb-Fire Return Upper"
    SOUL_ORB_HOOKSHOT_SECRET = "Soul Orb-Hookshot Secret"
    SOUL_ORB_BOMB_RETURN = "Soul Orb-Bomb Return"
    SOUL_ORB_BOMB_SECRET = "Soul Orb-Bomb Secret"
    SOUL_ORB_HOOKSHOT_RETURN = "Soul Orb-Hookshot Return"
    SOUL_ORB_FIRE_RETURN_LOWER = "Soul Orb-Fire Return Lower"
    SOUL_ORB_FIRE_SECRET = "Soul Orb-Fire Secret"
    SOUL_ORB_CATACOMBS_EXIT = "Soul Orb-Catacombs Exit"
    SOUL_ORB_CEMETERY_HOOKSHOT_TOWERS = "Soul Orb-Cemetery Hookshot Towers"
    SOUL_ORB_CEMETERY_UNDER_BRIDGE = "Soul Orb-Cemetery Under Bridge"
    SOUL_ORB_CEMETERY_EAST_TREE = "Soul Orb-Cemetery East Tree"
    SOUL_ORB_CEMETERY_WINDING_BRIDGE_END = "Soul Orb-Cemetery Winding Bridge End"
    SOUL_ORB_CATACOMBS_ROOM_2 = "Soul Orb-Catacombs Room 2"
    SOUL_ORB_CATACOMBS_ROOM_1 = "Soul Orb-Catacombs Room 1"
    SOUL_ORB_CEMETERY_GATED_SEWER = "Soul Orb-Cemetery Gated Sewer"
    SOUL_ORB_CATACOMBS_ENTRANCE = "Soul Orb-Catacombs Entrance"
    SOUL_ORB_CEMETERY_CAVE = "Soul Orb-Cemetery Cave"
    SOUL_ORB_SAILOR_TURNCAM = "Soul Orb-Sailor Turncam"
    SOUL_ORB_NORTH_LOCKSTONE_SEWER = "Soul Orb-North Lockstone Sewer"
    SOUL_ORB_LOCKSTONE_HOOKSHOT_NORTH = "Soul Orb-Lockstone Hookshot North"
    SOUL_ORB_LOCKSTONE_EXIT = "Soul Orb-Lockstone Exit"
    SOUL_ORB_WEST_LOCKSTONE_SEWER = "Soul Orb-West Lockstone Sewer"
    SOUL_ORB_CAMP_ROOFTOPS = "Soul Orb-Camp Rooftops"
    SOUL_ORB_CAMP_BROKEN_BRIDGE = "Soul Orb-Camp Broken Bridge"
    SOUL_ORB_WATCHTOWERS_BEHIND_BARB_ELEVATOR = (
        "Soul Orb-Watchtowers Behind Barb Elevator"
    )
    SOUL_ORB_DUNGEON_VINE = "Soul Orb-Dungeon Vine"
    SOUL_ORB_RUINS_STUMP = "Soul Orb-Ruins Stump"
    SOUL_ORB_RUINS_OUTSIDE_LEFT_DUNGEON_EXIT = (
        "Soul Orb-Ruins Outside Left Dungeon Exit"
    )
    SOUL_ORB_DUNGEON_COBWEB = "Soul Orb-Dungeon Cobweb"
    SOUL_ORB_RUINS_LEFT_AFTER_KEY_DOOR = "Soul Orb-Ruins Left After Key Door"
    SOUL_ORB_RUINS_LOWER_BOMB_WALL = "Soul Orb-Ruins Lower Bomb Wall"
    SOUL_ORB_RUINS_LORD_OF_DOORS_ARENA_HOOKSHOT = (
        "Soul Orb-Ruins Lord of Doors Arena Hookshot"
    )
    SOUL_ORB_DUNGEON_LOWER_ENTRANCE = "Soul Orb-Dungeon Lower Entrance"
    SOUL_ORB_RUINS_UPPER_ABOVE_HORN = "Soul Orb-Ruins Upper Above Horn"
    SOUL_ORB_RUINS_ABOVE_THREE_PLANTS = "Soul Orb-Ruins Above Three Plants"
    SOUL_ORB_RUINS_UP_TURNCAM_LADDER = "Soul Orb-Ruins Up Turncam Ladder"
    SOUL_ORB_RUINS_ABOVE_ENTRANCE_GATE = "Soul Orb-Ruins Above Entrance Gate"
    SOUL_ORB_RUINS_UPPER_BOMB_WALL = "Soul Orb-Ruins Upper Bomb Wall"
    SOUL_ORB_DUNGEON_LEFT_EXIT_SHELF = "Soul Orb-Dungeon Left Exit Shelf"
    SOUL_ORB_RUINS_LOWER_HOOKSHOT = "Soul Orb-Ruins Lower Hookshot"
    SOUL_ORB_FORTRESS_BOMB = "Soul Orb-Fortress Bomb"
    SOUL_ORB_FORTRESS_HIDDEN_SEWER = "Soul Orb-Fortress Hidden Sewer"
    SOUL_ORB_FORTRESS_DROP = "Soul Orb-Fortress Drop"
    SOUL_ORB_ESTATE_ACCESS_CRYPT = "Soul Orb-Estate Access Crypt"
    SOUL_ORB_ESTATE_BALCONY = "Soul Orb-Estate Balcony"
    SOUL_ORB_GARDEN_OF_LOVE_TURNCAM = "Soul Orb-Garden of Love Turncam"
    SOUL_ORB_GARDEN_OF_LIFE_HOOKSHOT_LOOP = "Soul Orb-Garden of Life Hookshot Loop"
    SOUL_ORB_GARDEN_OF_LOVE_BOMB_WALLS = "Soul Orb-Garden of Love Bomb Walls"
    SOUL_ORB_GARDEN_OF_LIFE_BOMB_WALL = "Soul Orb-Garden of Life Bomb Wall"
    SOUL_ORB_ESTATE_BROKEN_BOARDWALK = "Soul Orb-Estate Broken Boardwalk"
    SOUL_ORB_ESTATE_SECRET_CAVE = "Soul Orb-Estate Secret Cave"
    SOUL_ORB_ESTATE_TWIN_BENCHES = "Soul Orb-Estate Twin Benches"
    SOUL_ORB_ESTATE_SEWER_MIDDLE = "Soul Orb-Estate Sewer Middle"
    SOUL_ORB_ESTATE_SEWER_END = "Soul Orb-Estate Sewer End"
    SOUL_ORB_GARDEN_OF_PEACE = "Soul Orb-Garden of Peace"
    SOUL_ORB_MANOR_IMP_LOFT = "Soul Orb-Manor Imp Loft"
    SOUL_ORB_MANOR_LIBRARY_SHELF = "Soul Orb-Manor Library Shelf"
    SOUL_ORB_MANOR_CHANDELIER = "Soul Orb-Manor Chandelier"
    SOUL_ORB_FURNACE_LANTERN_CHAIN = "Soul Orb-Furnace Lantern Chain"
    SOUL_ORB_SMALL_ROOM = "Soul Orb-Small Room"
    SOUL_ORB_FURNACE_ENTRANCE_SEWER = "Soul Orb-Furnace Entrance Sewer"

    # Tablets
    RED_ANCIENT_TABLET_OF_KNOWLEDGE = "Red Ancient Tablet of Knowledge"
    YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE = "Yellow Ancient Tablet of Knowledge"
    GREEN_ANCIENT_TABLET_OF_KNOWLEDGE = "Green Ancient Tablet of Knowledge"
    CYAN_ANCIENT_TABLET_OF_KNOWLEDGE = "Cyan Ancient Tablet of Knowledge"
    BLUE_ANCIENT_TABLET_OF_KNOWLEDGE = "Blue Ancient Tablet of Knowledge"
    PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE = "Purple Ancient Tablet of Knowledge"
    ESTATE_OWL = "Estate Owl"
    RUINS_OWL = "Ruins Owl"
    WATCHTOWERS_OWL = "Watchtowers Owl"

    # Levers
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

    # Doors
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

    # Keys
    KEY_CEMETERY_CENTRAL = "Key-Cemetery Central"
    KEY_CEMETERY_GREY_CROW = "Key-Cemetery Grey Crow"
    KEY_CAMP_OF_THE_FREE_CROWS = "Key-Camp of the Free Crows"
    KEY_LOCKSTONE_WEST = "Key-Lockstone West"
    KEY_LOCKSTONE_NORTH = "Key-Lockstone North"
    KEY_OVERGROWN_RUINS = "Key-Overgrown Ruins"
    KEY_DUNGEON_HALL = "Key-Dungeon Hall"
    KEY_DUNGEON_RIGHT = "Key-Dungeon Right"
    KEY_DUNGEON_NEAR_WATER_ARENA = "Key-Dungeon Near Water Arena"
    KEY_MANOR_UNDER_DINING_ROOM = "Key-Manor Under Dining Room"
    KEY_MANOR_AFTER_SPINNY_POT_ROOM = "Key-Manor After Spinny Pot Room"
    KEY_MANOR_LIBRARY = "Key-Manor Library"

    # Crow Souls
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


class DeathsDoorLocationData(NamedTuple):
    name: DeathsDoorLocationName
    location_id: int
    region: R
    location_groups: List[LocationGroup]


location_table: List[DeathsDoorLocationData] = [
    # Spells and their upgrades
    DeathsDoorLocationData(
        DeathsDoorLocationName.FIRE_AVARICE, 0, R.HALL_OF_DOORS, [LocationGroup.SPELL]
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.BOMB_AVARICE, 0, R.HALL_OF_DOORS, [LocationGroup.SPELL]
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HOOKSHOT_AVARICE,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.SPELL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.FIRE_SILENT_SERVANT,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SPELL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.BOMB_SILENT_SERVANT,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SPELL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HOOKSHOT_SILENT_SERVANT,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SPELL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ARROW_SILENT_SERVANT,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SPELL],
    ),
    # Weapons
    DeathsDoorLocationData(
        DeathsDoorLocationName.ROGUE_DAGGERS,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.WEAPON],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.DISCARDED_UMBRELLA,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.WEAPON],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.REAPERS_GREATSWORD,
        0,
        R.STRANDED_SAILOR,
        [LocationGroup.WEAPON],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.THUNDER_HAMMER,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.WEAPON],
    ),
    # Giant Souls
    DeathsDoorLocationData(
        DeathsDoorLocationName.BETTY, 0, R.BETTYS_LAIR, [LocationGroup.GIANT_SOUL]
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.FROG_KING,
        0,
        R.THRONE_OF_THE_FROG_KING,
        [LocationGroup.GIANT_SOUL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.GRANDMA,
        0,
        R.URN_WITCHS_LABORATORY,
        [LocationGroup.GIANT_SOUL],
    ),
    # Shrines
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_CEMETERY_BEHIND_ENTRANCE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_CEMETERY_AFTER_SMOUGH_ARENA,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_CEMETERY_WINDING_BRIDGE_END,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_HOOKSHOT_ARENA,
        0,
        R.STRANDED_SAILOR,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_SAILOR_TURNCAM,
        0,
        R.STRANDED_SAILOR,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_LOCKSTONE_SECRET_WEST,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_CAMP_ICE_SKATING,
        0,
        R.CAMP_OF_THE_FREE_CROWS,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_RUINS_HOOKSHOT_ARENA,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_RUINS_TURNCAM,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_DUNGEON_WATER_ARENA,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_RUINS_SEWER,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_FORTRESS_BOW_SECRET,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_ESTATE_LEFT_OF_MANOR,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_GARDEN_OF_LIFE,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_MANOR_BATHROOM_PUZZLE,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_FURNACE_CART_PUZZLE,
        0,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SHRINE],
    ),
    # Shiny Things
    DeathsDoorLocationData(
        DeathsDoorLocationName.ENGAGEMENT_RING,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.OLD_COMPASS,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.INCENSE, 0, R.LOST_CEMETERY, [LocationGroup.SHINY_THING]
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.UNDYING_BLOSSOM,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.OLD_PHOTOGRAPH,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SLUDGE_FILLED_URN,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.TOKEN_OF_DEATH,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.RUSTY_GARDEN_TROWEL,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CAPTAINS_LOG,
        0,
        R.STRANDED_SAILOR,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.GIANT_ARROWHEAD,
        0,
        R.THRONE_OF_THE_FROG_KING,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MALFORMED_SEED,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CORRUPTED_ANTLER,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGICAL_FOREST_HORN,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ANCIENT_CROWN,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.GRUNTS_OLD_MASK,
        0,
        R.STRANDED_SAILOR,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ANCIENT_DOOR_SCALE_MODEL,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MODERN_DOOR_SCALE_MODEL,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.RUSTY_BELLTOWER_KEY,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SURVEILLANCE_DEVICE,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SHINY_MEDALLION,
        0,
        R.CAMP_OF_THE_FREE_CROWS,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.INK_COVERED_TEDDY_BEAR,
        0,
        R.STRANDED_SAILOR,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.DEATHS_CONTRACT,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAKESHIFT_SOUL_KEY,
        0,
        R.GROVE_OF_SPIRITS,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MYSTERIOUS_LOCKET,
        0,
        R.OLD_WATCHTOWERS,
        [LocationGroup.SHINY_THING],
    ),
    # Seeds
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CEMETERY_BROKEN_BRIDGE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CATACOMBS_TOWER,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CEMETERY_LEFT_OF_MAIN_ENTRANCE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CEMETERY_NEAR_TABLET_GATE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_BETWEEN_CEMETERY_AND_SAILOR,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_SAILOR_UPPER,
        0,
        R.STRANDED_SAILOR,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_UPPER_EAST,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_SOUL_DOOR,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_BEHIND_BARS,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_ENTRANCE_WEST,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_NORTH,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CAMP_LEDGE_WITH_HUTS,
        0,
        R.CAMP_OF_THE_FREE_CROWS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CAMP_STALL,
        0,
        R.CAMP_OF_THE_FREE_CROWS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CAMP_ROOFTOPS,
        0,
        R.CAMP_OF_THE_FREE_CROWS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_WATCHTOWERS_ICE_SKATING,
        0,
        R.OLD_WATCHTOWERS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_WATCHTOWERS_TABLET_DOOR,
        0,
        R.OLD_WATCHTOWERS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_WATCHTOWERS_ARCHER_PLATFORM,
        0,
        R.OLD_WATCHTOWERS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_WATCHTOWERS_BOXES,
        0,
        R.OLD_WATCHTOWERS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_FIRE_PUZZLE_NEAR_WATER_ARENA,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_LORD_OF_DOORS_ARENA,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_FIRE_PLANT_CORRIDOR,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_WATER_ARENA_LEFT_EXIT,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_RIGHT_MIDDLE,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_ON_SETTLEMENT_WALL,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_BEHIND_BOXES,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_DOWN_THROUGH_BOMB_WALL,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_ABOVE_RIGHTMOST_CROW,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_RIGHT_ABOVE_KEY,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_AVARICE_BRIDGE,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_WATCHTOWER,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_STATUE,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_BRIDGE,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_INTRO_CRATE,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_EAST_AFTER_STATUE,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_ESTATE_FAMILY_TOMB,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_ESTATE_ENTRANCE,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_ESTATE_HEDGE_GAPS,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_GARDEN_OF_JOY,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_BOXES,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_NEAR_BRAZIER,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_BELOW_BIG_POT_ARENA,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_RAFTERS,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_MAIN_ROOM_UPPER,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_SPINNY_POT_ROOM,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_LIBRARY_SHELF,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CART_PUZZLE,
        0,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FURNACE_ENTRANCE,
        0,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_INNER_FURNACE_HORIZONTAL_PISTONS,
        0,
        R.INNER_FURNACE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_INNER_FURNACE_CONVEYOR_BRIDGE,
        0,
        R.INNER_FURNACE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_INNER_FURNACE_CONVEYOR_GAUNTLET,
        0,
        R.INNER_FURNACE,
        [LocationGroup.SEED],
    ),
    # Soul Orbs
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FIRE_RETURN_UPPER,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_HOOKSHOT_SECRET,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_BOMB_RETURN,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_BOMB_SECRET,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_HOOKSHOT_RETURN,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FIRE_RETURN_LOWER,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FIRE_SECRET,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CATACOMBS_EXIT,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_HOOKSHOT_TOWERS,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_UNDER_BRIDGE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_EAST_TREE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_WINDING_BRIDGE_END,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CATACOMBS_ROOM_2,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CATACOMBS_ROOM_1,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_GATED_SEWER,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CATACOMBS_ENTRANCE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_CAVE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_SAILOR_TURNCAM,
        0,
        R.STRANDED_SAILOR,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_NORTH_LOCKSTONE_SEWER,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_LOCKSTONE_HOOKSHOT_NORTH,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_LOCKSTONE_EXIT,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_WEST_LOCKSTONE_SEWER,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CAMP_ROOFTOPS,
        0,
        R.CAMP_OF_THE_FREE_CROWS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CAMP_BROKEN_BRIDGE,
        0,
        R.CAMP_OF_THE_FREE_CROWS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_WATCHTOWERS_BEHIND_BARB_ELEVATOR,
        0,
        R.OLD_WATCHTOWERS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_DUNGEON_VINE,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_STUMP,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_OUTSIDE_LEFT_DUNGEON_EXIT,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_DUNGEON_COBWEB,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_LEFT_AFTER_KEY_DOOR,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_LOWER_BOMB_WALL,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_LORD_OF_DOORS_ARENA_HOOKSHOT,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_DUNGEON_LOWER_ENTRANCE,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_UPPER_ABOVE_HORN,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_ABOVE_THREE_PLANTS,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_UP_TURNCAM_LADDER,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_ABOVE_ENTRANCE_GATE,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_UPPER_BOMB_WALL,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_DUNGEON_LEFT_EXIT_SHELF,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_LOWER_HOOKSHOT,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FORTRESS_BOMB,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FORTRESS_HIDDEN_SEWER,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FORTRESS_DROP,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_ACCESS_CRYPT,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_BALCONY,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_LOVE_TURNCAM,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_LIFE_HOOKSHOT_LOOP,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_LOVE_BOMB_WALLS,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_LIFE_BOMB_WALL,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_BROKEN_BOARDWALK,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_SECRET_CAVE,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_TWIN_BENCHES,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_SEWER_MIDDLE,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_SEWER_END,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_PEACE,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_MANOR_IMP_LOFT,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_MANOR_LIBRARY_SHELF,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_MANOR_CHANDELIER,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FURNACE_LANTERN_CHAIN,
        0,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_SMALL_ROOM,
        0,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FURNACE_ENTRANCE_SEWER,
        0,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SOUL_ORB],
    ),
    # Tablets
    DeathsDoorLocationData(
        DeathsDoorLocationName.RED_ANCIENT_TABLET_OF_KNOWLEDGE,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.GREEN_ANCIENT_TABLET_OF_KNOWLEDGE,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CYAN_ANCIENT_TABLET_OF_KNOWLEDGE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.BLUE_ANCIENT_TABLET_OF_KNOWLEDGE,
        0,
        R.OLD_WATCHTOWERS,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ESTATE_OWL,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.RUINS_OWL, 0, R.OVERGROWN_RUINS, [LocationGroup.TABLET]
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.WATCHTOWERS_OWL,
        0,
        R.OLD_WATCHTOWERS,
        [LocationGroup.TABLET],
    ),
    # Levers
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_BOMB_EXIT,
        0,
        R.HALL_OF_DOORS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CEMETERY_SEWER,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GUARDIAN_OF_THE_DOOR_ACCESS,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CEMETERY_EAST_TREE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CATACOMBS_TOWER,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CEMETERY_EXIT_TO_ESTATE,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CATACOMBS_EXIT,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_HOOKSHOT_SILENT_SERVANT,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_SAILOR_TURNCAM_UPPER,
        0,
        R.STRANDED_SAILOR,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_SAILOR_TURNCAM_LOWER,
        0,
        R.STRANDED_SAILOR,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_SAILOR_GREATSWORD_GATE,
        0,
        R.STRANDED_SAILOR,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_EAST_START_SHORTCUT,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_ENTRANCE,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_EAST_LOWER,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_UPPER_SHORTCUT,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_DUAL_LASER_PUZZLE,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_TRACKING_BEAM_PUZZLE,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_VERTICAL_LASER_PUZZLE,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_NORTH_PUZZLE,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_SHRINE,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_HOOKSHOT_PUZZLE,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_UPPER_PUZZLE,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_UPPER_DUAL_LASER_PUZZLE,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_WATCHTOWERS_BEFORE_ICE_ARENA,
        0,
        R.OLD_WATCHTOWERS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_WATCHTOWERS_AFTER_ICE_SKATING,
        0,
        R.OLD_WATCHTOWERS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_WATCHTOWERS_AFTER_BOOMERS,
        0,
        R.OLD_WATCHTOWERS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_SETTLEMENT_GATE,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_UPPER_DUNGEON_ENTRANCE,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_LADDER_LEFT_OF_LORD_OF_DOORS_ARENA,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_ENTRANCE_LADDER_SHORTCUT,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_MAIN_GATE,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_DUNGEON_ENTRANCE_RIGHT_GATE,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_DUNGEON_ENTRANCE_LEFT_GATE,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_BOMB,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_MAIN_GATE,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_CENTRAL_SHORTCUT,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_STATUE,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_WATCHTOWER_LOWER,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_BRIDGE,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_PRE_MAIN_GATE,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_WATCHTOWER_UPPER,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_NORTH_WEST,
        0,
        R.FLOODED_FORTRESS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_ESTATE_ELEVATOR_LEFT,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_ESTATE_ELEVATOR_RIGHT,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_LOVE,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_LIFE_END,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_PEACE,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_JOY,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_LOVE_TURNCAM,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_LIFE_LANTERNS,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_ESTATE_UNDERGROUND_URN_SHED,
        0,
        R.ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_MANOR_BIG_POT_ARENA,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_MANOR_BOOKSHELF_SHORTCUT,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.LEVER],
    ),
    # Doors
    DeathsDoorLocationData(
        DeathsDoorLocationName.GROVE_OF_SPIRITS_DOOR,
        0,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LOST_CEMETERY_DOOR,
        0,
        R.LOST_CEMETERY_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.STRANDED_SAILOR_DOOR,
        0,
        R.STRANDED_SAILOR_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CASTLE_LOCKSTONE_DOOR,
        0,
        R.CASTLE_LOCKSTONE_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CAMP_OF_THE_FREE_CROWS_DOOR,
        0,
        R.CAMP_OF_THE_FREE_CROWS_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.OLD_WATCHTOWERS_DOOR,
        0,
        R.OLD_WATCHTOWERS_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.BETTYS_LAIR_DOOR,
        0,
        R.BETTYS_LAIR_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.OVERGROWN_RUINS_DOOR,
        0,
        R.OVERGROWN_RUINS_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MUSHROOM_DUNGEON_DOOR,
        0,
        R.MUSHROOM_DUNGEON_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.FLOODED_FORTRESS_DOOR,
        0,
        R.FLOODED_FORTRESS_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.THRONE_OF_THE_FROG_KING_DOOR,
        0,
        R.THRONE_OF_THE_FROG_KING_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ESTATE_OF_THE_URN_WITCH_DOOR,
        0,
        R.ESTATE_OF_THE_URN_WITCH_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CERAMIC_MANOR_DOOR,
        0,
        R.CERAMIC_MANOR_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.INNER_FURNACE_DOOR,
        0,
        R.INNER_FURNACE_DOOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.THE_URN_WITCHS_LABORATORY_DOOR,
        0,
        R.URN_WITCHS_LABORATORY_DOOR,
        [LocationGroup.DOOR],
    ),
    # Keys
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_CEMETERY_CENTRAL,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_CEMETERY_GREY_CROW,
        0,
        R.LOST_CEMETERY,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_CAMP_OF_THE_FREE_CROWS,
        0,
        R.CAMP_OF_THE_FREE_CROWS,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_LOCKSTONE_WEST,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_LOCKSTONE_NORTH,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_OVERGROWN_RUINS,
        0,
        R.OVERGROWN_RUINS,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_DUNGEON_HALL,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_DUNGEON_RIGHT,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_DUNGEON_NEAR_WATER_ARENA,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_MANOR_UNDER_DINING_ROOM,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_MANOR_AFTER_SPINNY_POT_ROOM,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_MANOR_LIBRARY,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.KEY],
    ),
    # Crow Souls
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_MANOR_AFTER_TORCH_PUZZLE,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_MANOR_IMP_LOFT,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_MANOR_LIBRARY,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_MANOR_BEDROOM,
        0,
        R.CERAMIC_MANOR,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_DUNGEON_HALL,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_DUNGEON_WATER_ARENA,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_DUNGEON_COBWEB,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_DUNGEON_RIGHTMOST,
        0,
        R.MUSHROOM_DUNGEON,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_LOCKSTONE_EAST,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_LOCKSTONE_WEST,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_LOCKSTONE_WEST_LOCKED,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_LOCKSTONE_SOUTH_WEST,
        0,
        R.CASTLE_LOCKSTONE,
        [LocationGroup.LOST_CROW],
    ),
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
