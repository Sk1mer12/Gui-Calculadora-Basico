from tkinter import *

root = Tk()
root.title("Simple calculator")
root.iconbitmap('C:/Users/simao/OneDrive/Ambiente de Trabalho/Projects/Python/dinal_deal.ico')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def gui_clear():
    e.delete(0, END)

def function_add():
    global op
    op = "add"
    x=e.get()
    global f_x
    f_x=0
    f_x = int(x)
    e.delete(0, END)

def function_multi():
    global op
    op = "multi"
    x=e.get()
    global f_x
    f_x=0
    f_x = int(x)
    e.delete(0, END)

def function_div():
    global op
    op = "div"
    x=e.get()
    global f_x
    f_x=0
    f_x = int(x)
    e.delete(0, END)

def function_sub():
    global op
    op = "sub"
    x=e.get()
    global f_x
    f_x=0
    f_x = int(x)
    e.delete(0, END)

def final_result():
    if op=="add":
        y=e.get()
        e.delete(0, END)
        z=int(y)+f_x
        e.insert(0, z)
    if op=="sub":
        y=e.get()
        e.delete(0, END)
        z=f_x-int(y)
        e.insert(0, z)
    if op=="multi":
        y=e.get()
        e.delete(0, END)
        z=f_x*int(y)
        e.insert(0, z)
    if op=="div":
        y=e.get()
        e.delete(0, END)
        z=f_x/int(y)
        e.insert(0, z)


button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_clear = Button(root, text="Clear", padx=79, pady=20, command=gui_clear)
button_plus = Button(root, text="+", padx=39, pady=20, command=function_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=final_result)

button_multiplication = Button(root, text="x", padx=40, pady=20, command=function_multi)
button_division = Button(root, text="/", padx=40, pady=20, command=function_div)
button_subtraction = Button(root, text="-", padx=40, pady=20, command=function_sub)

button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_clear.grid(row=5, column=1, columnspan=2)
button_plus.grid(row=5, column=0)
button_equal.grid(row=6, column=1, columnspan=2)

button_multiplication.grid(row=4, column=2)
button_division.grid(row=4, column=1)
button_subtraction.grid(row=6, column=0)

root.mainloop()