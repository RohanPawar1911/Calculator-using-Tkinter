import tkinter
from tkinter.font import BOLD

def btnclick(numbers):
    global operators
    operators=operators+str(numbers)
    text_input.set(operators)

def btncleardisplay():
    global operators
    operators=""
    text_input.set("")

def btnequalinput():
    global operators
    sumup=str(eval(operators))
    text_input.set(sumup)
    operators=sumup

window=tkinter.Tk()
window.title("CALCULATOR")

operators=""
text_input=tkinter.StringVar()

txtdisplay=tkinter.Entry(window,font=("arial",20,BOLD),textvariable=text_input,border=30,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)

btn7=tkinter.Button(window,padx=16,bd=8,fg="black",font=("arial",20,BOLD),
        text="7",bg="powder blue",command=lambda:btnclick(7)).grid(row=1,column=0)

btn8=tkinter.Button(window,padx=16,bd=8,fg="black",font=("arial",20,BOLD),
        text="8",bg="powder blue",command=lambda:btnclick(8)).grid(row=1,column=1)

btn9=tkinter.Button(window,padx=16,bd=8,fg="black",font=("arial",20,BOLD),
        text="9",bg="powder blue",command=lambda:btnclick(9)).grid(row=1,column=2)

addition=tkinter.Button(window,padx=16,bd=8,fg="black",font=("arial",20,BOLD),text="+",bg="powder blue",command=lambda:btnclick("+")).grid(row=1,column=3)
#**********************************************************************************
btn4=tkinter.Button(window,padx=16,bd=8,fg="black",font=("arial",20,BOLD),
        text="4",bg="powder blue",command=lambda:btnclick(4)).grid(row=2,column=0)

btn5=tkinter.Button(window,padx=16,bd=8,fg="black",font=("arial",20,BOLD),
        text="5",bg="powder blue",command=lambda:btnclick(5)).grid(row=2,column=1)

btn6=tkinter.Button(window,padx=16,bd=8,fg="black",font=("arial",20,BOLD),
        text="6",bg="powder blue",command=lambda:btnclick(6)).grid(row=2,column=2)

subtraction=tkinter.Button(window,padx=16,bd=8,fg="black",font=("arial",20,BOLD),text="-",bg="powder blue",command=lambda:btnclick("-")).grid(row=2,column=3)

#************************************************************************************
btn1=tkinter.Button(window,padx=16,bd=8,fg="black",font=("arial",20,BOLD),
        text="1",bg="powder blue",command=lambda:btnclick(1)).grid(row=3,column=0)

btn2=tkinter.Button(window,padx=16,bd=8,fg="black",font=("arial",20,BOLD),
        text="2",bg="powder blue",command=lambda:btnclick(2)).grid(row=3,column=1)

btn3=tkinter.Button(window,padx=16,bd=8,fg="black",font=("arial",20,BOLD),
        text="3",bg="powder blue",command=lambda:btnclick(3)).grid(row=3,column=2)


multiplication=tkinter.Button(window,padx=16,bd=8,fg="black",font=("arial",20,BOLD),text="*",bg="powder blue",command=lambda:btnclick("*")).grid(row=3,column=3)

#****************************************************************************************
btn0=tkinter.Button(window,padx=16,pady=16,bd=8,fg="black",font=("arial",20,BOLD),
        text="0",bg="powder blue",command=lambda:btnclick(0)).grid(row=4,column=0)

btnclear=tkinter.Button(window,padx=16,pady=16,bd=8,fg="black",font=("arial",20,BOLD),
        text="x",bg="powder blue",command=btncleardisplay).grid(row=4,column=1)

btnequal=tkinter.Button(window,padx=16,pady=16,bd=8,fg="black",font=("arial",20,BOLD),
        text="=",bg="powder blue",command=btnequalinput).grid(row=4,column=2)


division=tkinter.Button(window,padx=16,pady=16,bd=8,fg="black",font=("arial",20,BOLD),text="/",command=lambda:btnclick("/"),bg="powder blue").grid(row=4,column=3)

#************************************************************************************






















window.mainloop()