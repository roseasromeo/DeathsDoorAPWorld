from typing import Any, NamedTuple


class SceneTransformation(NamedTuple):
    map_offsets: dict[int, tuple[int, int]]
    swap_x_z: bool
    negative_x: bool
    negative_z: bool


class Volume(NamedTuple):
    point1: tuple[int, int, int]
    point2: tuple[int, int, int]
    map_index: int

    def point_in_volume(self, point: tuple[int, int, int]) -> bool:
        for i in range(0, 3):
            min_v = min(self.point1[i], self.point2[i])
            max_v = max(self.point1[i], self.point2[i])
            if point[i] > max_v or point[i] < min_v:
                return False
        return True


BASE_TRANSFORMATION: float = 5.75 / 4.0
PER_SCENE_TRANSFORMATION: dict[int, SceneTransformation] = {
    0: SceneTransformation({0: (1248, 166)}, False, False, True),  # Hall of Doors
    1: SceneTransformation({0: (163, 111)}, False, False, True),  # Grove of Spirits
    2: SceneTransformation(
        {0: (375, 786), 1: (1033, 786)},
        False,
        False,
        True,
    ),  # Lost Cemetery
    3: SceneTransformation({0: (463, 672)}, False, False, True),  # Crypt
    4: SceneTransformation(
        {0: (1316, 1341)}, False, False, True
    ),  # Estate of the Urn Witch
    5: SceneTransformation(
        {0: (295, 1850), 1: (845, 1850), 2: (1095, 1850)},
        False,
        False,
        True,
    ),  # Ceramic Manor
    6: SceneTransformation(
        {0: (991, 1515)}, False, False, True
    ),  # Furnace Observation Rooms
    7: SceneTransformation({0: (-800, 1648)}, True, False, False),  # Inner Furnace
    8: SceneTransformation(
        {0: (1636, 1394)}, False, False, True
    ),  # The Urn Witch's Laboratory
    9: SceneTransformation(
        {0: (-350, 1216), 1: (295, 1216)},
        False,
        False,
        True,
    ),  # Overgrown Ruins and Mushroom Dungeon
    10: SceneTransformation({0: (-874, 908)}, False, False, True),  # Flooded Fortress
    11: SceneTransformation(
        {0: (517, 1772)}, False, False, True
    ),  # Throne of the Frog King
    12: SceneTransformation(
        {0: (599, 354)}, False, False, True
    ),  # Stranded Sailor Caves
    13: SceneTransformation({0: (961, 419)}, False, False, True),  # Stranded Sailor
    14: SceneTransformation(
        {0: (130, 1706), 1: (130, 1306)},
        True,
        False,
        False,
    ),  # Castle Lockstone
    15: SceneTransformation(
        {0: (621, 1244)}, False, False, True
    ),  # Camp of the Free Crows
    16: SceneTransformation({0: (1155, 1759)}, False, False, True),  # Old Watchtowers
    17: SceneTransformation({0: (-17, 265)}, False, False, True),  # Betty's Lair
}

