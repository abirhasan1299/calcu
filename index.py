from tkinter import *
root = Tk()
root.title("Simple Calculator(Abir)")

entry = Entry(root, width=40,borderwidth=5, bg="yellow", fg="black")
entry.grid(row=0, column=0, columnspan=3, padx=10, pady= 10)

def button_click(number):
    present = entry.get()
    entry.delete(0, END)
    entry.insert(0,str(present) + str(number))
def button_clr():
    entry.delete(0, END)
def button_pls():
    first_number = entry.get()
    global math
    global f_num
    math = "addition"
    f_num = int(first_number)
    entry.delete(0,END)
def button_eql():
    second_number=entry.get()
    entry.delete(0,END)
    if math == "addition" :
        entry.insert(0,f_num + int(second_number))
    if math == "subtraction" :
        entry.insert(0,f_num - int(second_number))
    if math == "multiplication" :
        entry.insert(0,f_num * int(second_number))
    if math == "division":
        entry.insert(0,f_num / int(second_number))
def button_sub():
    first_number = entry.get()
    global math
    global f_num
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)
def button_multi():
    first_number = entry.get()
    global math
    global f_num
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)
def button_div():
    first_number = entry.get()
    global math
    global f_num
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)

button_1 = Button(root, text="1", padx=40, pady=20,bg="#fcb603",fg="white", command= lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20,bg="#fcb603",fg="white", command= lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="#fcb603",fg="white",command= lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="#fcb603",fg="white",command= lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="#fcb603",fg="white",command= lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="#fcb603",fg="white",command= lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="#fcb603",fg="white",command= lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20,bg="#fcb603",fg="white", command= lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20,bg="#fcb603",fg="white", command= lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20,bg="#fcb603",fg="white", command= lambda: button_click(0))
button_plus = Button(root,text="+",padx=39,pady=20,bg="#fc0377",command= button_pls)
button_clear = Button(root,text="Clear",padx=79,pady=20,bg="red",fg="#03dffc",command=button_clr)
button_equal = Button(root,text="=",padx=91,pady=20,bg="#fc0377",command=button_eql)
button_substrac = Button(root,text="-",padx=41,pady=20,bg="#fc0377",command=button_sub)
button_multiply = Button(root,text="x",padx=41,pady=20,bg="#fc0377",command=button_multi)
button_divide = Button(root,text="/",padx=42,pady=20,bg="#fc0377",command=button_div)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_plus.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1,columnspan=2)
button_substrac.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

root.mainloop()