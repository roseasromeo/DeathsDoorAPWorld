from enum import Enum
from typing import NamedTuple

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
    def __str__(self) -> str:
        return self.value
    
    # Spells and their upgrades
    FIRE_AVARICE = "Hall of Doors Fire Avarice (Ceramic Manor Ancient Door)"
    BOMB_AVARICE = "Hall of Doors Bomb Avarice (Mushroom Dungeon Ancient Door)"
    HOOKSHOT_AVARICE = "Hall of Doors Hookshot Avarice (Mushroom Dungeon Ancient Door)"
    FIRE_SILENT_SERVANT = "Crypt Fire Silent Servant"
    BOMB_SILENT_SERVANT = "Lost Cemetery East Tree Bridge Bomb Silent Servant"
    HOOKSHOT_SILENT_SERVANT = "Stranded Sailor Caves Hookshot Silent Servant"
    ARROW_SILENT_SERVANT = "Lost Cemetery Catacombs Arrow Silent Servant"

    # Weapons
    ROGUE_DAGGERS = "Garden of Life Rogue Daggers"
    DISCARDED_UMBRELLA = "Hall of Doors Discarded Umbrella"
    REAPERS_GREATSWORD = "Stranded Sailor Reaper's Greatsword"
    THUNDER_HAMMER = "Mushroom Dungeon Thunder Hammer"

    # Giant Souls
    BETTY = "Betty Giant Soul"
    FROG_KING = "Frog King Giant Soul"
    GRANDMA = "Urn Witch Giant Soul"

    # Shrines
    HEART_SHRINE_CEMETERY_BEHIND_ENTRANCE = "Lost Cemetery Behind Entrance Vitality Shard Shrine"
    MAGIC_SHRINE_CEMETERY_AFTER_SMOUGH_ARENA = (
        "Lost Cemetery After Smough Arena Magic Shard Shrine"
    )
    HEART_SHRINE_CEMETERY_WINDING_BRIDGE_END = (
        "Lost Cemetery Winding Bridge End Vitality Shard Shrine"
    )
    HEART_SHRINE_HOOKSHOT_ARENA = "Stranded Sailor Hookshot Arena Vitality Shard Shrine"
    MAGIC_SHRINE_SAILOR_TURNCAM = "Stranded Sailor Turncam Magic Shard Shrine"
    MAGIC_SHRINE_LOCKSTONE_SECRET_WEST = "Castle Lockstone Secret West Magic Shard Shrine"
    HEART_SHRINE_CAMP_ICE_SKATING = "Camp of the Free Crows Ice Skating Vitality Shard Shrine"
    MAGIC_SHRINE_RUINS_HOOKSHOT_ARENA = "Overgrown Ruins Hookshot Arena Magic Shard Shrine"
    MAGIC_SHRINE_RUINS_TURNCAM = "Overgrown Ruins Turncam Magic Shard Shrine"
    HEART_SHRINE_DUNGEON_WATER_ARENA = "Mushroom Dungeon Water Arena Vitality Shard Shrine"
    HEART_SHRINE_RUINS_SEWER = "Overgrown Ruins Sewer Vitality Shard Shrine"
    MAGIC_SHRINE_FORTRESS_BOW_SECRET = "Flooded Fortress Bow Secret Magic Shard Shrine"
    MAGIC_SHRINE_ESTATE_LEFT_OF_MANOR = "Estate of the Urn Witch Left of Manor Magic Shard Shrine"
    HEART_SHRINE_GARDEN_OF_LIFE = "Garden of Life Vitality Shard Shrine"
    MAGIC_SHRINE_MANOR_BATHROOM_PUZZLE = "Ceramic Manor Bathroom Puzzle Magic Shard Shrine"
    HEART_SHRINE_FURNACE_CART_PUZZLE = "Furnace Observation Rooms Cart Puzzle Vitality Shard Shrine"

    # Shiny Things
    ENGAGEMENT_RING = "Ceramic Manor Engagement Ring"
    OLD_COMPASS = "Lost Cemetery Catacombs Old Compass"
    INCENSE = "Lost Cemetery Summit Incense"
    UNDYING_BLOSSOM = "Lost Cemetery Undying Blossom (in southeast Green Roof Tower)"
    OLD_PHOTOGRAPH = "Ceramic Manor Old Photograph"
    SLUDGE_FILLED_URN = "Estate of the Urn Witch Sludge-Filled Urn"
    TOKEN_OF_DEATH = "Stranded Sailor Caves Token of Death"
    RUSTY_GARDEN_TROWEL = "Estate of the Urn Witch Rusty Garden Trowel"
    CAPTAINS_LOG = "Stranded Sailor Captain's Log"
    GIANT_ARROWHEAD = "Throne of the Frog King Giant Arrowhead"
    MALFORMED_SEED = "Overgrown Ruins Malformed Seed"
    CORRUPTED_ANTLER = "Mushroom Dungeon Corrupted Antler"
    MAGICAL_FOREST_HORN = "Overgrown Ruins Magical Forest Horn"
    ANCIENT_CROWN = "Castle Lockstone Ancient Crown"
    GRUNTS_OLD_MASK = "Stranded Sailor Grunt's Old Mask"
    ANCIENT_DOOR_SCALE_MODEL = "Hall of Doors Ancient Door Scale Model"
    MODERN_DOOR_SCALE_MODEL = "Hall of Doors Modern Door Scale Model"
    RUSTY_BELLTOWER_KEY = "Hall of Doors Rusty Belltower Key (Beat Lord of Doors)"
    SURVEILLANCE_DEVICE = "Hall of Doors Surveillance Device"
    SHINY_MEDALLION = "Camp of the Free Crows Shiny Medallion"
    INK_COVERED_TEDDY_BEAR = "Stranded Sailor Ink-Covered Teddy Bear"
    DEATHS_CONTRACT = "Castle Lockstone Death's Contract"
    MAKESHIFT_SOUL_KEY = "Grove of Spirits Makeshift Soul Key"
    MYSTERIOUS_LOCKET = "Old Watchtowers Mysterious Locket"

    # Seeds
    SEED_CEMETERY_BROKEN_BRIDGE = "Lost Cemetery Broken Bridge Life Seed"
    SEED_CATACOMBS_TOWER = "Lost Cemetery Catacombs Tower Life Seed"
    SEED_CEMETERY_LEFT_OF_MAIN_ENTRANCE = "Lost Cemetery Left of Main Entrance Life Seed"
    SEED_CEMETERY_NEAR_TABLET_GATE = "Lost Cemetery Near Tablet Gate Life Seed"
    SEED_BETWEEN_CEMETERY_AND_SAILOR = "Stranded Sailor Caves Between Cemetery and Sailor Life Seed"
    SEED_SAILOR_UPPER = "Stranded Sailor Upper Life Seed"
    SEED_LOCKSTONE_UPPER_EAST = "Castle Lockstone Upper East Life Seed"
    SEED_LOCKSTONE_SOUL_DOOR = "Castle Lockstone Soul Door Life Seed"
    SEED_LOCKSTONE_BEHIND_BARS = "Castle Lockstone Behind Bars Life Seed"
    SEED_LOCKSTONE_ENTRANCE_WEST = "Castle Lockstone Entrance West Life Seed"
    SEED_LOCKSTONE_NORTH = "Castle Lockstone North Life Seed"
    SEED_CAMP_LEDGE_WITH_HUTS = "Camp of the Free Crows Ledge With Huts Life Seed"
    SEED_CAMP_STALL = "Camp of the Free Crows Stall Life Seed"
    SEED_CAMP_ROOFTOPS = "Camp of the Free Crows Rooftops Life Seed"
    SEED_WATCHTOWERS_ICE_SKATING = "Old Watchtowers Ice Skating Life Seed"
    SEED_WATCHTOWERS_TABLET_DOOR = "Old Watchtowers Tablet Door Life Seed"
    SEED_WATCHTOWERS_ARCHER_PLATFORM = "Old Watchtowers Archer Platform Life Seed"
    SEED_WATCHTOWERS_BOXES = "Old Watchtowers Boxes Life Seed"
    SEED_DUNGEON_FIRE_PUZZLE_NEAR_WATER_ARENA = (
        "Mushroom Dungeon Fire Puzzle Near Water Arena Life Seed"
    )
    SEED_RUINS_LORD_OF_DOORS_ARENA = "Overgrown Ruins Lord of Doors Arena Life Seed"
    SEED_RUINS_FIRE_PLANT_CORRIDOR = "Overgrown Ruins Fire Plant Corridor Life Seed"
    SEED_DUNGEON_WATER_ARENA_LEFT_EXIT = "Mushroom Dungeon Water Arena Left Exit Life Seed"
    SEED_RUINS_RIGHT_MIDDLE = "Overgrown Ruins Right Middle Life Seed"
    SEED_RUINS_ON_SETTLEMENT_WALL = "Overgrown Ruins On Settlement Wall Life Seed"
    SEED_RUINS_BEHIND_BOXES = "Overgrown Ruins Behind Boxes Life Seed"
    SEED_RUINS_DOWN_THROUGH_BOMB_WALL = "Overgrown Ruins Down Through Bomb Wall Life Seed"
    SEED_DUNGEON_ABOVE_RIGHTMOST_CROW = "Mushroom Dungeon Above Rightmost Crow Life Seed"
    SEED_DUNGEON_RIGHT_ABOVE_KEY = "Mushroom Dungeon Right Above Key Life Seed"
    SEED_DUNGEON_AVARICE_BRIDGE = "Mushroom Dungeon Avarice Bridge Life Seed"
    SEED_FORTRESS_WATCHTOWER = "Flooded Fortress Watchtower Life Seed"
    SEED_FORTRESS_STATUE = "Flooded Fortress Statue Life Seed"
    SEED_FORTRESS_BRIDGE = "Flooded Fortress Bridge Life Seed"
    SEED_FORTRESS_INTRO_CRATE = "Flooded Fortress Intro Crate Life Seed"
    SEED_FORTRESS_EAST_AFTER_STATUE = "Flooded Fortress East After Statue Life Seed"
    SEED_ESTATE_FAMILY_TOMB = "Estate of the Urn Witch Family Tomb Life Seed"
    SEED_ESTATE_ENTRANCE = "Estate of the Urn Witch Entrance Life Seed"
    SEED_ESTATE_HEDGE_GAPS = "Estate of the Urn Witch Hedge Gaps Life Seed"
    SEED_GARDEN_OF_JOY = "Garden of Joy Life Seed"
    SEED_MANOR_BOXES = "Ceramic Manor Boxes Life Seed"
    SEED_MANOR_NEAR_BRAZIER = "Ceramic Manor Near Brazier Life Seed"
    SEED_MANOR_BELOW_BIG_POT_ARENA = "Ceramic Manor Below Big Pot Arena Life Seed"
    SEED_MANOR_RAFTERS = "Ceramic Manor Rafters Life Seed"
    SEED_MANOR_MAIN_ROOM_UPPER = "Ceramic Manor Main Room Upper Life Seed"
    SEED_MANOR_SPINNY_POT_ROOM = "Ceramic Manor Spinny Pot Room Life Seed"
    SEED_MANOR_LIBRARY_SHELF = "Ceramic Manor Library Shelf Life Seed"
    SEED_CART_PUZZLE = "Furnace Observation Rooms Cart Puzzle Life Seed"
    SEED_FURNACE_ENTRANCE = "Furnace Observation Rooms Entrance Life Seed"
    SEED_INNER_FURNACE_HORIZONTAL_PISTONS = "Inner Furnace Horizontal Pistons Life Seed"
    SEED_INNER_FURNACE_CONVEYOR_BRIDGE = "Inner Furnace Conveyor Bridge Life Seed"
    SEED_INNER_FURNACE_CONVEYOR_GAUNTLET = "Inner Furnace Conveyor Gauntlet Life Seed"

    # Soul Orbs
    SOUL_ORB_FIRE_RETURN_UPPER = "Hall of Doors Fire Return Upper Soul Orb"
    SOUL_ORB_HOOKSHOT_SECRET = "Hall of Doors Hookshot Secret Soul Orb"
    SOUL_ORB_BOMB_RETURN = "Hall of Doors Bomb Return Soul Orb"
    SOUL_ORB_BOMB_SECRET = "Hall of Doors Bomb Secret Soul Orb"
    SOUL_ORB_HOOKSHOT_RETURN = "Hall of Doors Hookshot Return Soul Orb"
    SOUL_ORB_FIRE_RETURN_LOWER = "Hall of Doors Fire Return Lower Soul Orb"
    SOUL_ORB_FIRE_SECRET = "Hall of Doors Fire Secret Soul Orb"
    SOUL_ORB_CATACOMBS_EXIT = "Lost Cemetery Catacombs Exit Soul Orb"
    SOUL_ORB_CEMETERY_HOOKSHOT_TOWERS = "Lost Cemetery Hookshot Towers Soul Orb"
    SOUL_ORB_CEMETERY_UNDER_BRIDGE = "Lost Cemetery Under Bridge Soul Orb"
    SOUL_ORB_CEMETERY_EAST_TREE = "Lost Cemetery East Tree Soul Orb"
    SOUL_ORB_CEMETERY_WINDING_BRIDGE_END = "Lost Cemetery Winding Bridge End Soul Orb"
    SOUL_ORB_CATACOMBS_ROOM_2 = "Lost Cemetery Catacombs Room 2 Soul Orb"
    SOUL_ORB_CATACOMBS_ROOM_1 = "Lost Cemetery Catacombs Room 1 Soul Orb"
    SOUL_ORB_CEMETERY_GATED_SEWER = "Lost Cemetery Gated Sewer Soul Orb"
    SOUL_ORB_CATACOMBS_ENTRANCE = "Lost Cemetery Catacombs Entrance Soul Orb"
    SOUL_ORB_CEMETERY_CAVE = "Lost Cemetery Cave Soul Orb"
    SOUL_ORB_SAILOR_TURNCAM = "Stranded Sailor Turncam Soul Orb"
    SOUL_ORB_NORTH_LOCKSTONE_SEWER = "North Lockstone Sewer Soul Orb"
    SOUL_ORB_LOCKSTONE_HOOKSHOT_NORTH = "Castle Lockstone Hookshot North Soul Orb"
    SOUL_ORB_LOCKSTONE_EXIT = "Castle Lockstone Exit Soul Orb"
    SOUL_ORB_WEST_LOCKSTONE_SEWER = "West Lockstone Sewer Soul Orb"
    SOUL_ORB_CAMP_ROOFTOPS = "Camp Rooftops Soul Orb"
    SOUL_ORB_CAMP_BROKEN_BRIDGE = "Camp Broken Bridge Soul Orb"
    SOUL_ORB_WATCHTOWERS_BEHIND_BARB_ELEVATOR = (
        "Old Watchtowers Behind Barb Elevator Soul Orb"
    )
    SOUL_ORB_DUNGEON_VINE = "Mushroom Dungeon Vine Soul Orb"
    SOUL_ORB_RUINS_STUMP = "Overgrown Ruins Stump Soul Orb"
    SOUL_ORB_RUINS_OUTSIDE_LEFT_DUNGEON_EXIT = (
        "Overgrown Ruins Outside Left Dungeon Exit Soul Orb"
    )
    SOUL_ORB_DUNGEON_COBWEB = "Mushroom Dungeon Cobweb Soul Orb"
    SOUL_ORB_RUINS_LEFT_AFTER_KEY_DOOR = "Overgrown Ruins Left After Key Door Soul Orb"
    SOUL_ORB_RUINS_LOWER_BOMB_WALL = "Overgrown Ruins Lower Bomb Wall Soul Orb"
    SOUL_ORB_RUINS_LORD_OF_DOORS_ARENA_HOOKSHOT = (
        "Overgrown Ruins Lord of Doors Arena Hookshot Soul Orb"
    )
    SOUL_ORB_DUNGEON_LOWER_ENTRANCE = "Mushroom Dungeon Lower Entrance Soul Orb"
    SOUL_ORB_RUINS_UPPER_ABOVE_HORN = "Overgrown Ruins Upper Above Horn Soul Orb"
    SOUL_ORB_RUINS_ABOVE_THREE_PLANTS = "Overgrown Ruins Above Three Plants Soul Orb"
    SOUL_ORB_RUINS_UP_TURNCAM_LADDER = "Overgrown Ruins Up Turncam Ladder Soul Orb"
    SOUL_ORB_RUINS_ABOVE_ENTRANCE_GATE = "Overgrown Ruins Above Entrance Gate Soul Orb"
    SOUL_ORB_RUINS_UPPER_BOMB_WALL = "Overgrown Ruins Upper Bomb Wall Soul Orb"
    SOUL_ORB_DUNGEON_LEFT_EXIT_SHELF = "Mushroom Dungeon Left Exit Shelf Soul Orb"
    SOUL_ORB_RUINS_LOWER_HOOKSHOT = "Overgrown Ruins Lower Hookshot Soul Orb"
    SOUL_ORB_FORTRESS_BOMB = "Flooded Fortress Bomb Soul Orb"
    SOUL_ORB_FORTRESS_HIDDEN_SEWER = "Flooded Fortress Hidden Sewer Soul Orb"
    SOUL_ORB_FORTRESS_DROP = "Flooded Fortress Drop Soul Orb"
    SOUL_ORB_ESTATE_ACCESS_CRYPT = "Estate of the Urn Witch Access Crypt Soul Orb"
    SOUL_ORB_ESTATE_BALCONY = "Estate of the Urn Witch Balcony Soul Orb"
    SOUL_ORB_GARDEN_OF_LOVE_TURNCAM = "Garden of Love Turncam Soul Orb"
    SOUL_ORB_GARDEN_OF_LIFE_HOOKSHOT_LOOP = "Garden of Life Hookshot Loop Soul Orb"
    SOUL_ORB_GARDEN_OF_LOVE_BOMB_WALLS = "Garden of Love Bomb Walls Soul Orb"
    SOUL_ORB_GARDEN_OF_LIFE_BOMB_WALL = "Garden of Life Bomb Wall Soul Orb"
    SOUL_ORB_ESTATE_BROKEN_BOARDWALK = "Estate of the Urn Witch Broken Boardwalk Soul Orb"
    SOUL_ORB_ESTATE_SECRET_CAVE = "Estate of the Urn Witch Secret Cave Soul Orb"
    SOUL_ORB_ESTATE_TWIN_BENCHES = "Estate of the Urn Witch Twin Benches Soul Orb"
    SOUL_ORB_ESTATE_SEWER_MIDDLE = "Estate of the Urn Witch Sewer Middle Soul Orb"
    SOUL_ORB_ESTATE_SEWER_END = "Estate of the Urn Witch Sewer End Soul Orb"
    SOUL_ORB_GARDEN_OF_PEACE = "Garden of Peace Soul Orb"
    SOUL_ORB_MANOR_IMP_LOFT = "Ceramic Manor Imp Loft Soul Orb"
    SOUL_ORB_MANOR_LIBRARY_SHELF = "Ceramic Manor Library Shelf Soul Orb"
    SOUL_ORB_MANOR_CHANDELIER = "Ceramic Manor Chandelier Soul Orb"
    SOUL_ORB_FURNACE_LANTERN_CHAIN = "Furnace Observation Rooms Lantern Chain Soul Orb"
    SOUL_ORB_SMALL_ROOM = "Furnace Observation Rooms Small Room Soul Orb"
    SOUL_ORB_FURNACE_ENTRANCE_SEWER = "Furnace Observation Rooms Entrance Sewer Soul Orb"

    # Tablets
    RED_ANCIENT_TABLET_OF_KNOWLEDGE = "Flooded Fortress Red Ancient Tablet of Knowledge (Jefferson)"
    YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE = "Overgrown Ruins Yellow Ancient Tablet of Knowledge (Avarice)"
    GREEN_ANCIENT_TABLET_OF_KNOWLEDGE = "Estate of the Urn Witch Green Ancient Tablet of Knowledge (Life Seeds)"
    CYAN_ANCIENT_TABLET_OF_KNOWLEDGE = "Lost Cemetery Cyan Ancient Tablet of Knowledge (The Grave Digger)"
    BLUE_ANCIENT_TABLET_OF_KNOWLEDGE = "Old Watchtowers Blue Ancient Tablet of Knowledge (Light Torches)"
    PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE = "Lost Cemetery Purple Ancient Tablet of Knowledge (Lord Ghosts)"
    ESTATE_OWL = "Estate of the Urn Witch Owl"
    RUINS_OWL = "Overgrown Ruins Owl"
    WATCHTOWERS_OWL = "Old Watchtowers Owl"

    # Levers
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
    ESTATE_OF_THE_URN_WITCH_DOOR = "Estate of the Urn Witch of the Urn Witch Door"
    CERAMIC_MANOR_DOOR = "Ceramic Manor Door"
    INNER_FURNACE_DOOR = "Inner Furnace Door"
    THE_URN_WITCHS_LABORATORY_DOOR = "The Urn Witch's Laboratory Door"

    # Keys
    KEY_CEMETERY_CENTRAL = "Lost Cemetery Central Key"
    KEY_CEMETERY_GREY_CROW = "Lost Cemetery Grey Crow Key"
    KEY_CAMP_OF_THE_FREE_CROWS = "Camp of the Free Crows Key"
    KEY_LOCKSTONE_WEST = "Castle Lockstone West Key"
    KEY_LOCKSTONE_NORTH = "Castle Lockstone North Key"
    KEY_OVERGROWN_RUINS = "Overgrown Ruins Key"
    KEY_DUNGEON_HALL = "Mushroom Dungeon Hall Key"
    KEY_DUNGEON_RIGHT = "Mushroom Dungeon Right Key"
    KEY_DUNGEON_NEAR_WATER_ARENA = "Mushroom Dungeon Near Water Arena Key"
    KEY_MANOR_UNDER_DINING_ROOM = "Ceramic Manor Under Dining Room Key"
    KEY_MANOR_AFTER_SPINNY_POT_ROOM = "Ceramic Manor After Spinny Pot Room Key"
    KEY_MANOR_LIBRARY = "Ceramic Manor Library Key"

    # Crow Souls
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


