                 #import module
import tkinter as tk
from tkinter import *
import customtkinter as ctk   
expr=""                 #create global expression
root = ctk.CTk()            #create main window
root.title("calculator")
root.geometry("620x900")
root.configure(fg_color="#D4A7DA")

def press(key):          #called when a number or operator button is clicked
    global expr
    expr=expr+str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result=str(eval(expr))
        display.set(result)
        expr=""
    except:
        display.set("error")
        expr=""
def clear():
    global expr
    expr = ""
    display.set("")
display=StringVar()               #stores text in entry widget
entry=Entry(root,textvariable=display,font=("Poppins", 28),bd=0,justify='right')   #create input box
entry.grid(row=0,
    column=0,
    columnspan=4,
    ipadx=80,
    ipady=25,
    pady=20)      

#number buttons 
btn1=ctk.CTkButton(root,text='1',text_color='black',fg_color="#A06BB5",command=lambda:press(1),font=("Poppins", 18),
height=30,width=60)
btn1.grid(row=2, column=0,padx=15,
    pady=15)
btn2=ctk.CTkButton(root,text='2',text_color='black',fg_color="#A06BB5",command=lambda:press(2),font=("Poppins", 18),
height=30,width=60)
btn2.grid(row=2, column=1,padx=15,
    pady=15)
btn3=ctk.CTkButton(root,text='3',text_color='black',fg_color="#A06BB5",command=lambda:press(3),font=("Poppins", 18),
height=30,width=60)
btn3.grid(row=2, column=2,padx=15,
    pady=15)
btn4=ctk.CTkButton(root,text='4',text_color='black',fg_color="#A06BB5",command=lambda:press(4),font=("Poppins", 18),
height=30,width=60)
btn4.grid(row=3, column=0,padx=15,
    pady=15)
btn5=ctk.CTkButton(root,text='5',text_color='black',fg_color="#A06BB5",command=lambda:press(5),font=("Poppins", 18),
height=30,width=60)
btn5.grid(row=3, column=1,padx=15,
    pady=15)
btn6=ctk.CTkButton(root,text='6',text_color='black',fg_color="#A06BB5",command=lambda:press(6),font=("Poppins", 18),
height=30,width=60)
btn6.grid(row=3, column=2,padx=15,
    pady=15)
btn7=ctk.CTkButton(root,text='7',text_color='black',fg_color="#A06BB5",command=lambda:press(7),font=("Poppins", 18),
height=30,width=60)
btn7.grid(row=4, column=0,padx=15,
    pady=15)
btn8=ctk.CTkButton(root,text='8',text_color='black',fg_color="#A06BB5",command=lambda:press(8),font=("Poppins", 18),
height=30,width=60)
btn8.grid(row=4, column=1,padx=15,
    pady=15)
btn9=ctk.CTkButton(root,text='9',text_color='black',fg_color="#A06BB5",command=lambda:press(9),font=("Poppins", 18),
height=30,width=60)
btn9.grid(row=4, column=2,padx=15,
    pady=15)
btn0 = ctk.CTkButton(root, text='0', text_color='black', fg_color="#A06BB5", command=lambda: press(0), font=("Poppins", 18),
height=30, width=60)
btn0.grid(row=5, column=1,padx=15,
    pady=15)

#operator buttons
plus=ctk.CTkButton(root,text='+',text_color='black',fg_color="#A06BB5",command=lambda:press('+'),font=("Poppins", 18),
height=30,width=60)
plus.grid(row=2,column=3,padx=15,
    pady=15)
minus = ctk.CTkButton(root, text='-', text_color='black', fg_color="#A06BB5", command=lambda: press('-'),font=("Poppins", 18),
 height=30, width=60)
minus.grid(row=3, column=3,padx=15,
    pady=15)
mult = ctk.CTkButton(root, text='*',text_color='black', fg_color="#A06BB5", command=lambda: press('*'),font=("Poppins", 18),
height=30, width=60)
mult.grid(row=4, column=3,padx=15,
    pady=15)
div = ctk.CTkButton(root, text='/', text_color='black', fg_color="#A06BB5", command=lambda: press('/'), font=("Poppins", 18),
height=30, width=60)
div.grid(row=5, column=3,padx=15,
    pady=15)
eq = ctk.CTkButton(root, text='=', text_color='black', fg_color="#A06BB5", command=equal,font=("Poppins", 18),
 height=30, width=60)
eq.grid(row=6, column=2,padx=15,
    pady=15)
clr = ctk.CTkButton(root, text='Clear', text_color='black', fg_color="#A06BB5", command=clear,font=("Poppins", 18),
 height=30, width=60)
clr.grid(row=6, column=1,padx=15,
    pady=15)
dot = ctk.CTkButton(root, text='.', text_color='black', fg_color="#A06BB5", command=lambda: press('.'),font=("Poppins", 18),
 height=30, width=60)
dot.grid(row=6, column=0,padx=15,
    pady=15)
#start event loop
root.mainloop()

