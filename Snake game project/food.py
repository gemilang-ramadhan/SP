from turtle import Turtle
import random as rnd

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.pu()
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        self.shapesize(0.5,0.5)
        self.goto(rnd.randint(-280,280), rnd.randint(-280,280))


