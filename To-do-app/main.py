from tkinter import *
import sys
import time
from tkinter.ttk import *

def day(e):
    match e:
        case 0:
            return 'Monday'
        case 1:
            return 'Tuesday'
        case 2:
            return 'Wednesday'
        case 3:
            return 'Thursday'
        case 4:
            return 'Friday'
        case 5:
            return 'Saturday'
        case 6:
            return 'Sunday'
        case default:
            return 'error '+ e +' in day function'

screen = Tk()
screen.title('To Do')
screen.geometry('500x500')

wday = day(time.localtime().tm_wday)

t_label = Label(screen, background='lightgrey', font=('Ariel',20), text='     Welcome !\n Today is %s'%(wday))
t_label.pack()
t_label.configure(width='500', anchor='center')


canvas = Canvas(screen, width='500', height='10')
canvas.pack()
canvas.create_line(0,0,500,0,fill='black', width='5')


fram = []

for i in range(4):
    val = Frame(screen, width='300', height='100', border='2' )
    fram.append(val)

f_label1 = Label(fram[0], text='1st frame', background='red').pack()
f_label2 = Label(fram[1], text='2st frame', background='blue').pack()
f_label3 = Label(fram[2], text='3st frame', background='green').pack()
f_label4 = Label(fram[3], text='4st frame', background='yellow').pack()

for e in fram:
    e.pack()
screen.mainloop()