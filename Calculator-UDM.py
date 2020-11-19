#!/home/itachi/anaconda3/bin/python3
from tkinter import *
import tkinter

root = Tk()
root.geometry("430x580")
root.minsize(400,560)
root.maxsize(450,600)
root.title("Calculator-UDM")


# Functionality

text = ""
result = ""
oprnd1 = ""
oprnd2 = ""
oprn = ""

def calculate(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == "/":
        if b == 0:
            return 'ERROR'
        else:
            return a/b
    else:
        return a

def click(event):
    # taking out thetext from a widget...
    global text, result, oprnd1, oprnd2, oprn
    opr1 = event.widget.cget("text")
    if opr1 == 'C':
        text = ""
        oprnd1, oprnd2, result, oprn = "","","",""
        e1.set("")

    elif opr1 == '=':
        oprnd2 = text
        result = calculate(float(oprnd1),float(oprnd2),oprn)
        e1.set(result)
        oprnd1 = result
        oprnd2 = ""
        text = ""
        oprn = ""

    elif opr1 == '+' or opr1 == '-' or opr1 == '*' or opr1 == '/':
        oprn = opr1
        if oprnd1 == "":
            oprnd1 = text
            text = ""
            e1.set("")
        else:
            oprnd2 = text
            oprnd1 = calculate(float(oprnd1),float(oprnd2),oprn)
            e1.set(str(oprnd1))
            text=""
            


    else:
        text += opr1
        e1.set(text)


# SCREEN
e1 = StringVar()
e1.set("")
screen = Entry(root, textvar=e1, font="lucida 30 bold",
            borderwidth=5, relief=SUNKEN, state=DISABLED)
screen.pack(side=TOP, fill=X, padx=5, ipadx=10, pady=10, ipady=5)


screen.configure({'disabledforeground':'black'})

# Status Bar
statevar = StringVar()
statevar.set("Ready")
statusbar = Label(root, bg="grey", fg="red", font="lucida 12 bold",
                  textvariable=statevar, anchor=W, borderwidth=3, relief=RAISED)
statusbar.pack(side=BOTTOM, fill=X)

# Creating Digits 
digit_frame = Frame(root,padx=10)
digit_frame.pack(side=RIGHT, anchor=NE, padx=5)





def digitButton(val, i, j):
    db = Button(digit_frame, text=val, height=2, width=2,padx=5, pady=2, 
                font="licida 28 bold", relief=SUNKEN,)
    db.grid(row=i, column=j)
    db.bind("<Button-1>", click)

lst = [9,8,7,6,5,4,3,2,1,0,'e','.','+','-','*','/','=','C']

pi, pj, p = 1,1,1
for i in lst[:12]:
    digitButton(str(i),pi,pj)
    pj += 1
    if pj == 4:
        pi += 1
        pj = 1


# Operations
oprn_frame = Frame(root, bg="black")
oprn_frame.pack(side=LEFT, anchor=NW, pady = 10,padx=10)

pi, pj = 1,1

for i in lst[12:]:
    
    bo = Button(oprn_frame, height=2, width=2, text=str(i), bg="#383030", fg="white",
           font="lucida 20 bold")
    bo.grid(row=pi,column=pj)

    pj += 1
    if pj % 3 == 0:
        pi+=1
        pj=1
    bo.bind("<Button-1>", click)


root.mainloop()