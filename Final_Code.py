from ast import Lambda
from optparse import Option
from tkinter import *
from turtle import width

Questions = ["Which NFL team is known as America's Team?",
             "Which current team began as the Houston Oilers?",
             "What city did the Indianapolis Colts relocate from?"]

Options = [["Stealers", "Cowboys", "Raiders"],
           ["Titans", "Texans", "Browns"],
           ["Cleveland", "St.Louis", "Baltimore"]]

Answers = [2, 1, 3]

Score = 0
Total_No_Questions = 3
Question_no = 1


def start_again():
    global Score, Question_no

    Score = 0
    Question_no = 1
    val1.set(0)
    val2.set(0)
    val3.set(0)
    question.config(text=Questions[Question_no - 1])
    option1.config(text=Options[Question_no - 1][0])
    option2.config(text=Options[Question_no - 1][1])
    option3.confiig(text=Options[Question_no - 1][2])
    next_button.config(text="Next")
    play_again.place_forget()
    score.place_forget()
    root.pack()


def next():
    global Score, Question_no
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    else:
        selected_option = -1

    if Answers[Question_no - 1] == selected_option:
        Score += 1

    Question_no += 1

    if Question_no > Total_No_Questions:
        root.pack_forget()
        score.place(relx=.5, rely=.5, anchor=CENTER)
        play_again.place(relx=.45, rely=.1)

        score.config(text="Score:" + str(Score))

    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        question.config(text=Questions[Question_no - 1])
        option1.config(text=Options[Question_no - 1][0])
        option2.config(text=Options[Question_no - 1][1])
        option3.config(text=Options[Question_no - 1][2])


def check(option):
    if option == 1:
        val2.set(0)
        val3.set(3)
    elif option == 2:
        val1.set(0)
        val3.set(0)
    else:
        val2.set(0)
        val1.set(0)


def start_game():
    user_screen.place_forget()
    root.pack()


Win = Tk()
Win.geometry("600x150")
Win.title("Kelsey's Quiz Game")

user_screen = Frame()
user_screen.place(relx=.5, rely=.5, anchor=CENTER)

intro_message = Label(user_screen, text="Welcome to the Quiz Show!", font=("Arial", 14), width=50)
intro_message.pack()

play_button = Button(user_screen, text="Press Play", command=start_game)
play_button.pack()

root = Frame()
root.pack_forget()

question = Label(root, width=50, font=12, text=Questions[0])
question.pack()

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()

option1 = Checkbutton(root, variable=val1, text=Options[0][0], command=lambda: check(1))
option1.pack()

option2 = Checkbutton(root, variable=val2, text=Options[0][1], command=lambda: check(2))
option2.pack()

option3 = Checkbutton(root, variable=val3, text=Options[0][2], command=lambda: check(3))
option3.pack()

next_button = Button(root, text="Next", command=next)
next_button.pack()

score = Label(Win)
score.place_forget()

play_again = Button(Win, text="Play Again", command=start_again)
play_again.place_forget()

exit_button = Button(root, text="Exit", command=exit)
exit_button.pack()
Win.mainloop()
