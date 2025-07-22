from enum import Enum, auto
from typing import Dict, NamedTuple, Set, List

from .regions import DeathsDoorRegionName


class LocationGroup(Enum):
    Spell = "Spell"

class DeathsDoorLocationName(str, Enum):
    Fire_Avarice = "Fire Avarice"

class DeathsDoorEventLocationName(str, Enum):
    VICTORY = "Defeat the Lord of Doors"

class DeathsDoorLocationData(NamedTuple):
    name: DeathsDoorLocationName
    location_id: int
    region: DeathsDoorRegionName
    location_groups: List[LocationGroup]

location_table: List[DeathsDoorLocationData] = [

]

location_table.sort(key = lambda entry: entry.name.name)

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

