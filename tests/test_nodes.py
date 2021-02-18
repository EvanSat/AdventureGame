from scenes.nodes import get_story_text, get_scene_from_story, get_story_point_adjustments, get_story_new_inventory, get_story_links
import pytest

sample_scene_node = {
    "id": "single_node",
    "text": "hello world",
    "point_adjust": 100,
    "new_inventory": "Friend Maria",
    "links": [
        {"label":"Choice 1", "id":"1"},
        {"label":"Choice 2", "id":"2"}
    ]
}

sample_scene_array = [
    {
        "id": "A",
        "text": "this is the story text",
        "point_adjust": 105,
        "new_inventory": "Friend Ethan",
        "links": [
            {"label":"Option B", "id":"B"},
            {"label":"Option C", "id":"C"}
        ]
    },{
        "id": "B",
        "text": "story b",
        "point_adjust": 10,
        "new_inventory": "Understand JavaScript",
        "links": [
            {"label":"Option C", "id":"C"}
        ]
    },{
        "id": "C",
        "text": "story c",
        "point_adjust": 15
    }
]

@pytest.mark.parametrize('scene, result', [
    (sample_scene_node, 'hello world'),
    ({"id": "missingText"}, 'Uh oh! The story is missing...'),
    (sample_scene_array[1], 'story b')
])
def test_get_story_text(scene, result):
    assert get_story_text(scene) == result

@pytest.mark.parametrize('scene_array, scene_id, result', [
    (sample_scene_array, 'A', sample_scene_array[0]),
    (sample_scene_array, 'B', sample_scene_array[1]),
    (sample_scene_array, 'C', sample_scene_array[2])
])
def test_get_scene_from_story(scene_array, scene_id, result):
    assert get_scene_from_story(scene_array, scene_id) == result

@pytest.mark.parametrize('scene, result', [
    (sample_scene_node, 100),
    (sample_scene_array[0], 105),
    (sample_scene_array[1], 10),
    (sample_scene_array[2], 15)
])
def test_get_story_point_adjustments(scene, result):
    assert get_story_point_adjustments(scene) == result

@pytest.mark.parametrize('scene, result', [
    (sample_scene_node, "Friend Maria"),
    (sample_scene_array[0], "Friend Ethan"),
    (sample_scene_array[1], "Understand JavaScript"),
    (sample_scene_array[2], None)
])
def test_get_story_new_inventory(scene, result):
    assert get_story_new_inventory(scene) == result

@pytest.mark.parametrize('scene, result', [
    (sample_scene_node, [
        {"label":"Choice 1", "id":"1"},
        {"label":"Choice 2", "id":"2"}
    ]),
    (sample_scene_array[0], [
        {"label":"Option B", "id":"B"},
        {"label":"Option C", "id":"C"}
    ]),
    (sample_scene_array[1], [
        {"label":"Option C", "id":"C"}
    ]),
    (sample_scene_array[2], None)
])
def test_get_story_links(scene, result):
    assert get_story_links(scene) == result
