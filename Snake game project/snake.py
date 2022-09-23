import turtle as t
dt = 20
screen = t.Screen()
screen.listen()
class Snakey:
    def __init__(self): 
        self.toise_list = []
        
    def snake(self):
        x, y = 0, 0
        for n in range(0,3):
            toise = t.Turtle(shape = 'square')
            toise.color('white')
            toise.pu()
            toise.goto(x, y)
            self.toise_list.append(toise)
            x -= dt

    def tambah_snake(self):
        toise = t.Turtle(shape = 'square')
        toise.color('white')
        toise.pu()
        tambah_x = self.toise_list[-1].xcor()
        tambah_y = self.toise_list[-1].ycor()
        toise.goto(tambah_x, tambah_y)
        self.toise_list.append(toise)
    
    def move(self):
        for x in range(len(self.toise_list)-1, 0, -1):
            x_toise = self.toise_list[x-1].xcor()
            y_toise = self.toise_list[x-1].ycor()
            self.toise_list[x].goto(x_toise, y_toise)
        self.toise_list[0].fd(20)


    def reset(self):
        for x in self.toise_list:
            x.goto(1000,1000)
        self.toise_list.clear()
        self.snake()

    def wall(self):
        toise = t.Turtle()
        toise.ht()
        toise.color('white')
        toise.goto(0,0)
        toise.write('GAME OVER', False, align = 'center', font = ('Times-Roman', 20, 'bold'))
        

    def up(self):
        if self.toise_list[0].heading() != 270:
            self.toise_list[0].seth(90)
    

    def rt(self):
        if self.toise_list[0].heading() != 180:
            self.toise_list[0].seth(0)
        

    def lt(self):
        if self.toise_list[0].heading() != 0:
            self.toise_list[0].seth(180)
        

    def down(self):
        if self.toise_list[0].heading() != 90:
            self.toise_list[0].seth(270)
        
        
