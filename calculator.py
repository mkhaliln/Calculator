from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(0, 0)

fram = LabelFrame(root, padx=5, pady=5, bg="silver")
fram.pack()

e = Entry(fram, width=15, font=("Verdana", 20), justify=RIGHT, bg="#5d6d7e", fg="white", relief=FLAT, borderwidth=15)
e.grid(row=0, column=0, columnspan=3)

def clickbutton(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clearbutton():
    e.delete(0, END)

def addbutton():
    firstnumber = e.get()
    global fnum
    global math
    math = 'addition'
    fnum = int(firstnumber)
    e.delete(0, END)

def subbutton():
    firstnumber = e.get()
    global fnum
    global math
    math = 'subtraction'
    fnum = int(firstnumber)
    e.delete(0, END)

def mulbutton():
    firstnumber = e.get()
    global fnum
    global math
    math = 'multiplication'
    fnum = int(firstnumber)
    e.delete(0, END)

def divbutton():
    firstnumber = e.get()
    global fnum
    global math
    math = 'division'
    fnum = int(firstnumber)
    e.delete(0, END)

def equalbutton():
    secondnumber = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, fnum + int(secondnumber))
    if math == 'subtraction':
        e.insert(0, fnum - int(secondnumber))
    if math == 'multiplication':
        e.insert(0, fnum * int(secondnumber))
    if math == 'division':
        try:
            e.insert(0, fnum / int(secondnumber))
        except:
            e.insert(0, "Error")
# Button Defines
button1 = Button(fram, text="1", height=2, width=8, border=3, bg="#d6eaf8", command=lambda: clickbutton(1))
button2 = Button(fram, text="2", height=2, width=8, border=3, bg="#d6eaf8", command=lambda: clickbutton(2))
button3 = Button(fram, text="3", height=2, width=8, border=3, bg="#d6eaf8", command=lambda: clickbutton(3))
button4 = Button(fram, text="4", height=2, width=8, border=3, bg="#d6eaf8", command=lambda: clickbutton(4))
button5 = Button(fram, text="5", height=2, width=8, border=3, bg="#d6eaf8", command=lambda: clickbutton(5))
button6 = Button(fram, text="6", height=2, width=8, border=3, bg="#d6eaf8", command=lambda: clickbutton(6))
button7 = Button(fram, text="7", height=2, width=8, border=3, bg="#d6eaf8", command=lambda: clickbutton(7))
button8 = Button(fram, text="8", height=2, width=8, border=3, bg="#d6eaf8", command=lambda: clickbutton(8))
button9 = Button(fram, text="9", height=2, width=8, border=3, bg="#d6eaf8", command=lambda: clickbutton(9))
button0 = Button(fram, text="0", height=2, width=8, border=3, bg="#d6eaf8", command=lambda: clickbutton(0))
buttonadd = Button(fram, text="+", height=2, width=8, border=3, bg="#aed6f1", command=addbutton)
buttonsub = Button(fram, text="_", height=2, width=8, border=3, bg="#aed6f1", command=subbutton)
buttonmul = Button(fram, text="x", height=2, width=8, border=3, bg="#aed6f1", command=mulbutton)
buttondiv = Button(fram, text="/", height=2, width=8, border=3, bg="#aed6f1", command=divbutton)
buttonequal = Button(fram, text="=", height=2, width=19, border=3,bg="#5dade2", command=equalbutton)
buttonclear = Button(fram, text="Clear", height=2, width=19, border=3, bg="#fdfefe", command=clearbutton)

# Button Put on Screen

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonadd.grid(row=5, column=0)
buttonequal.grid(row=5, column=1, columnspan=2)
buttonclear.grid(row=4, column=1, columnspan=2)

buttonsub.grid(row=6, column=0)
buttonmul.grid(row=6, column=1)
buttondiv.grid(row=6, column=2)

root.mainloop()
