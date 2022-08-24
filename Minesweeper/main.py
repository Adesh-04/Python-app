from tkinter import *
from tkinter.ttk import *
from mine import *

screen = Tk()
screen.title('Minesweeper')
screen.geometry('720x600')
screen.resizable(False,False)

btn = []
win_condition = []
num = 5
  

def pressed(board,id):
    global score_label
    x = id[0]
    y = id[1]
    if board[x][y] == 'X':
        btn[x][y]['text'] = 'x'
        score_label.config(text = 'Lose')
    else:

        btn[x][y]['text'] = board[x][y]
    return i,j

win = board(num)
win = put_mines(win,num)
win,win_condition = put_mark(win,num,win_condition)

display(win)
print()

bgImg = PhotoImage(file = 'bac.png')
bgLabel = Label(screen,image=bgImg)
bgLabel.place(x=-2,y=-2)

score_label = Label(bgLabel,text=' SCORE ')
score_label.place(x=360,y=20,anchor=CENTER)

for i in range(5):
    btn.append([])
    for j in range(5):
        btn[i].append(Button(bgLabel,text='',command= lambda id=(i,j):  pressed(win,id)  ,width=5))
        btn[i][j].place(x=j*50, y=i*50)
        

screen.mainloop()


