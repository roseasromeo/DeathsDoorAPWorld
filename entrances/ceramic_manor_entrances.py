try:
    from rule_builder import False_
except ModuleNotFoundError:
    from ..rule_builder import False_
from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has, HasAll
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R
from ..events import DeathsDoorEventName as E

ceramic_manor_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Ceramic Manor
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        None,
    ),
    DeathsDoorEntrance(R.CERAMIC_MANOR_DOOR, R.CERAMIC_MANOR_MAIN_LOBBY, None),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY, R.CERAMIC_MANOR_DOOR, Has(I.CERAMIC_MANOR_DOOR)
    ),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY,
        R.CERAMIC_MANOR_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        False_(),
    ),  ## TODO Glitch logic
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY,
        R.CERAMIC_MANOR_LEFT,
        Has(I.YELLOW_KEY, 3) | Has(I.LEVER_MANOR_BIG_POT_ARENA),
    ),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY, R.CERAMIC_MANOR_LIBRARY, Has(I.YELLOW_KEY, 3)
    ),
    # TODO: Base randomizer has a confusing "entrance" here from the Ancient Door back to Ceramic Manor... Omitting for now
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY,
        R.CERAMIC_MANOR_ANCIENT_DOOR,
        HasAll(
            E.ACCESS_TO_DAY,
            I.CROW_MANOR_AFTER_TORCH_PUZZLE,
            I.CROW_MANOR_BEDROOM,
            I.CROW_MANOR_IMP_LOFT,
            I.CROW_MANOR_LIBRARY,
        ),
    ),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY,
        R.CERAMIC_MANOR_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
        Has(I.YELLOW_KEY, 3) & Has(I.FIRE),
    ),
    ## TODO: Check if can return from furnace observation rooms without it being opened, not in base rando
]
