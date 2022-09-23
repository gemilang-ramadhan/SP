import turtle as t
import random

screen = t.Screen()
screen.setup(width = 500, height = 400)

toise_color = ['purple', 'red', 'green', 'blue', 'black', 'yellow']
toise_coordinates = [-180, -108, -36, 36, 108, 180]
toise = []

for x in range(0,6):
    new_toise = t.Turtle(shape = 'turtle')
    new_toise.pu()
    new_toise.color(toise_color[x])
    new_toise.goto(x = -230, y = toise_coordinates[x])
    toise.append(new_toise)

ui = screen.textinput(title = 'Which turtle you think gonna win?', prompt = 'Choose a color').lower()

if ui:
    race = True

while race:
    for x in toise:
        distance = random.randint(0,10)
        x.fd(distance)
        if (x.xcor() + distance) >= 230:
            x_color = x.pencolor()
            if x_color == ui: 
                print(f'You won!')
            else:
                print(f'You lost! The winner is {x_color}!')
            race = False

screen.exitonclick()

