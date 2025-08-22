from typing import ClassVar, Any
from logging import warning

from Options import Option

try:
    from rule_builder import RuleWorldMixin
except ModuleNotFoundError:
    from .rule_builder import RuleWorldMixin
from .options import (
    DeathsDoorOptions,
    deathsdoor_options_presets,
    deathsdoor_option_groups,
    StartWeapon,
)
from .vanilla_pools import vanilla_location_lookup
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
from .json_generator import (
    generate_rule_json,
    generate_items_json,
    generate_locations_json,
)

deathsdoor_version = "0.1.0"


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
            authors=[""],
        )
    ]


class DeathsDoorWorld(RuleWorldMixin, World):
    """Reaping souls of the dead and punching a clock might get monotonous but it's honest work for a Crow.
    The job gets lively when your assigned soul is stolen and you must track down a desperate thief to a realm
    untouched by death - where creatures grow far past their expiry."""

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
            current_version = f"{deathsdoor_version}"
            slot_version = f"v{slot_data['APWorldVersion']}"

            raise Exception(
                f"Death's Door version error: The version of apworld used to generate this world ({slot_version}) "
                f"does not match the version of your installed apworld ({current_version})."
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

        # warn for all the incompatible options
        if "Weapon" in self.options.unrandomized_pools.value:
            if self.options.start_weapon != StartWeapon.option_sword:
                warning(
                    f"{self.player_name}: If Weapons are not randomized, start weapon will be forced to be sword."
                )
                self.options.start_weapon.value = StartWeapon.option_sword
        if "Shiny Thing" in self.options.unrandomized_pools.value:
            warning(
                f"{self.player_name}: If Shiny Things are not randomized, Rusty Belltower Key will still be added to "
                "the pool so that the player has access to day/night"
            )
            if "Soul Orb" in self.options.unrandomized_pools.value:
                warning(
                    f"{self.player_name}: Without Soul Orbs and Shiny Things, there is no location to put the Rusty "
                    "Belltower Key, so a random item will be added to the player's start inventory"
                )
        if "Soul Orb" in self.options.unrandomized_pools.value:
            if (
                self.options.extra_life_seeds.value > 0
                or self.options.extra_magic_shards.value > 0
                or self.options.extra_vitality_shards > 0
            ):
                warning(
                    f"{self.player_name}: If Soul Orbs are not randomized, no extra items can be safely added to the "
                    "seed. Extra Life Seeds, Extra Magic Shards, and Extra Vitality Shards will be set to 0."
                )
                self.options.extra_life_seeds.value = 0
                self.options.extra_magic_shards.value = 0
                self.options.extra_vitality_shards.value = 0

        if self.options.start_weapon == StartWeapon.option_random_excluding_umbrella:
            self.options.start_weapon.value = self.random.randint(0, 3)

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
            current_location_group_names = set(
                location_group.value for location_group in location_data.location_groups
            )

            # Make all locations that have not been specifically chosen in unrandomized_pools
            # If we somehow end up with items in two location groups, only omit them from randomization if all of their groups have been selected for unrandomized
            if (
                len(
                    self.options.unrandomized_pools.value.intersection(
                        current_location_group_names
                    )
                )
                == 0
            ):
                location = DeathsDoorLocation(
                    self.player,
                    location_data.name.value,
                    location_data.location_id,
                    region,
                )
                region.locations.append(location)
            elif (
                "Life Seed" in self.options.unrandomized_pools.value
                and "Life Seed" in current_location_group_names
            ):
                # To avoid having to list all the life seeds individually
                location = DeathsDoorLocation(
                    self.player,
                    location_data.name.value,
                    None,
                    region,
                )
                region.locations.append(location)
                location.place_locked_item(self.create_event(I.LIFE_SEED.value))
            else:
                # Create an event with the vanilla item name as needed
                if location_data.name in vanilla_location_lookup.keys():
                    location = DeathsDoorLocation(
                        self.player,
                        location_data.name.value,
                        None,
                        region,
                    )
                    region.locations.append(location)
                    location.place_locked_item(
                        self.create_event(
                            vanilla_location_lookup[location_data.name].value
                        )
                    )
            # Skip all other pools/locations selected as unrandomized (ex. non-progression)

        for event_location_data in event_location_table:
            region = self.get_region(event_location_data.region.value)
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

    def create_item(self, name: str, useful: bool = False) -> DeathsDoorItem:
        # if the name provided is an event, create it as an event
        if name in E:
            return DeathsDoorItem(
                name, ItemClassification.progression, None, self.player
            )

        # otherwise, look up the item data
        item_data = next(data for data in item_table if data.name.value == name)
        if useful:
            # Used to create useful versions instead of progression based on option
            # Standard create_item will still create the progression version
            return DeathsDoorItem(
                name, ItemClassification.useful, self.item_name_to_id[name], self.player
            )
        elif (
            True and IG.TABLET in item_data.item_groups
        ):  # This True is here so we can eventually have a tablet goal
            return DeathsDoorItem(
                name, ItemClassification.filler, self.item_name_to_id[name], self.player
            )
        else:
            return DeathsDoorItem(
                name, item_data.classification, self.item_name_to_id[name], self.player
            )

    def create_event(self, name: str) -> DeathsDoorItem:
        # for creating event versions of items for non-randomized pools
        return DeathsDoorItem(name, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        deathsdoor_items: list[DeathsDoorItem] = []
        items_to_create: dict[str, int] = {
            data.name.value: data.base_quantity_in_item_pool
            for data in item_table
            if len(
                self.options.unrandomized_pools.value.intersection(
                    set(data.item_groups)
                )
            )
            == 0  # filter out unrandomized pools
        }

        if "Weapon" not in self.options.unrandomized_pools.value and self.options.remove_spell_upgrades.value:
            items_to_create[I.FIRE] = 1
            items_to_create[I.BOMB] = 1
            items_to_create[I.HOOKSHOT] = 1
            items_to_create[I.BOW] = 0

        if self.options.start_weapon != StartWeapon.option_sword:
            # If Weapon unrandomized, start_weapon forced to be option_sword
            # Default is that Reaper's Sword is not in the pool, and the others are
            # Mod handles granting the starting weapon
            items_to_create[I.SWORD.value] = 1
            if self.options.start_weapon == StartWeapon.option_daggers:
                items_to_create[I.ROGUE_DAGGERS.value] = 0
            elif self.options.start_weapon == StartWeapon.option_hammer:
                items_to_create[I.THUNDER_HAMMER.value] = 0
            elif self.options.start_weapon == StartWeapon.option_greatsword:
                items_to_create[I.REAPERS_GREATSWORD.value] = 0
            elif self.options.start_weapon == StartWeapon.option_umbrella:
                items_to_create[I.DISCARDED_UMBRELLA.value] = 0

        if not self.options.roll_buffers:
            # If roll_buffers is not on, convert the weapons back to being useful
            # Done so to ensure that any weapons used in rules are created by create_item as progression if we aren't directly responsible for creating it
            for weapon_name in [
                I.SWORD.value,
                I.ROGUE_DAGGERS.value,
                I.REAPERS_GREATSWORD,
                I.DISCARDED_UMBRELLA,
            ]:
                if (
                    weapon_name in items_to_create.keys()
                    and items_to_create[weapon_name] == 1
                ):
                    items_to_create[weapon_name] = 0
                    deathsdoor_items.append(self.create_item(weapon_name, True))

        if (
            self.options.plant_pot_number < 50
        ) and "Life Seed" not in self.options.unrandomized_pools.value:
            # Only add life seeds to the pool if they are randomized
            # Only create up to the number of Life Seeds needed for check as progression
            items_to_create[I.LIFE_SEED.value] = self.options.plant_pot_number.value
            # Remainder are useful
            for _ in range(50 - self.options.plant_pot_number.value):
                deathsdoor_items.append(self.create_item(I.LIFE_SEED.value, True))

        # Create extra life seeds
        for _ in range(self.options.extra_life_seeds.value):
            deathsdoor_items.append(self.create_item(I.LIFE_SEED.value, True))

        # Create extra magic shards
        for _ in range(self.options.extra_magic_shards.value):
            deathsdoor_items.append(self.create_item(I.MAGIC_SHARD.value))

        # Create extra vitality shards
        for _ in range(self.options.extra_vitality_shards.value):
            deathsdoor_items.append(self.create_item(I.VITALITY_SHARD.value))

        for item, quantity in items_to_create.items():
            for _ in range(quantity):
                deathsdoor_items.append(self.create_item(item))

        if "Shiny Thing" in self.options.unrandomized_pools.value:
            # Still add the Rusty Belltower Key to pool so it is accessible for night
            deathsdoor_items.append(self.create_item(I.RUSTY_BELLTOWER_KEY.value))
            if "Soul Orb" in self.options.unrandomized_pools.value:
                # randomly choose an item to precollect, since there won't be space
                # for the Belltower key
                removed_item: DeathsDoorItem = self.random.choice(deathsdoor_items)
                self.push_precollected(removed_item)
                deathsdoor_items.remove(removed_item)

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
        slot_data = self.options.as_dict(
            "start_day_or_night",
            "start_weapon",
            "plant_pot_number",
            "soul_multiplier",
            "starting_souls",
        )
        slot_data["APWorldVersion"] = deathsdoor_version
        return slot_data

    def get_filler_item_name(self) -> str:
        return I.SOULS.value

    @classmethod
    def stage_fill_hook(
        cls,
        multiworld: MultiWorld,
        progitempool: list[Item],
        usefulitempool: list[Item],
        filleritempool: list[Item],
        fill_locations: list[Location],
    ) -> None:
        # This function was borrowed from Mysteryem's implementation of Lego Star Wars Complete Saga
        # https://github.com/Mysteryem/Archipelago-TCS/blob/v1.0.1/lego_star_wars_tcs/__init__.py#L1298-L1334
        game_player_ids = set(multiworld.get_game_players(cls.game))
        game_minimal_player_ids = {
            player
            for player in game_player_ids
            if multiworld.worlds[player].options.accessibility == "minimal"
        }

        def sort_func(item: Item):
            if (
                item.player in game_player_ids
                and item.name == I.LIFE_SEED.value
                and ItemClassification.progression in item.classification
            ):
                # Only sort the progression Life Seeds
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
