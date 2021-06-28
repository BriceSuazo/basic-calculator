import tkinter as tk
from tkinter import Tk, Button, Frame, TOP, PhotoImage

answer = 0
window = tk.Tk()
window.wm_title("Basic Calculator | Brice Suazo")
window.resizable(0, 0)
window.configure(bg='#1A1A1A')

icon = PhotoImage(file = 'calculator-icon.png')
window.iconphoto(False, icon)


#==============================================

def clearEntry():
    mainEntry.delete(0, 'end')
    mainEntry.insert(0, "0")

def clear():
    secondaryEntry.delete(0, 'end')
    mainEntry.delete(0, 'end')
    mainEntry.insert(0, "0")

def deleteNum():
    mainEntry.delete(mainEntry.index("end") - 1)

    if mainEntry.get() == "":
        mainEntry.insert(0, "0")


def entryPlus():
    initialMainEntry = float(mainEntry.get())
    currentMainEntry = float(0)

    if secondaryEntry.get() == "":
        secondaryEntry.insert(0, str(initialMainEntry) + " + ")
    else:
        initialMainEntry = float(mainEntry.get())
        currentMainEntry = float(str(secondaryEntry.get()[:-3]))
        secondaryEntry.delete(0, 'end')
        secondaryEntry.insert(0, str(currentMainEntry + initialMainEntry) + " + ")
        
    mainEntry.delete(0, 'end')
    mainEntry.insert(0, "0")


def entryMinus():
    initialMainEntry = float(mainEntry.get())
    currentMainEntry = float(0)

    if secondaryEntry.get() == "":
        secondaryEntry.insert(0, str(initialMainEntry) + " - ")
    else:
        initialMainEntry = float(mainEntry.get())
        currentMainEntry = float(str(secondaryEntry.get()[:-3]))
        secondaryEntry.delete(0, 'end')
        secondaryEntry.insert(0, str(currentMainEntry - initialMainEntry) + " - ")
        
    mainEntry.delete(0, 'end')
    mainEntry.insert(0, "0")


def entryMultiply():
    initialMainEntry = float(mainEntry.get())
    currentMainEntry = float(0)

    if secondaryEntry.get() == "":
        secondaryEntry.insert(0, str(initialMainEntry) + " * ")
    else:
        initialMainEntry = float(mainEntry.get())
        currentMainEntry = float(str(secondaryEntry.get()[:-3]))
        secondaryEntry.delete(0, 'end')
        secondaryEntry.insert(0, str(currentMainEntry * initialMainEntry) + " * ")
        
    mainEntry.delete(0, 'end')
    mainEntry.insert(0, "0")


def entryDivision():
    initialMainEntry = float(mainEntry.get())
    currentMainEntry = float(0)

    if secondaryEntry.get() == "":
        secondaryEntry.insert(0, str(initialMainEntry) + " / ")
    else:
        initialMainEntry = float(mainEntry.get())
        currentMainEntry = float(str(secondaryEntry.get()[:-3]))
        secondaryEntry.delete(0, 'end')
        try:
            answer = currentMainEntry / initialMainEntry
        except ZeroDivisionError:
            answer = float(0)
        secondaryEntry.insert(0, str(answer) + " / ")
        
    mainEntry.delete(0, 'end')
    mainEntry.insert(0, "0")



expression = ""

def btnClick(item):
    
    if (item == "+") or (item == "-") or (item == "*") or (item == "/") or (item == "="):
        if item == "+":
            entryPlus()
        elif item == "-":
            entryMinus()
        elif item == "*":
            entryMultiply()
        elif item == "/":
            entryDivision()
        elif item == "=":
            if secondaryEntry.get() == "":
                secondaryEntry.insert(0, str(mainEntry.get()) + " = ")
                mainEntry.delete(0, 'end')
            elif secondaryEntry.get()[-2] == "=":
                secondaryEntry.delete(0, 'end')
                if mainEntry.get() == "":
                    secondaryEntry.insert(0, "0 = ")
                else:
                    secondaryEntry.delete(0, 'end')
                    secondaryEntry.insert(0, str(mainEntry.get()) + " = ")

                mainEntry.delete(0, 'end')
            else:
                if secondaryEntry.get()[-2] == "+":
                    entryPlus()
                elif secondaryEntry.get()[-2] == "-":
                    entryMinus()
                elif secondaryEntry.get()[-2] == "*":
                    entryMultiply()
                elif secondaryEntry.get()[-2] == "/":
                    entryDivision()
    else:
        if mainEntry.get() == "0":
            mainEntry.delete(0, 1)


        global expression
        expression = str(item)
        mainEntry.insert("end", expression)


