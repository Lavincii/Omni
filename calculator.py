from tkinter import *

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="black")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add("*Font", "arial 20 bold")
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Calculator")

        display = StringVar()
        # relief can be FLAT or RIDGE or RAISED or SUNKEN GROOVE
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg='darkgray').pack(
            side=TOP, expand=YES, fill=BOTH)

        for clearBut in (["CE"], ["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(""))
        for numBut in ("789/", "456*", "123-", "0.+"):
            functionNum = iCalc(self, TOP)
            for char in numBut:
                button(functionNum, LEFT, char,
                       lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))
        equalButton = iCalc(self, TOP)
        for iEqual in "=":
            if iEqual == "=":
                btniEqual = button(equalButton, LEFT, iEqual)
                btniEqual.bind("<ButtonRelease-1>", lambda e, s=self, storeObj=display: s.calc(storeObj),
                               '+')
            else:
                btniEqual = button(equalButton, LEFT, iEqual,
                                   lambda storeObj=display, s='%s' % iEqual: storeObj.set(
                                       storeObj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


app().mainloop()