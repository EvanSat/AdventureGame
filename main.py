import os
from scenes.handle import print_scene, text_color
from scenes.nodes import get_scene_from_story, get_story_links, get_story_new_inventory, get_story_point_adjustments
from stories.developer_adventure import story

def handle_scene(choice, current_scene, previous_scene, inventory, total_points):
    if choice == -1:
        print("SETTING START SCENE")
        # Set the start scene as current
        current_scene = story[0]
    else:
        choice_index = choice - 1
        options = get_story_links(current_scene, inventory)
        option_id = options[choice_index]["id"]
        if option_id == "EXIT":
            print("\n\nTHANKS FOR PLAYING!\n\n")
            # Exit the game
            return False
        else:
            current_scene = get_scene_from_story(story, option_id)
            if current_scene == None:
                current_scene = previous_scene

    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Handle and store new inventory
    new_inventory_string = get_story_new_inventory(current_scene)
    if isinstance(new_inventory_string, str):
        inventory = inventory + [new_inventory_string]

    # Handle and store point adjustments
    new_point_adjustment = get_story_point_adjustments(current_scene)
    if isinstance(new_point_adjustment, int):
        total_points = total_points + new_point_adjustment

    if previous_scene == current_scene and choice != -1:
        print(text_color("[[red]]There was an error fetching next scene. Try again.\n[[resetColor]]"))

    print_scene(current_scene)

    try:
        selection = int(input('\nSelect option above using number: '))
    except ValueError:
        pass

    previous_scene = current_scene
    handle_scene(selection, current_scene, previous_scene, inventory, total_points)


def main():
    total_points = 0
    inventory = []
    handle_scene(-1, story[0], story[0], inventory, total_points)

if __name__ == '__main__':
    main()