class DeathsDoorLocationData(NamedTuple):
    name: DeathsDoorLocationName
    location_id: int
    region: R
    location_groups: list[LocationGroup]


location_table: list[DeathsDoorLocationData] = [
    # Spells and their upgrades
    DeathsDoorLocationData(
        DeathsDoorLocationName.FIRE_AVARICE, 1, R.FIRE_AVARICE, [LocationGroup.SPELL]
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.BOMB_AVARICE, 2, R.BOMB_AVARICE, [LocationGroup.SPELL]
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HOOKSHOT_AVARICE,
        3,
        R.HOOKSHOT_AVARICE,
        [LocationGroup.SPELL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.FIRE_SILENT_SERVANT,
        4,
        R.CRYPT_MAIN_ROOM,
        [LocationGroup.SPELL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.BOMB_SILENT_SERVANT,
        5,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        [LocationGroup.SPELL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HOOKSHOT_SILENT_SERVANT,
        6,
        R.STRANDED_SAILOR_CAVES,
        [LocationGroup.SPELL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ARROW_SILENT_SERVANT,
        7,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        [LocationGroup.SPELL],
    ),
    # Weapons
    DeathsDoorLocationData(
        DeathsDoorLocationName.ROGUE_DAGGERS,
        8,
        R.ESTATE_OF_THE_URN_WITCH_GARDEN_OF_LIFE_END,
        [LocationGroup.WEAPON],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.DISCARDED_UMBRELLA,
        9,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.WEAPON],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.REAPERS_GREATSWORD,
        10,
        R.STRANDED_SAILOR_JEFFERSON,
        [LocationGroup.WEAPON],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.THUNDER_HAMMER,
        11,
        R.MUSHROOM_DUNGEON_THUNDER_HAMMER,
        [LocationGroup.WEAPON],
    ),
    # Giant Souls
    DeathsDoorLocationData(
        DeathsDoorLocationName.BETTY, 12, R.BETTYS_LAIR, [LocationGroup.GIANT_SOUL]
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.FROG_KING,
        13,
        R.THRONE_OF_THE_FROG_KING,
        [LocationGroup.GIANT_SOUL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.GRANDMA,
        14,
        R.URN_WITCHS_LABORATORY,
        [LocationGroup.GIANT_SOUL],
    ),
    # Shrines
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_CEMETERY_BEHIND_ENTRANCE,
        15,
        R.LOST_CEMETERY_NEAR_GROVE_OF_SPIRITS_DOOR,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_CEMETERY_AFTER_SMOUGH_ARENA,
        16,
        R.LOST_CEMETERY_NEAR_EXIT_TO_STRANDED_SAILOR,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_CEMETERY_WINDING_BRIDGE_END,
        17,
        R.LOST_CEMETERY_RIGHT_ARENA,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_HOOKSHOT_ARENA,
        18,
        R.STRANDED_SAILOR,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_SAILOR_TURNCAM,
        19,
        R.STRANDED_SAILOR_UPPER,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_LOCKSTONE_SECRET_WEST,
        20,
        R.CASTLE_LOCKSTONE_JAILED_SEED,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_CAMP_ICE_SKATING,
        21,
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_RUINS_HOOKSHOT_ARENA,
        22,
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_RUINS_TURNCAM,
        23,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_DUNGEON_WATER_ARENA,
        24,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_RUINS_SEWER,
        25,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_FORTRESS_BOW_SECRET,
        26,
        R.FLOODED_FORTRESS_ENTRANCE,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_ESTATE_LEFT_OF_MANOR,
        27,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_GARDEN_OF_LIFE,
        28,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_MANOR_BATHROOM_PUZZLE,
        29,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_FURNACE_CART_PUZZLE,
        30,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SHRINE],
    ),
    # Shiny Things
    DeathsDoorLocationData(
        DeathsDoorLocationName.ENGAGEMENT_RING,
        31,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.OLD_COMPASS,
        32,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.INCENSE,
        33,
        R.LOST_CEMETERY_SUMMIT,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.UNDYING_BLOSSOM,
        34,
        R.LOST_CEMETERY_CENTRAL,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.OLD_PHOTOGRAPH,
        35,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SLUDGE_FILLED_URN,
        36,
        R.ESTATE_OF_THE_URN_WITCH_URN_SHED,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.TOKEN_OF_DEATH,
        37,
        R.STRANDED_SAILOR_CAVES,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.RUSTY_GARDEN_TROWEL,
        38,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CAPTAINS_LOG,
        39,
        R.STRANDED_SAILOR_JEFFERSON,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.GIANT_ARROWHEAD,
        40,
        R.THRONE_OF_THE_FROG_KING,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MALFORMED_SEED,
        41,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CORRUPTED_ANTLER,
        42,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGICAL_FOREST_HORN,
        43,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ANCIENT_CROWN,
        44,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.GRUNTS_OLD_MASK,
        45,
        R.STRANDED_SAILOR_JEFFERSON,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ANCIENT_DOOR_SCALE_MODEL,
        46,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MODERN_DOOR_SCALE_MODEL,
        47,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.RUSTY_BELLTOWER_KEY,
        48,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SURVEILLANCE_DEVICE,
        49,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SHINY_MEDALLION,
        50,
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.INK_COVERED_TEDDY_BEAR,
        51,
        R.STRANDED_SAILOR_JEFFERSON,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.DEATHS_CONTRACT,
        52,
        R.CASTLE_LOCKSTONE_LIBRARY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAKESHIFT_SOUL_KEY,
        53,
        R.GROVE_OF_SPIRITS,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MYSTERIOUS_LOCKET,
        54,
        R.OLD_WATCHTOWERS_CAVE_ENTRANCE,
        [LocationGroup.SHINY_THING],
    ),
    # Seeds
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CEMETERY_BROKEN_BRIDGE,
        55,
        R.LOST_CEMETERY_STEADHONE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CATACOMBS_TOWER,
        56,
        R.LOST_CEMETERY_CENTRAL,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CEMETERY_LEFT_OF_MAIN_ENTRANCE,
        57,
        R.LOST_CEMETERY_CENTRAL,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CEMETERY_NEAR_TABLET_GATE,
        58,
        R.LOST_CEMETERY_RIGHT_ARENA,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_BETWEEN_CEMETERY_AND_SAILOR,
        59,
        R.STRANDED_SAILOR_CAVES,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_SAILOR_UPPER,
        60,
        R.STRANDED_SAILOR_UPPER,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_UPPER_EAST,
        61,
        R.CASTLE_LOCKSTONE_EAST_CROW,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_SOUL_DOOR,
        62,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_BEHIND_BARS,
        63,
        R.CASTLE_LOCKSTONE_JAILED_SEED,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_ENTRANCE_WEST,
        64,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_NORTH,
        65,
        R.CASTLE_LOCKSTONE_EAST,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CAMP_LEDGE_WITH_HUTS,
        66,
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CAMP_STALL,
        67,
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CAMP_ROOFTOPS,
        68,
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_WATCHTOWERS_ICE_SKATING,
        69,
        R.OLD_WATCHTOWERS_ICE_SKATING_END,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_WATCHTOWERS_TABLET_DOOR,
        70,
        R.OLD_WATCHTOWERS_FIRST_POT_AREA,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_WATCHTOWERS_ARCHER_PLATFORM,
        71,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_WATCHTOWERS_BOXES,
        72,
        R.OLD_WATCHTOWERS_JAMMING_START,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_FIRE_PUZZLE_NEAR_WATER_ARENA,
        73,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_LORD_OF_DOORS_ARENA,
        74,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_FIRE_PLANT_CORRIDOR,
        75,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_WATER_ARENA_LEFT_EXIT,
        76,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_RIGHT_MIDDLE,
        77,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_ON_SETTLEMENT_WALL,
        78,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_BEHIND_BOXES,
        79,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_DOWN_THROUGH_BOMB_WALL,
        80,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_ABOVE_RIGHTMOST_CROW,
        81,
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_RIGHT_ABOVE_KEY,
        82,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_AVARICE_BRIDGE,
        83,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_WATCHTOWER,
        84,
        R.FLOODED_FORTRESS_WATCHTOWER_LOWER,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_STATUE,
        85,
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_BRIDGE,
        86,
        R.FLOODED_FORTRESS_BRIDGE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_INTRO_CRATE,
        87,
        R.FLOODED_FORTRESS_ENTRANCE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_EAST_AFTER_STATUE,
        88,
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_ESTATE_FAMILY_TOMB,
        89,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_ESTATE_ENTRANCE,
        90,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,  ##TODO: CHECK IF THERE SHOULD BE A NEW REGION BEFORE SOUTH
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_ESTATE_HEDGE_GAPS,
        91,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_GARDEN_OF_JOY,
        92,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_BOXES,
        93,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_NEAR_BRAZIER,
        94,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_BELOW_BIG_POT_ARENA,
        95,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_RAFTERS,
        96,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_MAIN_ROOM_UPPER,
        97,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_SPINNY_POT_ROOM,
        98,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_LIBRARY_SHELF,
        99,
        R.CERAMIC_MANOR_LIBRARY,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CART_PUZZLE,
        100,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FURNACE_ENTRANCE,
        101,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_INNER_FURNACE_HORIZONTAL_PISTONS,
        102,
        R.INNER_FURNACE_POST_BURNER_6,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_INNER_FURNACE_CONVEYOR_BRIDGE,
        103,
        R.INNER_FURNACE_POST_BURNER_3,
        [LocationGroup.SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_INNER_FURNACE_CONVEYOR_GAUNTLET,
        104,
        R.INNER_FURNACE_POST_BURNER_7,
        [LocationGroup.SEED],
    ),
    # Soul Orbs
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FIRE_RETURN_UPPER,
        105,
        R.POST_FIRE_AVARICE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_HOOKSHOT_SECRET,
        106,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_BOMB_RETURN,
        107,
        R.POST_BOMB_AVARICE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_BOMB_SECRET,
        108,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_HOOKSHOT_RETURN,
        109,
        R.POST_HOOKSHOT_AVARICE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FIRE_RETURN_LOWER,
        110,
        R.POST_FIRE_AVARICE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FIRE_SECRET,
        111,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CATACOMBS_EXIT,
        112,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_HOOKSHOT_TOWERS,
        113,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_UNDER_BRIDGE,
        114,
        R.LOST_CEMETERY_CENTRAL,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_EAST_TREE,
        115,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_WINDING_BRIDGE_END,
        116,
        R.LOST_CEMETERY_RIGHT_ARENA,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CATACOMBS_ROOM_2,
        117,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CATACOMBS_ROOM_1,
        118,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_GATED_SEWER,
        119,
        R.LOST_CEMETERY_SUMMIT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CATACOMBS_ENTRANCE,
        120,
        R.LOST_CEMETERY_CENTRAL,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_CAVE,
        121,
        R.LOST_CEMETERY_STEADHONE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_SAILOR_TURNCAM,
        122,
        R.STRANDED_SAILOR_UPPER,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_NORTH_LOCKSTONE_SEWER,
        123,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_LOCKSTONE_HOOKSHOT_NORTH,
        124,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_LOCKSTONE_EXIT,
        125,
        R.CASTLE_LOCKSTONE_ROOF,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_WEST_LOCKSTONE_SEWER,
        126,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CAMP_ROOFTOPS,
        127,
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CAMP_BROKEN_BRIDGE,
        128,
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_WATCHTOWERS_BEHIND_BARB_ELEVATOR,
        129,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_DUNGEON_VINE,
        130,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_STUMP,
        131,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_OUTSIDE_LEFT_DUNGEON_EXIT,
        132,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.SOUL_ORB],
    ),  ## TODO: What region should this really be in???
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_DUNGEON_COBWEB,
        133,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_LEFT_AFTER_KEY_DOOR,
        134,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_LOWER_BOMB_WALL,
        135,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_LORD_OF_DOORS_ARENA_HOOKSHOT,
        136,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_DUNGEON_LOWER_ENTRANCE,
        137,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        [LocationGroup.SOUL_ORB],
    ),  # TODO: Currently, this soul orb is in a Overgrown Ruins region despite being in Mushroom Dungeon
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_UPPER_ABOVE_HORN,
        138,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_ABOVE_THREE_PLANTS,
        139,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_UP_TURNCAM_LADDER,
        140,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_ABOVE_ENTRANCE_GATE,
        141,
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_UPPER_BOMB_WALL,
        142,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_DUNGEON_LEFT_EXIT_SHELF,
        143,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_LOWER_HOOKSHOT,
        144,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FORTRESS_BOMB,
        145,
        R.FLOODED_FORTRESS_WATCHTOWER_LOWER,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FORTRESS_HIDDEN_SEWER,
        146,
        R.FLOODED_FORTRESS_WATCHTOWER_LOWER,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FORTRESS_DROP,
        147,
        R.FLOODED_FORTRESS_ENTRANCE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_ACCESS_CRYPT,
        148,
        R.CRYPT_MAIN_ROOM,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_BALCONY,
        149,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_LOVE_TURNCAM,
        150,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_LIFE_HOOKSHOT_LOOP,
        151,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_LOVE_BOMB_WALLS,
        152,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_LIFE_BOMB_WALL,
        153,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_BROKEN_BOARDWALK,
        154,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_SECRET_CAVE,
        155,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_TWIN_BENCHES,
        156,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_SEWER_MIDDLE,
        157,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_SEWER_END,
        158,
        R.ESTATE_OF_THE_URN_WITCH_URN_SHED,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_PEACE,
        159,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_MANOR_IMP_LOFT,
        160,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_MANOR_LIBRARY_SHELF,
        161,
        R.CERAMIC_MANOR_LIBRARY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_MANOR_CHANDELIER,
        162,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FURNACE_LANTERN_CHAIN,
        163,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_SMALL_ROOM,
        164,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FURNACE_ENTRANCE_SEWER,
        165,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SOUL_ORB],
    ),
    # Tablets
    DeathsDoorLocationData(
        DeathsDoorLocationName.RED_ANCIENT_TABLET_OF_KNOWLEDGE,
        166,
        R.FLOODED_FORTRESS_ENTRANCE,
        [LocationGroup.TABLET],
    ), ##### TODO: JEFFERSON IS NOT FULLY TESTED
    DeathsDoorLocationData(
        DeathsDoorLocationName.YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE,
        167,
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.GREEN_ANCIENT_TABLET_OF_KNOWLEDGE,
        168,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CYAN_ANCIENT_TABLET_OF_KNOWLEDGE,
        169,
        R.LOST_CEMETERY_RIGHT_ARENA,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.BLUE_ANCIENT_TABLET_OF_KNOWLEDGE,
        170,
        R.OLD_WATCHTOWERS_FIRST_POT_AREA,  ##TODO CHECK THIS REGION
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE,
        171,
        R.LOST_CEMETERY_STEADHONE,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ESTATE_OWL,
        172,
        R.ESTATE_OF_THE_URN_WITCH_GARDEN_OF_LIFE_END,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.RUINS_OWL,
        173,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.WATCHTOWERS_OWL,
        174,
        R.OLD_WATCHTOWERS_ICE_SKATING_END,
        [LocationGroup.TABLET],
    ),
    # Levers
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_BOMB_EXIT,
        175,
        R.POST_BOMB_AVARICE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CEMETERY_SEWER,
        176,
        R.LOST_CEMETERY_SUMMIT,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GUARDIAN_OF_THE_DOOR_ACCESS,
        177,
        R.LOST_CEMETERY_RIGHT_ARENA,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE,
        178,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,  ##TODO: CHECK IF ROUTE FROM RIGHT ARENA OR EXIT TO RUINS IS DISTINCT
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CEMETERY_EAST_TREE,
        179,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CATACOMBS_TOWER,
        180,
        R.LOST_CEMETERY_STEADHONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CEMETERY_EXIT_TO_ESTATE,
        181,
        R.LOST_CEMETERY_BELLTOWER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CATACOMBS_EXIT,
        182,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_HOOKSHOT_SILENT_SERVANT,
        183,
        R.STRANDED_SAILOR_CAVES,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_SAILOR_TURNCAM_UPPER,
        184,
        R.STRANDED_SAILOR_UPPER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_SAILOR_TURNCAM_LOWER,
        185,
        R.STRANDED_SAILOR_UPPER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_SAILOR_GREATSWORD_GATE,
        186,
        R.STRANDED_SAILOR_JEFFERSON,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_EAST_START_SHORTCUT,
        187,
        R.CASTLE_LOCKSTONE_LIBRARY,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_ENTRANCE,
        188,
        R.CASTLE_LOCKSTONE_ENTRANCE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_EAST_LOWER,
        189,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_UPPER_SHORTCUT,
        190,
        R.CASTLE_LOCKSTONE_EAST_UPPER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_DUAL_LASER_PUZZLE,
        191,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_TRACKING_BEAM_PUZZLE,
        192,
        R.CASTLE_LOCKSTONE_EAST,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_VERTICAL_LASER_PUZZLE,
        193,
        R.CASTLE_LOCKSTONE_EAST,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_NORTH_PUZZLE,
        194,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_SHRINE,
        195,
        R.CASTLE_LOCKSTONE_JAILED_SEED,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_HOOKSHOT_PUZZLE,
        196,
        R.CASTLE_LOCKSTONE_SOUTHWEST_UPPER,  ##TODO: CHECK IF THIS SEPARATELY NEEDS HOOKSHOT TOO?
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_UPPER_PUZZLE,
        197,
        R.CASTLE_LOCKSTONE_EAST_UPPER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_UPPER_DUAL_LASER_PUZZLE,
        198,
        R.CASTLE_LOCKSTONE_EAST_UPPER_KEYED_DOOR,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_WATCHTOWERS_BEFORE_ICE_ARENA,
        199,
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_WATCHTOWERS_AFTER_ICE_SKATING,
        200,
        R.OLD_WATCHTOWERS_ICE_SKATING_END,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_WATCHTOWERS_AFTER_BOOMERS,
        201,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_SETTLEMENT_GATE,
        202,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_UPPER_DUNGEON_ENTRANCE,
        203,
        R.MUSHROOM_DUNGEON_MAIN_HALL,  ### TODO: Check if this is actually in ruins (if so, may need a new region)
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_LADDER_LEFT_OF_LORD_OF_DOORS_ARENA,
        204,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_ENTRANCE_LADDER_SHORTCUT,
        205,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_MAIN_GATE,
        206,
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_DUNGEON_ENTRANCE_RIGHT_GATE,
        207,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_DUNGEON_ENTRANCE_LEFT_GATE,
        208,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW,
        209,
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_BOMB,
        210,
        R.FLOODED_FORTRESS_U_TURN,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_MAIN_GATE,
        211,
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_CENTRAL_SHORTCUT,
        212,
        R.FLOODED_FORTRESS_INSIDE_MAIN_GATE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_STATUE,
        213,
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_WATCHTOWER_LOWER,
        214,
        R.FLOODED_FORTRESS_ENTRANCE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_BRIDGE,
        215,
        R.FLOODED_FORTRESS_BREAKABLE_BRIDGES,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_PRE_MAIN_GATE,
        216,
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,  ##TODO Need new region to account for Fortress_Frog_King_Statue + Fortress_Statue optio Levern
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_WATCHTOWER_UPPER,
        217,
        R.FLOODED_FORTRESS_ENTRANCE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_NORTH_WEST,
        218,
        R.FLOODED_FORTRESS_BRIDGE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_ESTATE_ELEVATOR_LEFT,
        219,
        R.CRYPT_MAIN_ROOM,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_ESTATE_ELEVATOR_RIGHT,
        220,
        R.CRYPT_MAIN_ROOM,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_LOVE,
        221,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_LIFE_END,
        222,
        R.ESTATE_OF_THE_URN_WITCH_GARDEN_OF_LIFE_END,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_PEACE,
        223,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_JOY,
        224,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_LOVE_TURNCAM,
        225,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_LIFE_LANTERNS,
        226,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_ESTATE_UNDERGROUND_URN_SHED,
        227,
        R.ESTATE_OF_THE_URN_WITCH_URN_SHED,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_MANOR_BIG_POT_ARENA,
        228,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_MANOR_BOOKSHELF_SHORTCUT,
        229,
        R.CERAMIC_MANOR_LIBRARY,
        [LocationGroup.LEVER],
    ),
    # Doors
    DeathsDoorLocationData(
        DeathsDoorLocationName.GROVE_OF_SPIRITS_DOOR,
        230,
        R.DOOR_CHECK_FOR_GROVE_OF_SPIRITS,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LOST_CEMETERY_DOOR,
        231,
        R.DOOR_CHECK_FOR_LOST_CEMETERY,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.STRANDED_SAILOR_DOOR,
        232,
        R.DOOR_CHECK_FOR_STRANDED_SAILOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CASTLE_LOCKSTONE_DOOR,
        233,
        R.DOOR_CHECK_FOR_CASTLE_LOCKSTONE,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CAMP_OF_THE_FREE_CROWS_DOOR,
        234,
        R.DOOR_CHECK_FOR_CAMP_OF_THE_FREE_CROWS,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.OLD_WATCHTOWERS_DOOR,
        235,
        R.DOOR_CHECK_FOR_OLD_WATCHTOWERS,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.BETTYS_LAIR_DOOR,
        236,
        R.DOOR_CHECK_FOR_BETTYS_LAIR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.OVERGROWN_RUINS_DOOR,
        237,
        R.DOOR_CHECK_FOR_OVERGROWN_RUINS,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MUSHROOM_DUNGEON_DOOR,
        238,
        R.DOOR_CHECK_FOR_MUSHROOM_DUNGEON,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.FLOODED_FORTRESS_DOOR,
        239,
        R.DOOR_CHECK_FOR_FLOODED_FORTRESS,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.THRONE_OF_THE_FROG_KING_DOOR,
        240,
        R.DOOR_CHECK_FOR_THRONE_OF_THE_FROG_KING,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ESTATE_OF_THE_URN_WITCH_DOOR,
        241,
        R.DOOR_CHECK_FOR_ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CERAMIC_MANOR_DOOR,
        242,
        R.DOOR_CHECK_FOR_CERAMIC_MANOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.INNER_FURNACE_DOOR,
        243,
        R.DOOR_CHECK_FOR_INNER_FURNACE,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.THE_URN_WITCHS_LABORATORY_DOOR,
        244,
        R.DOOR_CHECK_FOR_URN_WITCHS_LABORATORY,
        [LocationGroup.DOOR],
    ),
    # Keys
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_CEMETERY_CENTRAL,
        245,
        R.LOST_CEMETERY_CENTRAL,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_CEMETERY_GREY_CROW,
        246,
        R.LOST_CEMETERY_SUMMIT,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_CAMP_OF_THE_FREE_CROWS,
        247,
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_LOCKSTONE_WEST,
        248,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_LOCKSTONE_NORTH,
        249,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_OVERGROWN_RUINS,
        250,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_DUNGEON_HALL,
        251,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_DUNGEON_RIGHT,
        252,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_DUNGEON_NEAR_WATER_ARENA,
        253,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_MANOR_UNDER_DINING_ROOM,
        254,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_MANOR_AFTER_SPINNY_POT_ROOM,
        255,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_MANOR_LIBRARY,
        256,
        R.CERAMIC_MANOR_LIBRARY,
        [LocationGroup.KEY],
    ),
    # Crow Souls
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_MANOR_AFTER_TORCH_PUZZLE,
        257,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_MANOR_IMP_LOFT,
        258,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_MANOR_LIBRARY,
        259,
        R.CERAMIC_MANOR_LIBRARY,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_MANOR_BEDROOM,
        260,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_DUNGEON_HALL,
        261,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_DUNGEON_WATER_ARENA,
        262,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_DUNGEON_COBWEB,
        263,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_DUNGEON_RIGHTMOST,
        264,
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_LOCKSTONE_EAST,
        265,
        R.CASTLE_LOCKSTONE_EAST_CROW,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_LOCKSTONE_WEST,
        266,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_LOCKSTONE_WEST_LOCKED,
        267,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_LOCKSTONE_SOUTH_WEST,
        268,
        R.CASTLE_LOCKSTONE_SOUTHWEST_CROW,
        [LocationGroup.LOST_CROW],
    ),
]


def locations_for_group(group: LocationGroup) -> set[str]:
    location_names: set[str] = set()
    for data in location_table:
        if group in data.location_groups:
            location_names.add(data.name.value)
    return location_names


location_name_to_id: dict[str, int] = {
    data.name.value: data.location_id for data in location_table
}

location_name_groups: dict[str, set[str]] = {}
# for loc_data in location_table:
#     loc_group_name = loc_data.name.value.split(" - ", 1)[0]
#     location_name_groups.setdefault(loc_group_name, set()).add(loc_data.name.value)

for group in LocationGroup:
    location_name_groups[group.name] = locations_for_group(group)
