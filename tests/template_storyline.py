#Story Background
print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

skill = 100

#Game Start number question
if age >= 18:
    print("Congrats, you are in the Computer Science Program!")

#Question 2 yes/no
    wants_to_play = input("Do you know the basics?? ").lower()

#Question 2 yes answer
    if wants_to_play == "yes":
        print("Great your skill level is", skill, ".")
        print("Let's start your classes.")

#Question 3 text based answer
        left_or_right = input("First choice... (1)Software Engineering or (2)Art History 1? Choose your class number. ")
        if left_or_right == "1":

#Question 4 text based answer
            ans = input("Ask a coding question from this clas? (for now type software) ")
            if ans == "software":
                print("Great job. You passed your class. Move on to your next steps.")
                skill -= 5

#Scoring Example
                if skill <= 0:
                    print("You might need to repeat this class before moving to the next step.")
                else:
                    print("Congrats you finished your first class. ")

#Question 4 failed answer
            else:
                print("Try again to move forward ")

#Question 3 failed answer
        else:
            print("Maybe Computer Science is not your first choice. Talk to a your advisor to make sure this is the right fit.")

#Question 2 no answer
    else:
        print("Come back when you are ready...")

#Game Start wrong answer
else:
    print("You are too young. Keep practicing and come back after highschool.")

    