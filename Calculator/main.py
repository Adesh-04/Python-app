
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry('500x520')
window.resizable(False,False)

window.title('Simple Calculator')

bgImg = PhotoImage(file = 'background.png')
bgLabel = Label(window, image=bgImg)
bgLabel.place(x = 0)

answer = Text(bgLabel, height = 5, width = 48 ,font = ('Calibri',15,'bold'))
answer.place(x = 10, y = 20 )

## DATA
eq = []
backup = []
is_valid = True


# Functions

def valid():
    global backup

    if is_valid == False:
        answer.delete('1.0',END)
        answer.insert(END,'Error\n')
        backup = eq[:]
        eq.clear()
        return -1
    return 0
        
def pressed(var):
    global is_valid,answer
    content = answer.get("1.0",END)
    if content == "Error\n":
        clr()
    else:
        try:
            if int(var):
                True
            eq.append(var)
            answer.insert(END,var)
            is_valid = True
                
        except:
            if var == " X ":
                eq.append('*')
                is_valid = False
                answer.insert(END,var)
            elif var == "+/-":
                if eq:
                    last = eq.pop()
                    last = '-'+last
                    eq.append(last)
                    content = answer.get("1.0",'end-2c')
                    answer.delete("1.0",END)
                    answer.insert(END,content)
                    answer.insert(END,last)
                
            elif var == "**2" or var == "**(1/2)":
                eq.append(var)
                answer.insert(END,var)
                if valid() == 0:
                    is_valid = True
                else:
                    is_valid = False

            else:
                eq.append(var)
                is_valid = False
                answer.insert(END,var)

def clr():
    eq.clear()
    answer.delete('1.0','end')

def rem():
    if eq:
        eq.pop()
    answer.delete('end-2c','end')

def equat():
    if valid() == -1:
        return -1
    stri = ''.join(eq)
    eq.clear()
    val = ''
    try:
        val = eval(stri)
        eq.append(str(val))
    except:
        val = 'Error\n'

    answer.delete('1.0','end')
    answer.insert(END,val)

    




Button(bgLabel, text ='%', command = lambda : pressed('%')  ).place(x = 15 , y = 150, width = 110, height = 50)
Button(bgLabel, text ='!', command = lambda : pressed('!')  ).place(x = 135, y = 150, width = 110, height = 50)
Button(bgLabel, text ='C', command = clr                    ).place(x = 255, y = 150, width = 110, height = 50)
Button(bgLabel, text ='<-', command = rem                   ).place(x = 375, y = 150, width = 110, height = 50)

Button(bgLabel, text ='1/x', command = lambda : pressed('1/')          ).place(x = 15 , y = 210, width = 110, height = 50)  
Button(bgLabel, text ='x**2', command = lambda : pressed('**2')        ).place(x = 135, y = 210, width = 110, height = 50)  
Button(bgLabel, text ='x**(1/2)', command = lambda : pressed('**(1/2)')).place(x = 255, y = 210, width = 110, height = 50)  
Button(bgLabel, text ='/', command = lambda : pressed(' / ')           ).place(x = 375, y = 210, width = 110, height = 50)

Button(bgLabel, text ='7', command = lambda : pressed('7')  ).place(x = 15 , y = 270, width = 110, height = 50)
Button(bgLabel, text ='8', command = lambda : pressed('8')  ).place(x = 135, y = 270, width = 110, height = 50)
Button(bgLabel, text ='9', command = lambda : pressed('9')  ).place(x = 255, y = 270, width = 110, height = 50)
Button(bgLabel, text ='X', command = lambda : pressed(' X ')).place(x = 375, y = 270, width = 110, height = 50)

Button(bgLabel, text ='4', command = lambda : pressed('4')  ).place(x = 15 , y = 330, width = 110, height = 50)
Button(bgLabel, text ='5', command = lambda : pressed('5')  ).place(x = 135, y = 330, width = 110, height = 50)
Button(bgLabel, text ='6', command = lambda : pressed('6')  ).place(x = 255, y = 330, width = 110, height = 50)
Button(bgLabel, text ='-', command = lambda : pressed(' - ')).place(x = 375, y = 330, width = 110, height = 50)

Button(bgLabel, text ='1', command = lambda : pressed('1')  ).place(x = 15 , y = 390, width = 110, height = 50)
Button(bgLabel, text ='2', command = lambda : pressed('2')  ).place(x = 135, y = 390, width = 110, height = 50)
Button(bgLabel, text ='3', command = lambda : pressed('3')  ).place(x = 255, y = 390, width = 110, height = 50)
Button(bgLabel, text ='+', command = lambda : pressed(' + ')).place(x = 375, y = 390, width = 110, height = 50)

Button(bgLabel, text ='+/-', command = lambda : pressed('+/-')).place(x = 15 , y = 450,width = 110, height = 50)
Button(bgLabel, text ='0',   command = lambda : pressed('0')  ).place(x = 135, y = 450,width = 110, height = 50)
Button(bgLabel, text ='.',   command = lambda : pressed('.')  ).place(x = 255, y = 450,width = 110, height = 50)
Button(bgLabel, text ='=',   command = equat                  ).place(x = 375, y = 450,width = 110, height = 50)



    
window.mainloop()