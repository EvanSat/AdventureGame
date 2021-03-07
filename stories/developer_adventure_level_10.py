# TODO

level_10 = [
    {
        "id": "Level10_SceneA",
        "text": "[[cyan]]"
                "You are writing a thesis with your professor on new ways to use hashing algorithm. While doing so, \n"
                "you find something promising in the whole CS field that no one noticed before. Well, well, well.. \n"
                "you could change CS industry for better."
                "[[resetColor]]",
        "links": [
            {
                "label": "What's next?",
                "id": "Level11_SceneA",
                "requirements": ["Friend Johny"]
            }, {
                "label": "What's next?",
                "id": "Level11_SceneB"
                # Either BOTH friends or NEITHER friend...
                # "requirements": ["Friend Johny","Friend Kevin"]
            }, {
                "label": "What's next?",
                "id": "Level11_SceneC",
                "requirements": ["Friend Kevin"]
            }
        ]
    }, {
        "id": "Level10_SceneB",
        "text": "[[cyan]]"
                "It's always Friday at your place. What an impressive four years of school. You could definitely \n"
                "use what you have learned about CS in your bright future."
                "[[resetColor]]",
        "links": [
            {
                "label": "What's next?",
                "id": "Level11_SceneB",
                "requirements": ["Friend Johny"]
            }, {
                "label": "Earn money, money, money",
                "id": "Level11_SceneC"
                # Either BOTH friends or NEITHER friend...
                # "requirements": ["Friend Johny","Friend Kevin"]
            }, {
                "label": "What's next?",
                "id": "Level11_SceneE",
                "requirements": ["Friend Kevin"]
            }
        ]
    }, {
        "id": "Level10_SceneC",
        "text": "[[cyan]]"
                "You might not be the next Musk or Bezos, but did you really wanted to be one of them? Your \n"
                "experience and knowledge of CS open some doors for you. It's up to you to decide whether they \n"
                "are good or bad."
                "[[resetColor]]",
        "links": [
            {
                "label": "What's next?",
                "id": "Level11_SceneD",
                "requirements": ["Friend Johny"]
            }, {
                "label": "What's next?",
                "id": "Level11_SceneF",
                "requirements": ["Friend Kevin"]
            }, {
                "label": "What's next?",
                "id": "Level11_SceneE"
                # Either BOTH friends or NEITHER friend...
                # "requirements": ["Friend Johny","Friend Kevin"]
            }
        ]
    }
]
