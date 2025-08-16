from dataclasses import dataclass
from typing import Any

from Options import (
    Choice,
    StartInventoryPool,
    PerGameCommonOptions,
    OptionGroup,
    Range,
)


class StartDayOrNight(Choice):
    """Choose whether to start with daytime or nighttime. Must access Rusty Belltower Bell in game to toggle."""

    internal_name = "start_day_or_night"
    display_name = "Start Day or Night"
    option_day = 0
    option_night = 1

class EarlyImportantItem(Choice):
    """Choose whether one random important item will be placed early in the multiworld ("early"), early and in your world ("local early"), or be allowed to be randomly placed ("random placement").
    If random placement, generation is more likely to fail.
    Important items are all non-boss doors, Hookshot, Bomb, and Fire since these unlock access to more early game checks."""

    internal_name = "early_important_item"
    display_name = "Early Important Item"
    option_early = 0
    option_local_early = 1
    option_random_placement = 2
    default = option_early

class ExtraLifeSeeds(Range):
    """Add extra life seeds to the item pool. Extra life seeds will be marked as useful. Extra items will replace 100 Souls items."""

    internal_name = "extra_life_seeds"
    display_name = "Extra Life Seeds"
    range_start = 0
    range_end = 20
    default = 0

class ExtraMagicShards(Range):
    """Add extra magic shards to the item pool. Extra magic shards can allow magic to go over the vanilla maximum of 6. Extra items will replace 100 Souls items."""

    internal_name = "extra_magic_shards"
    display_name = "Extra Magic Shards"
    range_start = 0
    range_end = 8
    default = 0

class ExtraVitalityShards(Range):
    """Add extra vitality shards to the item pool. Extra health shards can allow health to go over the vanilla maximum of 6. These life seeds will replace 100 Souls items."""

    internal_name = "extra_magic_shards"
    display_name = "Extra Magic Shards"
    range_start = 0
    range_end = 8
    default = 0

class StartWeapon(Choice):
    """Choose which weapon you would like to start with (others will be shuffled into the itempool as useful items). Note: Umbrella is a much worse weapon than the other 4. Choose at your own risk."""

    internal_name = "start_weapon"
    display_name = "Starting Weapon"
    option_sword = 0
    option_daggers = 1
    option_hammer = 2
    option_greatsword = 3
    option_umbrella = 4
    option_random_excluding_umbrella = 5
    default = option_sword

class PlantedPotsRequired(Range):
    """Number of planted pots required for Green Tablet location. Also, adjusts the number of Life Seeds marked as Progression. Vanilla value is 50."""

    internal_name = "plant_pot_number"
    display_name = "Number of Planted Pots Required for Green Tablet"
    range_start = 1
    range_end = 50
    default = 25

@dataclass
class DeathsDoorOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    start_day_or_night: StartDayOrNight
    early_important_item: EarlyImportantItem
    start_weapon: StartWeapon
    plant_pot_number: PlantedPotsRequired
    extra_life_seeds: ExtraLifeSeeds
    extra_magic_shards: ExtraMagicShards
    extra_vitality_shards: ExtraVitalityShards


deathsdoor_options_presets: dict[str, dict[str, Any]] = {}

deathsdoor_option_groups: list[OptionGroup] = [
    OptionGroup("Logic Options", [StartDayOrNight, PlantedPotsRequired, EarlyImportantItem]),
    OptionGroup("Itempool Modification Options", [ExtraLifeSeeds, ExtraMagicShards, ExtraVitalityShards]),
    OptionGroup("Customization Options", [StartWeapon])
]
