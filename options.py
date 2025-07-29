from dataclasses import dataclass
from typing import Any

from Options import (
    Choice,
    StartInventoryPool,
    PerGameCommonOptions,
    OptionGroup,
    Toggle,
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


@dataclass
class DeathsDoorOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    start_day_or_night: StartDayOrNight
    early_important_item: EarlyImportantItem


deathsdoor_options_presets: dict[str, dict[str, Any]] = {}

deathsdoor_option_groups: list[OptionGroup] = [
    OptionGroup("Logic Options", [StartDayOrNight, EarlyImportantItem])
]
