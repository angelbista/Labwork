from tkinter import*

def btnclick(numbers):   #define the button(btn)click function
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():   # define the clear function
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():     #define the Equal to function
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operators=""

cal = Tk()
cal.title("Calculator")       # name the app, i choose a "Calculator" because it's random
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal,font=('bold',30), textvariable=text_Input, bd=20, insertwidth=4,
                   bg="white", justify='right').grid(columnspan=4) 

btnclear=Button(cal,padx=16,pady=16,bd=8, fg="white",font=('arial',15,'bold'),
            text="C",bg="black",command=btnClearDisplay).grid(row=1,column="3")

btn7=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="9",bg="powder blue",command=lambda:btnclick(7)).grid(row=1,column="2")

btn8=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="8", bg="powder blue",command=lambda:btnclick(8)).grid(row=1,column="1")

btn9=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="7", bg="powder blue",command=lambda:btnclick(9)).grid(row=1,column="0")

Division=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="/",bg="powder blue",command=lambda:btnclick("/")).grid(row=2,column="3")

btn6=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="6",bg="powder blue",command=lambda:btnclick(6)).grid(row=2,column="0")

btn5=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="5",bg="powder blue",command=lambda:btnclick(5)).grid(row=2,column="1")

btn4=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="4",bg="powder blue",command=lambda:btnclick(4)).grid(row=2,column="2")

subtraction=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="-",bg="powder blue",command=lambda:btnclick("-")).grid(row=3,column="3")

btn3=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="3",bg="powder blue",command=lambda:btnclick(3)).grid(row=3,column="0")

btn2=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="2",bg="powder blue",command=lambda:btnclick(2)).grid(row=3,column="1")

btn1=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="1",bg="powder blue",command=lambda:btnclick(1)).grid(row=3,column="2")


Btn0=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="0",bg="powder blue",command=lambda:btnclick(0)).grid(row=5,column="0")

Dot=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 10,'bold'),
            text=".",bg="powder blue",command=lambda:btnclick(".")).grid(row=5,column="1")

Equal=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 15,'bold'),
            text="=",bg="powder blue",command=btnEqualsInput).grid(row=5,column="2")

Addition=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('bold', 30,'bold'),
            text="+",bg="powder blue",command=lambda:btnclick("+")).grid(row=5,column="3")



cal.mainloop()
