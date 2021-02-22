from scenes.handle import print_scene
import io
import sys
import pytest

sample_scene_node = {
    "id": "single_node",
    "text": "hello world\nsecond line of story\nthird line",
    "point_adjust": 100,
    "new_inventory": "Friend Maria",
    "links": [
        {"label":"Choice 1", "id":"1"},
        {"label":"Choice 2", "id":"2"}
    ]
}

sample_scene_from_file = {
    "id": "single_node",
    "file": "tests/test_sample.txt",
    "links": [
        {"label":"Choice 3", "id":"3"},
        {"label":"Choice 4", "id":"4"}
    ]
}

@pytest.mark.parametrize('scene, contains_result', [
    (sample_scene_node, "hello world"),
    (sample_scene_node, "second line of story"),
    (sample_scene_node, "third line"),
    (sample_scene_node, "1. Choice 1"),
    (sample_scene_node, "2. Choice 2"),
    (sample_scene_from_file, "This is just a sample test file."),
    (sample_scene_from_file, "1. Choice 3"),
    (sample_scene_from_file, "2. Choice 4")
])
def test_print_scene(scene, contains_result):
    print_scene(scene)

    captured_output = io.StringIO()  # Create StringIO object
    sys.stdout = captured_output     #  and redirect stdout.
    print_scene(scene)   # Call unchanged function.
    sys.stdout = sys.__stdout__      # Reset redirect.

    assert contains_result in captured_output.getvalue()