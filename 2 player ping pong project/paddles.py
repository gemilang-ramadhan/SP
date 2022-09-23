from turtle import Turtle

class pod(Turtle): 
    def __init__(self,x,y):
        super().__init__()
        self.shape('square')
        self.pu()
        self.color('white')
        self.shapesize(5, 1)
        self.goto(x, y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
