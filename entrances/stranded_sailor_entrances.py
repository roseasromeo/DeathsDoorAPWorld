from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has, HasAll
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R
from ..events import DeathsDoorEventName as E

stranded_sailor_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Stranded Sailor
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_EXIT_TO_STRANDED_SAILOR_CAVES, R.STRANDED_SAILOR, None
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR, R.STRANDED_SAILOR_EXIT_TO_STRANDED_SAILOR_CAVES, None
    ),
    DeathsDoorEntrance(R.STRANDED_SAILOR_DOOR, R.STRANDED_SAILOR, None),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR, R.STRANDED_SAILOR_DOOR, Has(I.STRANDED_SAILOR_DOOR)
    ),
    DeathsDoorEntrance(R.STRANDED_SAILOR_UPPER, R.STRANDED_SAILOR, Has(I.BOMB)),
    DeathsDoorEntrance(R.STRANDED_SAILOR, R.STRANDED_SAILOR_JEFFERSON, None),
    DeathsDoorEntrance(R.STRANDED_SAILOR_JEFFERSON, R.STRANDED_SAILOR, None),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_JEFFERSON,
        R.STRANDED_SAILOR_JEFFERSON_QUEST_START,
        HasAll(E.ACCESS_TO_NIGHT, I.INK_COVERED_TEDDY_BEAR),
    ),  ##TODO: Jefferson's quest/pathing is not implemented yet
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_JEFFERSON_QUEST_START,
        R.STRANDED_SAILOR_JEFFERSON,
        None,
    ),  ##TODO: Jefferson's quest/pathing is not implemented yet
    DeathsDoorEntrance(R.STRANDED_SAILOR, R.STRANDED_SAILOR_UPPER, Has(I.BOMB)),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_UPPER, R.STRANDED_SAILOR_EXIT_TO_CASTLE_LOCKSTONE, None
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_EXIT_TO_CASTLE_LOCKSTONE, R.STRANDED_SAILOR_UPPER, None
    ),
]