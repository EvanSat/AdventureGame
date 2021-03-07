from scenes.nodes import get_story_links
import pytest

link1 = {
            "label":"Choice 1", 
            "id":"1"
        }

link2 = {
            "label":"Choice 2", 
            "id":"2",
            "requirements":["sword"]
        }

link3 = {
            "label":"Choice 3",
            "id":"3",
            "requirements":["Friend John"]
        }

link4 = {
            "label":"Choice 4", 
            "id":"4",
            "requirements":["sword","Friend John"]
        }

sample_scene_node = {
    "id": "single_node",
    "text": "hello world",
    "point_adjust": 100,
    "new_inventory": "Friend Maria",
    "links": [link1,link2,link3,link4]
}

@pytest.mark.parametrize('scene, user_inventory, result', [
    (
        sample_scene_node, 
        ["Friend John"],
        [link1, link3, link4]
    ),(
        sample_scene_node, 
        ["Friend John","sword"],
        [link1, link2, link3, link4]
    ),(
        sample_scene_node, 
        ["sword"],
        [link1, link2, link4]
    ),(
        sample_scene_node, 
        ["Friend Maria"],
        [link1]
    ),(
        sample_scene_node, 
        [],
        [link1]
    )
])
def test_get_story_links_with_exact_requirements(scene, user_inventory, result):
    assert get_story_links(scene, user_inventory) == result
