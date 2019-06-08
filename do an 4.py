from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
    
cal = Tk()
cal.title("may tinh nvn")
operator = ""
text_Input = StringVar()
txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="blue", justify='right').grid(columnspan=4)


btn7 = Button(cal, padx=16, pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="7", bg="Orange", command=lambda: btnClick(7)).grid(row=1, column=0)

btn8 = Button(cal, padx=16, pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="8", bg="Orange", command=lambda: btnClick(8)).grid(row=1, column=1)

btn9 = Button(cal, padx=16, pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="9", bg="Orange", command=lambda: btnClick(9)).grid(row=1, column=2)

Addition = Button(cal, padx=16, pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="+", bg="Red", command=lambda: btnClick("+")).grid(row=1, column=3)
# ========================================================================================
btn4 = Button(cal, padx=16, pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="4", bg="Orange", command=lambda: btnClick(4)).grid(row=2, column=0)

btn5 = Button(cal, padx=16, pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="5", bg="Orange", command=lambda: btnClick(5)).grid(row=2, column=1)

btn6 = Button(cal, padx=16, pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="6", bg="Orange", command=lambda: btnClick(6)).grid(row=2, column=2)

Subtracition = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="-", bg="Red", command=lambda: btnClick("-")).grid(row=2, column=3)
# =========================================================================================
btn1 = Button(cal, padx=16,pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1", bg="Orange", command=lambda: btnClick(1)).grid(row=3, column=0)

btn2 = Button(cal, padx=16,pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="2", bg="Orange", command=lambda: btnClick(2)).grid(row=3, column=1)

btn3 = Button(cal, padx=16,pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="3", bg="Orange", command=lambda: btnClick(3)).grid(row=3, column=2)

Multiply = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="*", bg="Red", command=lambda: btnClick("*")).grid(row=3, column=3)
#=========================================================================================
btn10 = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="e", bg="teal", command=lambda: btnClick(2.71)).grid(row=5, column=0)

btn11 = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="Pi", bg="teal", command=lambda: btnClick(3.14)).grid(row=5, column=1)

btnClear = Button(cal, padx=16, pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="C", bg="Green", command=btnClearDisplay).grid(row=5, column=2)

btnEquals = Button(cal, padx=16, pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
                   text="=", bg="Green", command=btnEqualsInput).grid(row=5, column=3)
# =======================================================================================
btn13 = Button(cal, padx=16, pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="0", bg="Orange", command=lambda: btnClick(0)).grid(row=4, column=0)
btn14 = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
              text=".", bg="teal", command=lambda: btnClick(".")).grid(row=4, column=1)

btn15 = Button(cal, padx=16,pady=12, bd=6, fg="black", font=('arial', 20, 'bold'),
              text="x2", bg="teal", command=lambda: btnClick("*2")).grid(row=4, column=2)

Division = Button(cal, padx=16, pady=12, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="/", bg="Red", command=lambda: btnClick("/")).grid(row=4, column=3)
cal.mainloop()
