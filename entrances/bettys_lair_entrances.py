from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R

bettys_lair_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Betty's Lair
    DeathsDoorEntrance(
        R.BETTYS_LAIR_DOOR,
        R.BETTYS_LAIR,
        None,
    ),
    DeathsDoorEntrance(
        R.BETTYS_LAIR,
        R.BETTYS_LAIR_DOOR,
        Has(I.BETTYS_LAIR_DOOR),
    ),
    DeathsDoorEntrance(
        R.BETTYS_LAIR_EXIT_TO_OLD_WATCHTOWERS,
        R.BETTYS_LAIR,
        None,
    ),
    DeathsDoorEntrance(
        R.BETTYS_LAIR,
        R.BETTYS_LAIR_EXIT_TO_OLD_WATCHTOWERS,
        None,
    ),
]
