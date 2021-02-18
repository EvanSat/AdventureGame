import os
from scenes.handle import print_scene
from scenes.nodes import get_scene_from_story, get_story_links

# Sample story. TODO: Store this in a separate file.
story = [
    {
        "id": "A",
        "text": "this is the story text",
        "point_adjust": 105,
        "new_inventory": "Friend Ethan",
        "links": [
            {"label":"Option B", "id":"B"},
            {"label":"Option C", "id":"C"}
        ]
    },{
        "id": "B",
        "text": "story b",
        "point_adjust": 10,
        "new_inventory": "Understand JavaScript",
        "links": [
            {"label":"Option C", "id":"C"}
        ]
    },{
        "id": "C",
        "text": "story c",
        "point_adjust": 15
        "links": [
            {"label":"THE END", "id":"D"}
        ]
    }
]

def handle_scene(choice, current_scene):
    if choice == -1:
        # Print start scene
        # TODO: print the start screen
        current_scene = story[0]
    else:
        choice_index = choice - 1
        options = get_story_links(current_scene)
        option_id = options[choice_index]["id"]
        current_scene = get_scene_from_story(story, option_id)

    # Clear Screen
    # os.system("cls") # TODO: This doesn't clear on Mac ("clear")

    # TODO: handle and store new inventory
    # TODO: handle and store point adjustments

    print_scene(current_scene)

    try:
        selection = int(input('\nSelect option above using number: '))
    except ValueError:
        pass

    handle_scene(selection, current_scene)


def main():
    handle_scene(-1, story[0])

if __name__ == '__main__':
    main()
