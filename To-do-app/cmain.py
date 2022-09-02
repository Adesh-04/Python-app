from tkinter import *
from tkinter.ttk import *
import time

class App():
    def __init__(self):
        self.screen = Tk()
        self.screen.title('To Do')
        self.screen.geometry('500x500')
        self.screen.resizable(False,False)
        self.wday = self.getDay(time.localtime().tm_wday)
        self.title()
        self.line(0,70)
        self.frames = []
        self.labels = {}
        self.sizeofBox = 0

    def getDay(self,e):
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

    def title(self):
        t_label = Label(self.screen, background='lightgrey', font=('Ariel',20), text='     Welcome !\n Today is %s'%(self.wday))
        t_label.place(x = 0, y = 5, width = 500)
        t_label.configure(width='500', anchor='center')
    
    def line(self,x,y):
        canvas = Canvas(self.screen, width='500', height='10')
        canvas.place(x = x, y = y)
        canvas.create_line(0,0,500,0,fill='black', width='5')

    def newFrame(self,f):
        size = self.getFrames()
        val = Frame(self.screen, border='2')
        self.frames.append(val)
        self.labels[size] = []
        val.place(x=0,y=100 * (f+1),width=500,height=100)
        self.line(0,100 * (f+1))

    def newBox(self,txt,date,time,info = None):

        f = self.sizeofBox
        self.newFrame(f=f)
        n = self.frames[f]
        
        val = Label(n, background='lightgrey')
        val.place(x=40,y=0, width=440,height=150)

        val1 = Label(n, text=txt )
        val2 = Label(n, text=date )
        val3 = Label(n, text=time )
        val4 = Label(n, text=info )

        self.labels[f] += [val1,val2,val3,val4]

        val3.place(x=0 , y=5, height= 20)
        val1.place(x=100 , y=5, height= 20)
        val2.place(x=410 , y=5, height= 20, width=65)
        val4.place(x=50 , y=40, height= 50, width=400)

        self.sizeofBox += 1 


        

    def getFrames(self):
        return len(self.frames)

    def getLabels(self,f):
        val = self.labels[f]
        return len(val)

    def debug(self):
        for e in self.frames:
            print(e)
        for e in self.labels:
            print(e,end=' : ')
            print(self.labels.get(e))
        print(self.sizeofBox)


if __name__ == '__main__':

    curr_date = '21/03/2022'
    curr_time = '13:43'

    tttt = 'sadjbqi d qdqnd qdq damdoajbc abdadn'

    app = App()
    app.newBox('My 1st',curr_date,curr_time,tttt)
    app.newBox('My 1st',curr_date,curr_time,tttt)
    app.debug()

    app.screen.mainloop()

    