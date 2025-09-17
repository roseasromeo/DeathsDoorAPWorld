try:
    from rule_builder import False_
except ModuleNotFoundError:
    from ..rule_builder import False_

from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import HasAny, HasAll
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R

estate_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Estate of the Urn Witch
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CRYPT, R.ESTATE_OF_THE_URN_WITCH_ENTRANCE, None
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_ENTRANCE, R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CRYPT, None
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_ENTRANCE, R.ESTATE_OF_THE_URN_WITCH_SOUTH, None
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_SOUTH, R.ESTATE_OF_THE_URN_WITCH_ENTRANCE, False_()
    ),  # Not possible in vanilla
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        R.ESTATE_OF_THE_URN_WITCH_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_DOOR, R.ESTATE_OF_THE_URN_WITCH_SOUTH, None
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        HasAll(I.LEVER_GARDEN_OF_JOY, I.LEVER_GARDEN_OF_PEACE, I.BOMB),
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        HasAll(I.LEVER_GARDEN_OF_JOY, I.LEVER_GARDEN_OF_PEACE),
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CERAMIC_MANOR,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        None,
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CERAMIC_MANOR,
        None,
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        R.ESTATE_OF_THE_URN_WITCH_URN_SHED,
        HasAny(I.HOOKSHOT, I.LEVER_ESTATE_UNDERGROUND_URN_SHED),
    ),
    DeathsDoorEntrance(
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        R.ESTATE_OF_THE_URN_WITCH_GARDEN_OF_LIFE_END,
        HasAny(I.LEVER_GARDEN_OF_LIFE_LANTERNS, I.LEVER_GARDEN_OF_LIFE_END),
    ),
]
