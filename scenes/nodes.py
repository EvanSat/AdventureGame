# Expected Node Structure
# =======================
# scene_array = [
#     {
#         "id": "A",
#         "text": "this is the story text",
#         "point_adjust": 100,
#         "new_inventory": "Friend Maria",
#         "links": ["B","C"]
#     },{
#         "id": "B",
#         "text": "story b",
#         "point_adjust": 10,
#         "new_inventory": "Understand JavaScript",
#         "links": ["C"]
#     },{
#         "id": "C",
#         "text": "story c",
#         "point_adjust": 15
#     }
# ]

# Find a scene node from an array based on the id.
def get_scene_from_story(scene_array, scene_id):
    for scene in scene_array:
        if scene["id"] == scene_id:
            return scene
    return None

# Find the text in a story.
def get_story_text(scene):
    if "text" in scene:
        return scene["text"]
    else:
        return 'Uh oh! The story is missing...'
