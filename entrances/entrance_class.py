from typing import TYPE_CHECKING, NamedTuple

try:
    from rule_builder import Rule
except ModuleNotFoundError:
    from ..rule_builder import Rule
from ..regions import DeathsDoorRegionName as R

if TYPE_CHECKING:
    from .. import DeathsDoorWorld

from entrance_rando import EntranceType

class DeathsDoorEntrance(NamedTuple):
    starting_region: R
    ending_region: R
    rule: Rule["DeathsDoorWorld"] | None
    name: str = ""
    loading_zone_id: str = ""
    scene_name: str = ""
    no_jefferson: bool = False
