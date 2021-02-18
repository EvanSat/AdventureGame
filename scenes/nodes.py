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

# Find the text in a story.
def get_story_text(scene):
    if "text" in scene:
        return scene["text"]
    else:
        return 'Uh oh! The story is missing...'
