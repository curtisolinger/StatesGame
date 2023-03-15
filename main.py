import turtle
import pandas
from state_name import StateName

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
correct_guesses = 0
state_list = []
continue_mapping = True
while continue_mapping:
    if correct_guesses == 0:
        TITLE = "Guess the State"
    elif correct_guesses < 50:
        TITLE = f"{correct_guesses}/50 States Correct"
    else:
        TITLE = f"{correct_guesses}/50 States Correct. You win!"
        continue_mapping = False
    answer_state = screen.textinput(title=TITLE,
                                    prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break
    elif answer_state in data.state.unique():
        x_cor = int(data.x[data.state == answer_state])
        y_cor = int(data.y[data.state == answer_state])
        state_name = StateName(answer_state, x_cor, y_cor)
        correct_guesses += 1
        state_list.append(answer_state)

missing_states = [state for state in data.state.unique() if state not in state_list]

missing_states_df = pandas.DataFrame(missing_states)
missing_states_df.to_csv('missing_states.csv', index=False)
# screen.exitonclick()
