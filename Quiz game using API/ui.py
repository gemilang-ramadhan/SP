from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"
green = '#32CD32'
white = '#FFFFFF'
red = '#ff0000'
class GUI():
    def __init__(self, ques: QuizBrain):
        self.q = ques

        self.windows = Tk()
        self.windows.title('QUIZZZZZ')
        self.windows.config(padx = 20, pady=20, bg=THEME_COLOR)

        #score
        self.score = 0
        self.score_text = Label(text = f'Score : {self.score}', font = ('arial', '12', 'bold'), bg = THEME_COLOR, fg ='white')
        self.score_text.grid(row = 0, column = 1, padx = 20, pady = 20)

        #canvas
        self.canvas = Canvas(width = 300, height = 250, highlightthick =0)
        self.quiz_text = self.canvas.create_text(150, 125, text = self.q.next_question(), font = ('arial', '20', 'italic'), width = 280)
        self.canvas.grid(row = 2, column = 0, columnspan = 2, padx = 20, pady = 20)

        #botan
        self.t = PhotoImage(file = r'day 34\images\true.png')
        self.f = PhotoImage(file = r'day 34\images\false.png')

        self.true_botan = Button(image = self.t, command = self.betul)
        self.true_botan.grid(row = 3, column = 0, padx = 20, pady = 20)
        self.false_botan = Button(image = self.f, command = self.salah)
        self.false_botan.grid(row = 3, column = 1, padx = 20, pady = 20)


        self.windows.mainloop()

    def questions(self):
        try:
            pertanyaan = self.q.next_question()
        except IndexError:
            self.canvas.itemconfig(self.quiz_text, text = 'No more questions available')
        else:
            self.canvas.itemconfig(self.quiz_text, text = pertanyaan)
    
    def betul(self): 
        betul_kah = self.q.check_answer('True')
        if betul_kah == True: 
            self.canv_r()
            self.score += 1
            self.score_text.config(text = f'Score : {self.score}')
        else:
            self.canv_w()
        
        self.questions()
    
    def salah(self):
        salah_kah = self.q.check_answer('False')
        if salah_kah == True: 
            self.canv_r()
            self.score += 1
            self.score_text.config(text = f'Score : {self.score}')
        else:
            self.canv_w()
        self.questions()


    def canv_r(self): 
        self.canvas.config(bg = green)
        time.sleep(0.5)
        self.canvas.config(bg = white)

    def canv_w(self):
        self.canvas.config(bg = red)
        time.sleep(0.5)
        self.canvas.config(bg = white)