MAP_VOLUMES: dict[int, list[Volume]] = {
    2: [
        Volume((87, 29, 153), (60, 35, 180), 1),
        Volume((64, -100, 152), (160, 23, 256), 1),
        Volume((122, 23, 235), (83, 29, 264), 1),
        Volume((80, -100, 180), (16, 23, 247), 1),
        Volume((20, -100, 245), (-50, 23, 170), 1),
        Volume((15, -100, 200), (70, 23, 340), 1),
    ],
    5: [
        Volume((-242, 26, 952), (-26, 40, 1070), 1),
        Volume((-54, 38, 1060), (-185, 57, 1094), 1),
        Volume((60, 18, 1050), (35, 36, 965), 1),
        Volume((26, 23, 960), (-22, 62, 1013), 1),
        Volume((26, 47, 1013), (-22, 62, 1047), 1),
        Volume((-96, 40, 952), (-26, 100, 1230), 2),
        Volume((-19, 36, 1013), (33, 39, 1230), 2),
        Volume((-19, 29, 1048), (33, 50, 1230), 2),
    ],
    9: [
        Volume((220, -110, 476), (278, -75, 525), 1),
        Volume((260, -101, 586), (611, -200, 430), 1),
        Volume((616, -101, 587), (693, -200, 532), 1),
        Volume((537, -74, 587), (693, -200, 700), 1),
        Volume((540, -83, 484), (597, -200, 573), 1),
        Volume((491, -98, 587), (535, -200, 681), 1),
        Volume((424, -90, 527), (491, -200, 642), 1),
        Volume((425, -90, 615), (489, -200, 783), 1),
        Volume((478, -100, 680), (542, -200, 753), 1),
        Volume((478, -93, 750), (532, -200, 813), 1),
        Volume((330, -93, 777), (421, -200, 732), 1),
        Volume((415, -93, 732), (335, -200, 650), 1),
        Volume((383, -93, 663), (198, -200, 512), 1),
        Volume((393, -93, 564), (425, -200, 600), 1),
        Volume((327, -60, 688), (380, -200, 772), 1),
    ],
    14: [Volume((-1000, 15, -1000), (1000, 100, 1000), 1)],
}


def map_page_index(data: Any) -> int:
    mapping: dict[str, int] = {
        "hall_of_doors": 0,
        "grove_of_spirits": 1,
        "lost_cemetery": 2,
        "crypt": 3,
        "estate_of_the_urn_witch": 4,
        "ceramic_manor": 5,
        "furnace_observation_rooms": 6,
        "inner_furnace": 7,
        "the_urn_witchs_laboratory": 8,
        "overgrown_ruins": 9,
        "flooded_fortress": 10,
        "throne_of_the_frog_king": 11,
        "stranded_sailor_caves": 12,
        "stranded_sailor": 13,
        "castle_lockstone": 14,
        "camp_of_the_free_crows": 15,
        "old_watchtowers": 16,
        "bettys_lair": 17,
    }
    return mapping.get(data, 0)


def location_icon_coords(
    index: int | None, coords: dict[str, Any]
) -> tuple[int, int, str] | None:
    """Converts player coordinates provided by the game mod into image coordinates for the map page."""
    if index is None or not coords:
        return None

    pos_x = coords.get("X", 0) * BASE_TRANSFORMATION
    pos_z = coords.get("Z", 0) * BASE_TRANSFORMATION

    if index in PER_SCENE_TRANSFORMATION.keys():
        scene_transformation = PER_SCENE_TRANSFORMATION[index]
        map_index = calculate_map_index(index, coords)
        if scene_transformation.negative_x:
            pos_x = -pos_x
        if scene_transformation.negative_z:
            pos_z = -pos_z
        if scene_transformation.swap_x_z:
            temp = pos_z
            pos_z = pos_x
            pos_x = temp
        map_x = pos_x + scene_transformation.map_offsets[map_index][0]
        map_y = pos_z + scene_transformation.map_offsets[map_index][1]

        return map_x, map_y, f"images/icons/crow_position_icon.png"
    else:
        return None


def calculate_map_index(index: int, coords: dict[str, Any]) -> int:
    if index not in MAP_VOLUMES.keys():
        return 0
    else:
        point = (
            int(coords.get("X", 0)),
            int(coords.get("Y", 0)),
            int(coords.get("Z", 0)),
        )
        for volume in MAP_VOLUMES[index]:
            if volume.point_in_volume(point):
                return volume.map_index
        return 0


tracker_world = {
    "map_page_folder": "tracker",
    "map_page_maps": "maps/maps.json",
    "map_page_locations": "locations/locations.json",
    "map_page_setting_key": "{player}_{team}_deathsdoor_map",
    "map_page_index": map_page_index,
    "location_setting_key": "{player}_{team}_deathsdoor_coords",
    "location_icon_coords": location_icon_coords,
}
