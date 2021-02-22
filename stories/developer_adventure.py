from stories.developer_adventure_level_1 import level_1
from stories.developer_adventure_level_2 import level_2
from stories.developer_adventure_level_3 import level_3

start_scene = [
    {
        "id": "START",
        "file": "stories/files/developer_adventure_start.txt",
        "links": [
            {
                "label": "Start",
                "id": "Level1_SceneA"
            }, {
                "label": "Game Info",
                "id": "GAME_INFO"
            }, {
                "label": "Exit",
                "id": "EXIT"
            }
        ]
    },{
        "id": "GAME_INFO",
        "file": "stories/files/developer_adventure_info.txt",
        "links": [
            {
                "label": "Return to Title Screen",
                "id": "START"
            }
        ]
    }
]

story = start_scene + level_1 + level_2 + level_3
