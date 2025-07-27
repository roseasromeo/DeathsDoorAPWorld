from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R

laboratory_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Urn Witch's Laboratory
    DeathsDoorEntrance(R.URN_WITCHS_LABORATORY_DOOR, R.URN_WITCHS_LABORATORY, None),
    DeathsDoorEntrance(
        R.URN_WITCHS_LABORATORY,
        R.URN_WITCHS_LABORATORY_DOOR,
        Has(I.THE_URN_WITCHS_LABORATORY_DOOR),
    ),
    DeathsDoorEntrance(
        R.URN_WITCHS_LABORATORY,
        R.URN_WITCHS_LABORATORY_EXIT_TO_INNER_FURNACE,
        None,
    ),
    DeathsDoorEntrance(
        R.URN_WITCHS_LABORATORY_EXIT_TO_INNER_FURNACE,
        R.URN_WITCHS_LABORATORY,
        None,
    ),
]