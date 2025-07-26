from typing import Any

try:
    from rule_builder import True_
except ModuleNotFoundError:
    from .rule_builder import True_
from .entrances import deathsdoor_entrances
from .locations import location_table
from .rules import deaths_door_location_rules
import json


def generate_rule_json():
    entrance_json_accumulator: list[dict[str, Any]] = list()

    for entrance in deathsdoor_entrances:
        rule_dict = dict()
        rule_dict["starting_region"] = entrance.starting_region
        rule_dict["ending_region"] = entrance.ending_region
        if entrance.rule is not None:
            rule_dict["rule_json"] = entrance.rule.to_dict()
        else:
            rule_dict["rule_json"] = True_().to_dict()
        entrance_json_accumulator.append(rule_dict)

    with open("EntranceRules.json", "w") as f:
        json.dump(entrance_json_accumulator, f)

    location_json_accumulator: list[dict[str, Any]] = list()

    for location_data in location_table:
        rule = deaths_door_location_rules[location_data.name]
        rule_dict = dict()
        rule_dict["location_name"] = location_data.name.value
        rule_dict["location_id"] = location_data.location_id
        rule_dict["region"] = location_data.region
        if rule is not None:
            rule_dict["rule_json"] = rule.to_dict()
        else:
            rule_dict["rule_json"] = True_().to_dict()
        location_json_accumulator.append(rule_dict)

    with open("LocationRules.json", "w") as f:
        json.dump(location_json_accumulator, f)
