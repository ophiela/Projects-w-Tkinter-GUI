from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import math
import random

#the set up

root = Tk()
root.config(background = 'white')
root.option_add('tearOff', False)
top = Frame(root)
top.grid(sticky = N, column = 2)
style = ttk.Style(root)
style.configure('xpnative')
screen = Canvas(root, height = 100, width = 200)
screen.grid(row = 0,column = 1, sticky = N, columnspan = 3)
screen.config(background = 'white', borderwidth = 30)
number = Entry(root)
numbers = ['0','1', '2', '3', '4','5','6','7','8','9']
value = 'n'

#commands

def help_fun():
    messagebox.showinfo('Help', 'Help message')

def zero():
    global value
    if value == 'n':
        value = numbers[0]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[0]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def one():
    global value
    if value == 'n':
        value = numbers[1]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[1]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def two():
    global value
    if value == 'n':
        value = numbers[2]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[2]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def three():
    global value
    if value == 'n':
        value = numbers[3]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[3]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def four():
    global value
    if value == 'n':
        value = numbers[4]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[4]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def five():
    global value
    if value == 'n':
        value = numbers[5]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[5]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def six():
    global value
    if value == 'n':
        value = numbers[6]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[6]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def seven():
    global value
    if value == 'n':
        value = numbers[7]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[7]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def eight():
    global value
    if value == 'n':
        value = numbers[8]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[8]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def nine():
    global value
    if value == 'n':
        value = numbers[9]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[9]
        number.insert(INSERT, value)
        number.place(anchor = NW)

#Buttons
    
add = ttk.Button(root, text = '+',
                 command = help_fun).grid(row = 11, column = 3)
minus = ttk.Button(root, text = '-',
                   command = help_fun).grid(row = 12, column = 3)
multi = ttk.Button(root, text = 'x',
                   command = help_fun).grid(row = 13, column = 3)
minus = ttk.Button(root, text = '/',
                   command = help_fun).grid(row = 14, column = 3)
clear = ttk.Button(root,
                   text = 'Clear',
                   command = help_fun).grid(row = 16,column= 2,
                                            columnspan = 2, ipadx = 45)
one = ttk.Button(root, text = '1',
                 command = one).grid(row = 11, column = 1)
two = ttk.Button(root, text = '2',
                 command = two).grid(row = 11, column = 2)
three = ttk.Button(root, text = '3',
                   command = three).grid(row = 12, column = 1)
four = ttk.Button(root, text = '4',
                  command = four).grid(row = 12, column = 2)
five = ttk.Button(root, text = '5',
                  command = five).grid(row = 13, column = 1)
six = ttk.Button(root, text = '6',
                 command = six).grid(row = 13, column = 2)
seven = ttk.Button(root, text = '7',
                   command = seven).grid(row = 14, column = 1)
eight = ttk.Button(root, text = '8',
                   command = eight).grid(row = 14, column = 2)
nine = ttk.Button(root, text = '9',
                  command = nine).grid(row = 15, column = 1)
zero = ttk.Button(root, text = '0',
                  command = zero).grid(row = 15, column = 2)
square = ttk.Button(root, text = 'Sqr',
                  command = nine).grid(row = 15, column = 3)
pwr = ttk.Button(root, text = 'PWR',
                  command = nine).grid(row = 16, column = 1)

#style.configure('TButton', foreground = 'red')
menu = Menu(root)
root.config(menu = menu)
menu.add_command(label = 'Quit', command = root.destroy)
menu.add_command(label = 'Help', command = help_fun)



#screen = Entry(top, textvariable= str )
#screen.focus_set()
#screen.grid(row = 0, column = 1)

mainloop()