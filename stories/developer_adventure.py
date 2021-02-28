from stories.developer_adventure_level_1 import level_1
from stories.developer_adventure_level_2 import level_2
from stories.developer_adventure_level_3 import level_3
from stories.developer_adventure_level_4 import level_4
from stories.developer_adventure_level_5 import level_5
from stories.developer_adventure_level_6 import level_6
from stories.developer_adventure_level_7 import level_7
from stories.developer_adventure_level_8 import level_8
from stories.developer_adventure_level_9 import level_9
from stories.developer_adventure_level_10 import level_10
from stories.developer_adventure_level_11 import level_11

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

story = start_scene + level_1 + level_2 + level_3 + level_4 + level_5 + level_6 + level_7 + level_8 + level_9 + \
        level_10 + level_11
