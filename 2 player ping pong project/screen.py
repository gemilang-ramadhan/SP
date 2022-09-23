from turtle import Turtle, Screen
from paddles import pod
from bolz import Ballz
from skor import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(height = 600, width = 800)
screen.title('pongs')
screen.tracer(0)

r_pod = pod(350, 0)
l_pod = pod(-350, 0)

ball = Ballz()

skors = Scoreboard()
skors.papan()

screen.listen()
screen.onkey(l_pod.up, 's')
screen.onkey(l_pod.down, 'd')
screen.onkey(r_pod.up, 'j')
screen.onkey(r_pod.down, 'k')


geming = True
while geming :
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280: 
        ball.wall()
    
    if ball.xcor() >= 330 and ball.distance(r_pod) <= 50 or ball.xcor() <= -330 and ball.distance(l_pod) <= 50:
        ball.paddle()


    if ball.xcor() >= 400:
        skors.plus_l()
        ball.rerun()
        
    if ball.xcor() <= -400:
        skors.plus_r()
        ball.rerun()

    
screen.exitonclick()

