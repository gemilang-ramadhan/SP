from turtle import Turtle
import time
class Ballz(Turtle):
    def __init__(self): 
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.cor_x = 10
        self.cor_y = 10
        self.speed = 0.1 

    def move(self):
        x = self.xcor() + self.cor_x
        y = self.ycor() + self.cor_y
        self.goto(x, y)

    def wall(self):
        self.cor_y *= -1

    def paddle(self): 
        self.cor_x *= -1
        self.speed *= 0.7
    
    def rerun(self):
        self.goto(0,0)
        self.speed = 0.1
        self.paddle()
        
