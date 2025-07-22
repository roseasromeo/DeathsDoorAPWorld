from dataclasses import dataclass
from typing import Dict, Any

from Options import StartInventoryPool, PerGameCommonOptions, OptionGroup


@dataclass
class DeathsDoorOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool


deathsdoor_options_presets = {
}

deathsdoor_option_groups: Dict[str, Dict[str, Any]] = [
]
