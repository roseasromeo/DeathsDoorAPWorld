from typing import List, NamedTuple
try:
    from rule_builder import Rule
except ModuleNotFoundError:
    from .rule_builder import Rule
from .rules import Has
from .items import DeathsDoorItemName as I
from .regions import DeathsDoorRegionName as R

class DeathsDoorEntrance(NamedTuple):
    starting_region: R
    ending_region: R
    rule: Rule | None

deathsdoor_entrances: List[DeathsDoorEntrance] = [
    DeathsDoorEntrance(R.HALL_OF_DOORS, R.GOAL, None),
]