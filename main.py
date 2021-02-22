import os
from scenes.handle import print_scene
from scenes.nodes import get_scene_from_story, get_story_links
from stories.developer_adventure import story

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

    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

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
