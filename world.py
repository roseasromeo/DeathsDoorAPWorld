from typing import ClassVar, Any
from typing_extensions import override

from Options import Option

try:
    from rule_builder import RuleWorldMixin
except ModuleNotFoundError:
    from .rule_builder import RuleWorldMixin
from .options import (
    DeathsDoorOptions,
    deathsdoor_options_presets,
    deathsdoor_option_groups,
)
from .items import (
    item_name_to_id,
    item_table,
    item_name_groups,
    ItemGroup as IG,
    DeathsDoorItemName as I,
)
from .locations import (
    location_name_to_id,
    location_table,
    location_name_groups,
)
from .events import (
    DeathsDoorEventName as E,
    event_location_table,
)
from .event_rules import set_event_rules
from .regions import DeathsDoorRegionName as R
from .entrances.entrances import deathsdoor_entrances
from .rules import Has, set_location_rules
from worlds.AutoWorld import World, WebWorld
from BaseClasses import MultiWorld, Region, Location, Item, ItemClassification, Tutorial

# from .tracker import tracker_world
from .json_generator import generate_rule_json, generate_items_json, generate_locations_json

deathsdoor_version = 1


class DeathsDoorItem(Item):
    game: str = "Death's Door"


class DeathsDoorLocation(Location):
    game: str = "Death's Door"


class DeathsDoorWeb(WebWorld):
    theme = "stone"
    game = "Death's Door"
    option_groups = deathsdoor_option_groups
    options_presets = deathsdoor_options_presets

    tutorials = [
        Tutorial(
            tutorial_name="Multiworld Setup Guide",
            description="A guide to setting up the Death's Door Randomizer for Archipelago multiworld games.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=[""]
        )
    ]


