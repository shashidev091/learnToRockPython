import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')


answer_state = screen.textinput(title="Guess the state", prompt="What is another state's name?").title()

all_states = data['state'].to_list()
print(answer_state.title(), answer_state in all_states)
print(all_states)

if answer_state in all_states:
    print(answer_state)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state.item())


def get_mouse_click_co_or(x, y):

    print(x, y)


turtle.onscreenclick(get_mouse_click_co_or)

# turtle.mainloop()
screen.exitonclick()