def onlyCharacter(char):
    acceptedChars = "+-*/"
    if any(not char.isdigit() for char in acceptedChars):
        return True
    else:
        return False


validation = window.register(onlyCharacter)


#==============================================


inputFrame= Frame(window, height=50, bd=0, bg="#1A1A1A") 
inputFrame.pack(side=TOP)

btnFrame = Frame(window, bg="#1A1A1A")
btnFrame.pack()


#==============================================


mainEntry = tk.Entry(inputFrame, font=("Arial", 38), validate ="key", validatecommand =(validation, '% P'), fg="white", bg="#1A1A1A", bd = 0, width=13, justify="right")
mainEntry.insert(0, "0")
mainEntry.grid(row=1, column=0, columnspan = 4)
# mainEntry.focus()

secondaryEntry = tk.Entry(inputFrame, font=("Arial", 14), fg="white", bg="#1A1A1A", bd = 0, width=32, justify="right")
secondaryEntry.grid(row=0, column=0, columnspan = 4)


#==============================================


btnWidth1 = 12
btnWidth2 = btnWidth1 + 13
btnWidth3 = btnWidth2 + 13
btnHeight = 5

btnClear = tk.Button(btnFrame, text="C", fg="white", bg="#292929", bd = 0, width = btnWidth2, height = btnHeight, command=clear).grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
btnDelete = tk.Button(btnFrame, text="DELETE", fg="white", bg="#292929", bd = 0, width = btnWidth2, height = btnHeight, command=deleteNum).grid(row = 0, column = 2, columnspan = 2, padx = 1, pady = 1)
btnClearEntry = tk.Button(btnFrame, text="CE", fg="white", bg="#292929", bd = 0, width = btnWidth3, height = btnHeight, command=clearEntry).grid(row = 1, column = 0, columnspan = 3, padx = 1, pady = 1)

btn7 = tk.Button(btnFrame, text="7", fg="white", bg="#050505", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("7")).grid(row = 2, column = 0, padx = 1, pady = 1)
btn8 = tk.Button(btnFrame, text="8", fg="white", bg="#050505", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("8")).grid(row = 2, column = 1, padx = 1, pady = 1)
btn9 = tk.Button(btnFrame, text="9", fg="white", bg="#050505", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("9")).grid(row = 2, column = 2, padx = 1, pady = 1)
btn4 = tk.Button(btnFrame, text="4", fg="white", bg="#050505", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("4")).grid(row = 3, column = 0, padx = 1, pady = 1)
btn5 = tk.Button(btnFrame, text="5", fg="white", bg="#050505", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("5")).grid(row = 3, column = 1, padx = 1, pady = 1)
btn6 = tk.Button(btnFrame, text="6", fg="white", bg="#050505", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("6")).grid(row = 3, column = 2, padx = 1, pady = 1)
btn1 = tk.Button(btnFrame, text="1", fg="white", bg="#050505", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("1")).grid(row = 4, column = 0, padx = 1, pady = 1)
btn2 = tk.Button(btnFrame, text="2", fg="white", bg="#050505", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("2")).grid(row = 4, column = 1, padx = 1, pady = 1)
btn3 = tk.Button(btnFrame, text="3", fg="white", bg="#050505", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("3")).grid(row = 4, column = 2, padx = 1, pady = 1)
btn0 = tk.Button(btnFrame, text="0", fg="white", bg="#050505", bd = 0, width = btnWidth2, height = btnHeight, command=lambda: btnClick("0")).grid(row = 5, column = 0, columnspan = 2, padx = 1, pady = 1)
btnPoint = tk.Button(btnFrame, text=".", fg="white", bg="#050505", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick(".")).grid(row = 5, column = 2, padx = 1, pady = 1)

btnDivision = tk.Button(btnFrame, text="/", fg="white", bg="#292929", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("/")).grid(row = 1, column = 3, padx = 1, pady = 1)
btnMultiply = tk.Button(btnFrame, text="*", fg="white", bg="#292929", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("*")).grid(row = 2, column = 3, padx = 1, pady = 1)
btnMinus = tk.Button(btnFrame, text="-", fg="white", bg="#292929", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("-")).grid(row = 3, column = 3, padx = 1, pady = 1)
btnPlus = tk.Button(btnFrame, text="+", fg="white", bg="#292929", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("+")).grid(row = 4, column = 3, padx = 1, pady = 1)

btnEquals = tk.Button(btnFrame, text="=", fg="white", bg="#292929", bd = 0, width = btnWidth1, height = btnHeight, command=lambda: btnClick("=")).grid(row = 5, column = 3, padx = 1, pady = 1)


#==============================================

window.mainloop()