import os
import time
import winsound
import story

os.system("cls")

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


def title_screen():
    # reads text file
    f = open("Ascii Game Title - The Great Developer Adventure.txt", "r", encoding="utf8")

    # translates file into string
    game_title = "".join(f.readlines())

    print(text_color(game_title))


def title_screen_selection():
    selection = int()

    try:
        selection = int(input('Select option above using number: '))
    except ValueError:
        print(text_color("\n[[red]]Please input an integer only [[resetColor]]\n"))
        #error_sound()
        title_screen_selection()

    if selection == 1:
        os.system("cls")
        story.main()
    elif selection == 2:
        os.system("cls")
        print('GameInfo_TODO')
    elif selection == 3:
        print('EXITING')
        time.sleep(1)
        os.system("cls")
    else:
        print(text_color('\n[[red]]That\'s not an option! Please pick again [[resetColor]] \n'))
        #error_sound()
        title_screen_selection()


# def title_screen_sound():
#     sound_file1 = 'PinkPanther30.wav'
#     winsound.PlaySound(sound_file1, winsound.SND_FILENAME)
#
#
# def error_sound():
#     sound_file2 = 'vintage-error-alert-1-2.wav'
#     winsound.PlaySound(sound_file2, winsound.SND_FILENAME)


def main():
    title_screen()
    title_screen_selection()


if __name__ == '__main__':
    main()
