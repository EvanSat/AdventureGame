from scenes.nodes import get_story_text, get_story_links

# Print the scene and options.
def print_scene(scene):
    text = get_story_text(scene)
    options_list = get_story_links(scene)

    print(text, "\n\n")
    count = 1
    for option in options_list:
        print("{}. {}".format(count,option["label"]))
        count += 1
