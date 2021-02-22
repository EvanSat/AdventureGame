from scenes.nodes import get_story_file, get_story_text, get_story_links

COLORS = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "resetColor": "\u001b[0m",
    "backGroundWhite": "\u001b[47m"
}

def text_color(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

# Print the scene and options.
def print_scene(scene):
    # Check for a file!
    file = get_story_file(scene)

    if file != None:
        # Open the file
        f = open(file, "r", encoding="utf8")

        # translates file into string
        text = "".join(f.readlines())
    else:
        text = get_story_text(scene)

    options_list = get_story_links(scene)

    print(text_color(text), "\n\n")
    count = 1
    for option in options_list:
        print("{}. {}".format(count,option["label"]))
        count += 1
