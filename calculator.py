from tkinter import *
window = Tk()
window.title("Basic Calculator v0.1")
window.geometry("217x280")

# CALCULATOR LABEL

yazi = Label(text="Magnificent Calculator", bg="skyblue", width=30)
yazi.grid(padx=0, pady=0)

# ENTRY SPACE
entery = Entry(window, font="Verdana 14 bold", width=10, justify="right")
entery.insert(0, "")
entery.grid(padx=0, pady=1)


def process(number):
    s = len(entery.get())
    entery.insert(s, str(number))


# STORING FIRST NUMBER AND OPERATOR
s1 = 0
o = ""


def si(operator):
    global s1
    global o
    o = str(operator)
    s1 = float(entery.get())
    entery.delete(0, "end")


# GETTING SECOND NUMBER AND CALCULATING RESULT
s2 = 0


def calculate():
    global s2
    s2 = float(entery.get())
    result = float(eval("{}{}{}".format(s1, o, s2)))
    entery.delete(0, "end")
    entery.insert(0, str(result))


# NUMBERS


b1 = Button(text="1", fg="black", bg="gray", height=2, width=4,
            command=lambda: process(1), font="Verdana 10 bold").place(x=30, y=55)
b2 = Button(text="2", fg="black", bg="gray", height=2, width=4,
            command=lambda: process(2), font="Verdana 10 bold").place(x=70, y=55)
b3 = Button(text="3", fg="black", bg="gray", height=2, width=4,
            command=lambda: process(3), font="Verdana 10 bold").place(x=110, y=55)
b4 = Button(text="4", fg="black", bg="gray", height=2, width=4,
            command=lambda: process(4), font="Verdana 10 bold").place(x=30, y=100)
b5 = Button(text="5", fg="black", bg="gray", height=2, width=4,
            command=lambda: process(5), font="Verdana 10 bold").place(x=70, y=100)
b6 = Button(text="6", fg="black", bg="gray", height=2, width=4,
            command=lambda: process(6), font="Verdana 10 bold").place(x=110, y=100)
b7 = Button(text="7", fg="black", bg="gray", height=2, width=4,
            command=lambda: process(7), font="Verdana 10 bold").place(x=30, y=145)
b8 = Button(text="8", fg="black", bg="gray", height=2, width=4,
            command=lambda: process(8), font="Verdana 10 bold").place(x=70, y=145)
b9 = Button(text="9", fg="black", bg="gray", height=2, width=4,
            command=lambda: process(9), font="Verdana 10 bold").place(x=110, y=145)
bs = Button(text="0", fg="black", bg="gray", height=2, width=4,
            command=lambda: process(0), font="Verdana 10 bold").place(x=30, y=190)
# OPERATORS AND POINT
ba = Button(text="+", fg="black", bg="orange", height=2, width=4,
            command=lambda a="+": si("+"), font="Verdana 10 bold").place(x=150, y=145)
be = Button(text="-", fg="black", bg="orange", height=2, width=4,
            command=lambda e="-": si(e), font="Verdana 10 bold").place(x=70, y=190)
bn = Button(text=".", fg="black", bg="orange", height=2, width=4,
            command=lambda x=".": process(x), font="Verdana 10 bold").place(x=110, y=190)
eb = Button(text="=", fg="black", bg="orange", height=2, width=4,
            command=lambda: calculate(), font="Verdana 10 bold").place(x=150, y=190)
bb = Button(text="/", fg="black", bg="orange", height=2, width=4,
            command=lambda b="/": si(b), font="Verdana 10 bold").place(x=150, y=55)
bc = Button(text="x", fg="black", bg="orange", height=2, width=4,
            command=lambda c="*": si(c), font="Verdana 10 bold").place(x=150, y=100)
# RESET BUTTON
bd = Button(text="AC", fg="black", bg="orange", height=2, width=17,
            command=lambda: entery.delete(0, "end"), font="Verdana 10 bold").place(x=32, y=235)

window.mainloop()
