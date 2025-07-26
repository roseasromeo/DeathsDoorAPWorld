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


@dataclass
class DeathsDoorOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    start_day_or_night: StartDayOrNight


deathsdoor_options_presets: dict[str, dict[str, Any]] = {}

deathsdoor_option_groups: list[OptionGroup] = [
    OptionGroup("Logic Options", [StartDayOrNight])
]
