from turtle import Turtle


class Score(Turtle): 
    def __init__(self):
        super().__init__()
        self.skor = 0
        with open('C:\Project File\Python program\PYTHON COURSE\Code\day 20\data.txt') as file:
            self.hs = int(file.read())
        self.ht()
        self.color('white')
        self.pu()
        self.goto(0,280)
        self.scoreboard()
    
    def scoreboard(self):
        self.clear()
        self.write(f'Score : {self.skor} || High Score : {self.hs}', False, align = 'center', font = ('Times-Roman', 12, 'bold'))
    
    def high_score(self):
        if self.skor >= self.hs:
            self.hs = self.skor
            with open('C:\Project File\Python program\PYTHON COURSE\Code\day 20\data.txt', 'w') as file:
                file.write(f'{self.skor}')
        self.skor = 0
        self.scoreboard()

    def add_score(self):
        self.skor += 1
        self.scoreboard()

