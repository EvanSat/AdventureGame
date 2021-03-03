level_4 = [
    {
        "id": "Level4_SceneA",
        "text": "[[cyan]]"
                "You are feeling lucky and having a blast time. You made few connections and met the host - \n"
                "Jeremy. He is a very cool dude, even though he stayed in the same grade twice. It's almost 4 am, \n"
                "people are starting to leave. What's your plan?"
                "[[resetColor]]",
        "new_inventory": "Friend Jeremy",
        "links": [
            {
                "label": "Go home, it's getting too late",
                "id": "Level4_SceneC"
            }, {
                "label": "Shout \"a little party never killed nobody\" and join Jeremy in the dance battle",
                "id": "Level5_SceneF"
            }
        ]
    }, {
        "id": "Level4_SceneB",
        "text": "[[cyan]]"
                "You still have some time to prepare for an exam. Do you want to go through your notes?"
                "[[resetColor]]",
        "links": [
            {
                "label": "Go through the notes",
                "id": "Level5_SceneB"
            }, {
                "label": "Do something else before going to bed",
                "id": "Level5_SceneC"
            }
        ]
    }, {
        "id": "Level4_SceneC",
        "text": "[[cyan]]"
                "You didn't get enough time to sleep and you were late to class. To let you take the test \n"
                "the teacher told you to answer the following question: who wrote \"Crime and Punishment\"?"
                "[[resetColor]]",
        "links": [
            {
                "label": "Dostoevsky",
                "id": "Level5_SceneD"
            }, {
                "label": "Nabokov",
                "id": "Level5_SceneE"
            }
        ]
    }
]
