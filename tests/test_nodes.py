from scenes.nodes import get_story_text, get_scene_from_story, get_story_point_adjustments, get_story_new_inventory
import pytest

sample_scene_node = {
    "id": "single_node",
    "text": "hello world",
    "point_adjust": 100,
    "new_inventory": "Friend Maria",
    "links": ["B","C"]
}

sample_scene_array = [
    {
        "id": "A",
        "text": "this is the story text",
        "links": ["B","C"]
        "point_adjust": 105,
        "new_inventory": "Friend Ethan",
    },{
        "id": "B",
        "text": "story b",
        "point_adjust": 10,
        "new_inventory": "Understand JavaScript",
        "links": ["C"]
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
