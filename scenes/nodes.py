# Expected Node Structure
# =======================
# scene_array = [
#     {
#         "id": "A",
#         "text": "this is the story text",
#         "point_adjust": 100,
#         "new_inventory": "Friend Maria",
#         "links": [
#             {"label":"Option B", "id":"B"},
#             {"label":"Option C", "id":"C"}
#         ]
#     },{
#         "id": "B",
#         "text": "story b",
#         "point_adjust": 10,
#         "new_inventory": "Understand JavaScript",
#         "links": [
#             {"label":"Option C", "id":"C"}
#         ]
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

# Get point adjustments from scene
def get_story_point_adjustments(scene):
    if "point_adjust" in scene:
        return scene["point_adjust"]
    else:
        return 0

# Get new inventory from scene
def get_story_new_inventory(scene):
    if "new_inventory" in scene:
        return scene["new_inventory"]
    else:
        return None

# Get links from scene
def get_story_links(scene):
    if "links" in scene:
        return scene["links"]
    else:
        return None
