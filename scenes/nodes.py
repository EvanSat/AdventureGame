# Expected Node Structure
# =======================
# scene_array = [
#     {
#         "id": "A",
#         "text": "this is the story text",
#         "point_adjust": 100,
#         "new_inventory": "Friend Maria",
#         "links": [
#             {"label":"Option B", "id":"B", "requirements":"Maria"},
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

# Find the file in a story.
def get_story_file(scene):
    if "file" in scene:
        return scene["file"]
    else:
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
def get_story_links(scene, user_inventory=[]):
    limited_scenes = []
    if "links" in scene:
        
        # Check for requirements in any links
        for link in scene["links"]:

            # If there's a requirement for the scene, 
            # check if user meets the requirement
            if "requirements" in link:

                # Iterate through requirements
                for requirement in link["requirements"]:
                    if requirement in user_inventory:
                        limited_scenes.append(link)
                        break
            
            # If there's no requirement, give it as an option.
            else:
                limited_scenes.append(link)

        # Return limited scenes that match requirements
        return limited_scenes
    else:
        return None
