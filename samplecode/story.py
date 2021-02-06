import os
import time
import sys
import start_screen


def story_selection():
    selection = int()

    try:
        selection = int(input('Select option above using number: '))
    except ValueError:
        pass

    if selection == 1:
        os.system("cls")
        return 1
    elif selection == 2:
        os.system("cls")
        return 2
    elif selection == 3:
        os.system("cls")
        return 3
    elif selection == 4:
        os.system("cls")
        return 4


def story_line(choice):
    x = choice
    os.system("cls")

    if x == 10:
        print("L1. You are a highschool student with an interest to create new things. You live with your parents \n"
              "and have a do named Mai lo. Your best friend Katy is in the same lass with you. She likes music and \n"
              "plans to become a producer. You have an uncle who is a pen tester and you think he is cool. You still \n"
              "have 3 months to figure out what you want to do. It's an early night and it's getting boring.\n\n\n"
              "Options: 1. Check Social Media\n"
              "         2. Prepare for the next week literature\n"
              "         3. Play World of Warcraft with friends\n"
              "         4. Go to sleep\n")
        response = story_selection()
        if response == 1:
            story_line(20)
        elif response == 2:
            story_line(21)
        elif response == 3:
            story_line(22)
        elif response == 4:
            story_line(23)
        else:
            story_line_no_option(x)

    elif x == 20:
        print("L2. You got a message from Katy. She is inviting you to a party. You do not know the host, but at \n"
              "least you know Katy.\n\n\n"
              "Options: 1. Decline the invite, say that you are too busy studying for the literature test\n"
              "         2. Ignore the invite and continue browsing social media\n"
              "         3. Accept the invite and go have some fun\n")
        response = story_selection()
        if response == 1:
            story_line(42)
        elif response == 2:
            story_line(30)
        elif response == 3:
            story_line(31)
        else:
            story_line_no_option(x)

    elif x == 21:
        print("L2. You studied well. Even remembered that Ernest Hemming way hated the original cover of \n"
              "Fitzgerald's The Great Gatsby. You feel confident that you will pass the test. It's getting late..."
              "\n\n\n"
              "Options: 1. Go to Sleep\n"
              "         2. Check social media\n")
        response = story_selection()
        if response == 1:
            story_line(42)
        elif response == 2:
            story_line(30)
        else:
            story_line_no_option(x)

    elif x == 22:
        print("L2. Wow that was fun. Going scavenger hunting around Pandaria was fun. You had a blast and got to \n"
              "know your online friend, Kevin, better. The gang went to sleep.\n\n\n"
              "Options: 1. Go to sleep\n"
              "         2. Continue playing the game\n")
        response = story_selection()
        if response == 1:
            story_line(42)
        elif response == 2:
            story_line(32)
        else:
            story_line_no_option(x)

    elif x == 23:
        # TODO pending story line development
        print("L2. Full 8 hours of healthy sleep. What could be better?\n\n\n"
              "Options: 1. \n"
              "         2. \n"
              "         3. \n"
              "         4. \n")
        response = story_selection()
        if response == 1:
            # TODO story_line(__) & Remove 'PASS'
            pass
        elif response == 2:
            # TODO story_line(__) & Remove 'PASS'
            pass
        elif response == 3:
            # TODO story_line(__) & Remove 'PASS'
            pass
        elif response == 4:
            # TODO story_line(__) & Remove 'PASS'
            pass
        else:
            story_line_no_option(x)

    elif x == 30:
        print("L3. Time passes by quickly. You found Johny who you used to go to middle school together. \n"
              "You have not seen him in a couple of years. He moved to Amsterdam with his family. You sent \n"
              "a friend request.\n\n\n"
              "Options: 1. Go to sleep\n"
              "         2. Keep on scrolling social media\n")
        response = story_selection()
        if response == 1:
            story_line(42)
        elif response == 2:
            story_line(43)
        else:
            story_line_no_option(x)

    elif x == 31:
        print("L3. You get to the house but don't see anyone you might know.\n\n\n"
              "Options: 1. You don't want to go inside without knowing anyone and decide to go home\n"
              "         2. Wait for Katy to arrive\n"
              "         3. Go inside and have some fun\n")
        response = story_selection()
        if response == 1:
            story_line(42)
        elif response == 2:
            story_line(40)
        elif response == 3:
            story_line(41)
        else:
            story_line_no_option(x)

    elif x == 32:
        print("L3. You found a group to play together but that didn't feel good. You decide to go solo and have some \n"
              "nostalgia so you took a trip to see to Chromie (game character).\n\n\n"
              "Options: 1. Keep playing through the night\n")
        response = story_selection()
        if response == 1:
            story_line(43)
        else:
            story_line_no_option(x)

    elif x == 40:
        print("L4. An hour passes by, you cannot get a hold of Katy.\n\n\n"
              "Options: 1. Go home, it's getting too late\n"
              "         2. There is still time to go inside and have fun\n")
        response = story_selection()
        if response == 1:
            story_line(42)
        elif response == 2:
            story_line(41)
        else:
            story_line_no_option(x)

    elif x == 41:
        print("L4. You are feeling lucky and having a blast time. You made a few connections. Now you know Tonya who \n"
              "is a senior that got admitted to ASU for BioEngineering. It's almost 4 am and people are starting to\n"
              "leave.\n\n\n"
              "Options: 1. Go home, it's getting too late\n"
              "         2. You studied hard, so you keep partying\n")
        response = story_selection()
        if response == 1:
            story_line(43)
        elif response == 2:
            story_line(44)
        else:
            story_line_no_option(x)

    elif x == 42:
        # TODO pending story line development
        print("L4. You got 6 hours of sleep, not terrible but it could be better!\n\n\n"
              "Options: 1. \n"
              "         2. \n"
              "         3. \n"
              "         4. \n")
        response = story_selection()
        if response == 1:
            # TODO story_line(__) & Remove 'PASS'
            pass
        elif response == 2:
            # TODO story_line(__) & Remove 'PASS'
            pass
        elif response == 3:
            # TODO story_line(__) & Remove 'PASS'
            pass
        elif response == 4:
            # TODO story_line(__) & Remove 'PASS'
            pass
        else:
            story_line_no_option(x)

    elif x == 43:
        # TODO pending story line development
        print("L4. Oh my, you only got 2 hours of sleep. You don't feel as if you got any sleep at all.\n\n\n"
              "Options: 1. \n"
              "         2. \n"
              "         3. \n"
              "         4. \n")
        response = story_selection()
        if response == 1:
            # TODO story_line(__) & Remove 'PASS'
            pass
        elif response == 2:
            # TODO story_line(__) & Remove 'PASS'
            pass
        elif response == 3:
            # TODO story_line(__) & Remove 'PASS'
            pass
        elif response == 4:
            # TODO story_line(__) & Remove 'PASS'
            pass
        else:
            story_line_no_option(x)

    elif x == 44:
        # TODO pending story line development
        print("L4. You are the last one to leave the party. You finally met the host, Jeremy. You learn that he is \n"
              "on the basketball team and seems like a cool dude. Time has past quickly and before you know, it is \n"
              "already 7 am. No time to sleep, so you go home to quickly change and head to school.\n\n\n"
              "Options: 1. \n"
              "         2. \n"
              "         3. \n"
              "         4. \n")
        response = story_selection()
        if response == 1:
            # TODO story_line(__) & Remove 'PASS'
            pass
        elif response == 2:
            # TODO story_line(__) & Remove 'PASS'
            pass
        elif response == 3:
            # TODO story_line(__) & Remove 'PASS'
            pass
        elif response == 4:
            # TODO story_line(__) & Remove 'PASS'
            pass
        else:
            story_line_no_option(x)

    # elif x == 999:
    #     # TODO
    #     print("")
    #     response = story_selection()
    #     if response == 1:
    #         # TODO story_line(__) & Remove 'PASS'
    #         pass
    #     elif response == 2:
    #         # TODO story_line(__) & Remove 'PASS'
    #         pass
    #     elif response == 3:
    #         # TODO story_line(__) & Remove 'PASS'
    #         pass
    #     elif response == 4:
    #         # TODO story_line(__) & Remove 'PASS'
    #         pass
    #     else:
    #         story_line_no_option(x)
    #
    # elif x == 999:
    #     # TODO
    #     print("")
    #     response = story_selection()
    #     if response == 1:
    #         # TODO story_line(__) & Remove 'PASS'
    #         pass
    #     elif response == 2:
    #         # TODO story_line(__) & Remove 'PASS'
    #         pass
    #     elif response == 3:
    #         # TODO story_line(__) & Remove 'PASS'
    #         pass
    #     elif response == 4:
    #         # TODO story_line(__) & Remove 'PASS'
    #         pass
    #     else:
    #         story_line_no_option(x)


def story_line_no_option(x):
    print(start_screen.text_color("[[red]]"))
    for i in range(4):
        sys.stdout.write("\r" + " "*i + "."*(3-i) + "That\'s not an option! Please pick again using an integer." +
                         "."*(3-i) + " "*i)

        # inserted error sound since the timings did not match | commented out
        # if i == 0:
        #     start_screen.error_sound()
        time.sleep(1)
    print(start_screen.text_color("[[resetColor]]"))

    os.system("cls")
    story_line(x)


def story_line_root():
    story_line(10)


def main():
    story_line_root()


if __name__ == '__main__':
    main()
