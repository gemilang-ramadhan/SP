from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self): 
        super().__init__()
        self.pu()
        self.ht()
        self.color('white')
        self.goto(0,260)
        self.score_r = 0
        self.score_l = 0
        self.papan()
    
    def papan(self): 
        self.write(f'{self.score_l} || {self.score_r}', False, align = 'center', font = ('Times-Roman', 20, 'bold'))
    
    def plus_r(self):
        self.score_r += 1
        self.clear()
        self.papan()
    
    def plus_l(self):
        self.score_l += 1
        self.clear()
        self.papan()

        