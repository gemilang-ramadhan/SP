import snake
import food
from turtle import Screen
import random
import time
import skor

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Snek')
screen.tracer(0, 0)
toise_list = []
my_snake = snake.Snakey()
my_snake.snake()
my_food = food.Food()
my_score = skor.Score()
my_score.scoreboard()

screen.listen()
screen.onkey(my_snake.up, 'w')
screen.onkey(my_snake.rt, 'd')
screen.onkey(my_snake.lt, 'a')
screen.onkey(my_snake.down, 's')

geming = True
while geming: 
    screen.update()
    time.sleep(0.15)
    my_snake.move()
    if abs(my_snake.toise_list[0].xcor()) == 300 or abs(my_snake.toise_list[0].ycor()) == 300:

        my_score.high_score()
        my_snake.reset()
    if my_snake.toise_list[0].distance(my_food) <= 15: 
        my_food.refresh()
        my_score.add_score()
        my_snake.tambah_snake()
    for x in my_snake.toise_list[1:]: 
        if my_snake.toise_list[0].distance(x) <= 5:

            my_score.high_score()
            my_snake.reset()
        
screen.exitonclick()