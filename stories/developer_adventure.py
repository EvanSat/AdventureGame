story = [
    {
        "id": "Level1_SceneA",
        "text": "Level 1 text\nthis is the story text",
        "point_adjust": 105,
        "new_inventory": "Friend Ethan",
        "links": [
            {"label":"Option B", "id":"Level2_SceneA"},
            {"label":"Option C", "id":"Level3_SceneA"}
        ]
    },{
        "id": "Level2_SceneA",
        "text": "Level 2 text\nstory b",
        "point_adjust": 10,
        "new_inventory": "Understand JavaScript",
        "links": [
            {"label":"Option C", "id":"Level3_SceneA"}
        ]
    },{
        "id": "Level3_SceneA",
        "text": "Level 3 text\nstory c",
        "point_adjust": 15,
        "links": [
            {"label":"THE END", "id":"Level1_SceneA"}
        ]
    }
]
