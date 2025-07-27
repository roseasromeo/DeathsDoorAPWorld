from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R

throne_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Throne of the Frog King
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING_EXIT_TO_FLOODED_FORTRESS,
        R.THRONE_OF_THE_FROG_KING,
        None,
    ),
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING,
        R.THRONE_OF_THE_FROG_KING_EXIT_TO_FLOODED_FORTRESS,
        None,
    ),
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING_DOOR,
        R.THRONE_OF_THE_FROG_KING,
        None,
    ),
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING,
        R.THRONE_OF_THE_FROG_KING_DOOR,
        Has(I.THRONE_OF_THE_FROG_KING_DOOR),
    ),
]