class DeathsDoorWorld(RuleWorldMixin, World):
    """Reaping souls of the dead and punching a clock might get monotonous but it's honest work for a Crow. The job gets lively when your assigned soul is stolen and you must track down a desperate thief to a realm untouched by death - where creatures grow far past their expiry."""

    game = "Death's Door"  # name of the game/world
    web = DeathsDoorWeb()
    options_dataclass = DeathsDoorOptions  # options the player can set
    options: DeathsDoorOptions  # typing hints for option results
    topology_present = True  # show path to required location checks in spoiler
    origin_region_name = R.HALL_OF_DOORS_LOBBY

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    #  UT Integration
    # tracker_world: ClassVar[dict[str, Any]] = tracker_world
    ut_can_gen_without_yaml: ClassVar[bool] = True
    glitches_item_name: ClassVar[str] = E.OOL.value

    # rule_builder
    rule_caching_enabled = False

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:

        # Adapted from ClassicSpeed's SADX implementation of this feature
        if (
            "APWorldVersion" in slot_data
            and slot_data["APWorldVersion"] != deathsdoor_version
        ):
            current_version = f"v{deathsdoor_version // 100}.{(deathsdoor_version // 10) % 10}.{deathsdoor_version % 10}"
            slot_version = f"v{slot_data['APWorldVersion'] // 100}.{(slot_data['APWorldVersion'] // 10) % 10}.{slot_data['APWorldVersion'] % 10}"

            raise Exception(
                f"Death's Door version error: The version of apworld used to generate this world ({slot_version}) does not match the version of your installed apworld ({current_version})."
            )
        return slot_data

    def generate_early(self) -> None:
        # Add an important item to early or local_early if option is set
        early_important_item_candidates: list[I] = [
            I.CERAMIC_MANOR_DOOR,
            I.INNER_FURNACE_DOOR,
            I.LOST_CEMETERY_DOOR,
            I.GROVE_OF_SPIRITS_DOOR,
            I.OLD_WATCHTOWERS_DOOR,
            I.OVERGROWN_RUINS_DOOR,
            I.STRANDED_SAILOR_DOOR,
            I.CASTLE_LOCKSTONE_DOOR,
            I.FLOODED_FORTRESS_DOOR,
            I.MUSHROOM_DUNGEON_DOOR,
            I.CAMP_OF_THE_FREE_CROWS_DOOR,
            I.ESTATE_OF_THE_URN_WITCH_DOOR,
            I.HOOKSHOT,
            I.BOMB,
            I.FIRE,
        ]
        important_item = self.random.choice(early_important_item_candidates)
        if self.options.early_important_item.option_early:
            self.multiworld.early_items[self.player][important_item.value] = 1
        elif self.options.early_important_item.option_local_early:
            self.multiworld.local_early_items[self.player][important_item.value] = 1
        
        # Universal Tracker slot data handling
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            # Get the passed through slot data from the real generation
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]

            # Set all your options here instead of getting them from the yaml
            for key, value in slot_data.items():
                opt: Option[Any] | None = getattr(self.options, key, None)
                if opt is not None:
                    # You can also set .value directly but that won't work if you have OptionSets
                    setattr(self.options, key, opt.from_any(value))

    def create_regions(self) -> None:
        for deathsdoor_region in R:
            region = Region(deathsdoor_region.value, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for location_data in location_table:
            region = self.get_region(location_data.region.value)
            location = DeathsDoorLocation(
                self.player, location_data.name.value, location_data.location_id, region
            )
            region.locations.append(location)

        for event_location_data in event_location_table:
            region = self.get_region(
                event_location_data.region.value
            )
            event_location = DeathsDoorLocation(
                self.player, event_location_data.name.value, None, region
            )
            region.locations.append(event_location)
            event_location.place_locked_item(
                self.create_item(event_location_data.event_name.value)
            )

        for deathsdoor_entrance in deathsdoor_entrances:
            start_region = self.multiworld.get_region(
                deathsdoor_entrance.starting_region.value, self.player
            )
            end_region = self.multiworld.get_region(
                deathsdoor_entrance.ending_region.value, self.player
            )
            self.create_entrance(start_region, end_region, deathsdoor_entrance.rule)

    def create_item(self, name: str) -> DeathsDoorItem:
        # if the name provided is an event, create it as an event
        if name in E:
            return DeathsDoorItem(
                name, ItemClassification.progression, None, self.player
            )

        # otherwise, look up the item data
        item_data = next(data for data in item_table if data.name.value == name)
        if True and IG.TABLET in item_data.item_groups: # This True is here so we can eventually have a tablet goal
            return DeathsDoorItem(
                name, ItemClassification.filler, self.item_name_to_id[name], self.player
            )
        else:
            return DeathsDoorItem(
                name, item_data.classification, self.item_name_to_id[name], self.player
            )

    def create_items(self) -> None:
        deathsdoor_items: list[DeathsDoorItem] = []
        items_to_create: dict[str, int] = {
            data.name.value: data.base_quantity_in_item_pool for data in item_table
        }

        if not self.options.start_weapon.option_sword:
            starting_weapon: int = 0
            if self.options.start_weapon.option_random_excluding_umbrella:
                starting_weapon = self.random.randint(0,3)
            else:
                starting_weapon = self.options.start_weapon.value
            # Default is that Reaper's Sword is not in the pool, and the others are
            # Mod handles granting the starting weapon
            if not starting_weapon == 0:
                items_to_create[I.SWORD.value] = 1
            if starting_weapon == 1:
                items_to_create[I.ROGUE_DAGGERS.value] = 0
            elif starting_weapon == 2:
                items_to_create[I.THUNDER_HAMMER.value] = 0
            elif starting_weapon == 3:
                items_to_create[I.REAPERS_GREATSWORD.value] = 0
            elif starting_weapon == 4:
                items_to_create[I.DISCARDED_UMBRELLA.value] = 0


        for item, quantity in items_to_create.items():
            for i in range(quantity):
                deathsdoor_items.append(self.create_item(item))

        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(
            deathsdoor_items
        )
        deathsdoor_items += [
            self.create_item(self.get_filler_item_name()) for _ in range(junk)
        ]

        self.multiworld.itempool += deathsdoor_items

    def set_rules(self) -> None:
        set_location_rules(self)
        set_event_rules(self)

        self.set_completion_rule(Has(E.LORD_OF_DOORS))
        self.register_dependencies()

        # generate_rule_json()
        # generate_items_json()
        # generate_locations_json()

    def fill_slot_data(self) -> dict[str, Any]:
        # A dictionary returned from this method gets set as the slot_data and will be sent to the client after connecting.
        # The options dataclass has a method to return a `Dict[str, Any]` of each option name provided and the relevant
        # option's value.
        slot_data = self.options.as_dict("start_day_or_night", "start_weapon")
        slot_data["APWorldVersion"] = deathsdoor_version
        return slot_data

    def get_filler_item_name(self) -> str:
        return "100 Souls"

    @classmethod
    def stage_fill_hook(cls,
                        multiworld: MultiWorld,
                        progitempool: list[Item],
                        usefulitempool: list[Item],
                        filleritempool: list[Item],
                        fill_locations: list[Location],
                        ) -> None:
        # This function was borrowed from Mysteryem's implementation of Lego Star Wars Complete Saga
        # https://github.com/Mysteryem/Archipelago-TCS/blob/v1.0.1/lego_star_wars_tcs/__init__.py#L1298-L1334
        game_player_ids = set(multiworld.get_game_players(cls.game))
        game_minimal_player_ids = {player for player in game_player_ids
                                   if multiworld.worlds[player].options.accessibility == "minimal"}

        def sort_func(item: Item):
            if item.player in game_player_ids and item.name == I.LIFE_SEED.value:
                if item.player in game_minimal_player_ids:
                    # For minimal players, place Life Seeds first. This helps prevent fill from dumping logically relevant
                    # items into unreachable locations and reducing the number of reachable locations to fewer than the
                    # number of items remaining to be placed.
                    #
                    # Forcing Life Seeds first has the unfortunately sideeffect of priority fill picking Life Seeds first,
                    # but that will just have to be put up with in order to generate well. Maybe a small buffer of
                    # non-Life Seed items could be placed first so that the items in the buffer end up on priority
                    # locations.
                    return 1
                else:
                    # For non-minimal players, place Life Seeds last. This strategy helps prevent fill from filling most/all
                    # reachable locations with the macguffins that are only required for the one check.
                    return -1
            else:
                # Python sorting is stable, so this will leave everything else in its original order.
                return 0

        progitempool.sort(key=sort_func)