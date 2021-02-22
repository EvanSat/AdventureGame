from scenes.nodes import get_story_file, get_story_text, get_story_links

# Print the scene and options.
def print_scene(scene):
    # Check for a file!
    file = get_story_file(scene)

    if file != None:
        # Open the file
        f = open(file, "r", encoding="utf8")

        # translates file into string
        text = "".join(f.readlines())

        # print(text_color(game_title))
    else:
        text = get_story_text(scene)

    options_list = get_story_links(scene)

    print(text, "\n\n")
    count = 1
    for option in options_list:
        print("{}. {}".format(count,option["label"]))
        count += 1
