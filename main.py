import turtle
from turtle import Turtle, Screen
import pandas as pd


screen = Screen()
screen.title("U.S. States Game")
# screen.setup(width= , height=)
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()


def tur_class(state_names, x, y):
    tim = Turtle()
    tim.penup()
    tim.hideturtle()
    tim.goto(x, y)
    tim.color("black")
    tim.write(state_names, align="center", font=("Arial", 13, "normal"))


counter = 0
guessed_states = []
# Main loop

while len(guessed_states) < 50:
    answer = []
    answer_state = screen.textinput(title=f"Guess the State. {counter}/50", prompt="What's another state's name?")
    if answer_state is None or answer_state == "Exit":
        list_to_scv = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(list_to_scv)
        new_data.to_csv("states_to_learn.csv")
        break
    else:
        answer_state = answer_state.title()
        answer = data.loc[data["state"] == answer_state].values.tolist()

    if answer:
        answer_st = answer[0][0]
        answer_x = answer[0][1]
        answer_y = answer[0][2]
        if answer_st.lower() == answer_state.lower():
            tur_class(answer_st, answer_x, answer_y)
            counter += 1
            guessed_states.append(answer_state)
        else:
            pass


#
# with open("50_states.csv", "r") as csvfile:
#     data_read = csv.reader(csvfile)
#     for i in range(0, len(guessed_states)):
#         for row in data_read:
#             if row[0] != guessed_states[i]:
#                 dict_to_scv.append(row[0])
#
# # list_to_csv = {"State": dict_to_scv}
# print(dict_to_scv)

# data_to_csv = pd.DataFrame(list_to_scv, columns="States")
# data_to_csv.to_csv('learning_list.csv', index=False)

# with open("new_list")

screen.exitonclick()
