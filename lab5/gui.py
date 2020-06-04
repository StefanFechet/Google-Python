def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('random')
install_and_import('tkinter')
install_and_import('sys')
install_and_import('time')

import random
import tkinter as tk
import sys
import time
from tkinter import *

global machine, human, button1, button2, button3, button4, button5, button6, button7, button8, button9, button, \
    initial, configuration, root, depth, next_step


def doJob1():
    root = Node("root", configuration, depth)
    root.createChildren()
    next_step = 0
    for child in root.children:
        if child.value == root.value:
            next_step = int(child.name)
    if next_step == 1:
        button1.configure(image=s2, state='disabled', cursor='X_cursor')
    if next_step == 2:
        button2.configure(image=s2, state='disabled', cursor='X_cursor')
    if next_step == 3:
        button3.configure(image=s2, state='disabled', cursor='X_cursor')
    if next_step == 4:
        button4.configure(image=s2, state='disabled', cursor='X_cursor')
    if next_step == 5:
        button5.configure(image=s2, state='disabled', cursor='X_cursor')
    if next_step == 6:
        button6.configure(image=s2, state='disabled', cursor='X_cursor')
    if next_step == 7:
        button7.configure(image=s2, state='disabled', cursor='X_cursor')
    if next_step == 8:
        button8.configure(image=s2, state='disabled', cursor='X_cursor')
    if next_step == 9:
        button9.configure(image=s2, state='disabled', cursor='X_cursor')
    configuration[next_step] = 'o'
    root = Node("root", configuration, depth)
    if root.finalState(configuration):
        button1.configure(state='disabled', cursor='X_cursor')
        button2.configure(state='disabled', cursor='X_cursor')
        button3.configure(state='disabled', cursor='X_cursor')
        button4.configure(state='disabled', cursor='X_cursor')
        button5.configure(state='disabled', cursor='X_cursor')
        button6.configure(state='disabled', cursor='X_cursor')
        button7.configure(state='disabled', cursor='X_cursor')
        button8.configure(state='disabled', cursor='X_cursor')
        button9.configure(state='disabled', cursor='X_cursor')
        if root.finalState(configuration):
            root.whoWin(configuration)
        rooter.quit()


def doJob2():
    root = Node("root", configuration, depth)
    if root.finalState(configuration):
        button1.configure(state='disabled', cursor='X_cursor')
        button2.configure(state='disabled', cursor='X_cursor')
        button3.configure(state='disabled', cursor='X_cursor')
        button4.configure(state='disabled', cursor='X_cursor')
        button5.configure(state='disabled', cursor='X_cursor')
        button6.configure(state='disabled', cursor='X_cursor')
        button7.configure(state='disabled', cursor='X_cursor')
        button8.configure(state='disabled', cursor='X_cursor')
        button9.configure(state='disabled', cursor='X_cursor')
        if root.finalState(configuration):
            root.whoWin(configuration)
        rooter.quit()

    root.createChildren()
    next_step = 0
    for child in root.children:
        if child.value == root.value:
            next_step = int(child.name)
    if next_step == 1:
        button1.configure(image=s1, state='disabled', cursor='X_cursor')
    if next_step == 2:
        button2.configure(image=s1, state='disabled', cursor='X_cursor')
    if next_step == 3:
        button3.configure(image=s1, state='disabled', cursor='X_cursor')
    if next_step == 4:
        button4.configure(image=s1, state='disabled', cursor='X_cursor')
    if next_step == 5:
        button5.configure(image=s1, state='disabled', cursor='X_cursor')
    if next_step == 6:
        button6.configure(image=s1, state='disabled', cursor='X_cursor')
    if next_step == 7:
        button7.configure(image=s1, state='disabled', cursor='X_cursor')
    if next_step == 8:
        button8.configure(image=s1, state='disabled', cursor='X_cursor')
    if next_step == 9:
        button9.configure(image=s1, state='disabled', cursor='X_cursor')
    configuration[next_step] = 'x'
    if root.finalState(configuration):
        button1.configure(state='disabled', cursor='X_cursor')
        button2.configure(state='disabled', cursor='X_cursor')
        button3.configure(state='disabled', cursor='X_cursor')
        button4.configure(state='disabled', cursor='X_cursor')
        button5.configure(state='disabled', cursor='X_cursor')
        button6.configure(state='disabled', cursor='X_cursor')
        button7.configure(state='disabled', cursor='X_cursor')
        button8.configure(state='disabled', cursor='X_cursor')
        button9.configure(state='disabled', cursor='X_cursor')
        if root.finalState(configuration):
            root.whoWin(configuration)
        rooter.quit()


def click1():
    if human == 'x':
        button1.configure(image=s1, state='disabled', cursor='X_cursor')
        configuration[1] = 'x'
        doJob1()
    else:
        button1.configure(image=s2, state='disabled', cursor='X_cursor')
        configuration[1] = 'o'
        doJob2()


def click2():
    if human == 'x':
        button2.configure(image=s1, state='disabled', cursor='X_cursor')
        configuration[2] = 'x'
        doJob1()
    else:
        button2.configure(image=s2, state='disabled', cursor='X_cursor')
        configuration[2] = 'o'
        doJob2()


def click3():
    if human == 'x':
        button3.configure(image=s1, state='disabled', cursor='X_cursor')
        configuration[3] = 'x'
        doJob1()
    else:
        button3.configure(image=s2, state='disabled', cursor='X_cursor')
        configuration[3] = 'o'
        doJob2()


def click4():
    if human == 'x':
        button4.configure(image=s1, state='disabled', cursor='X_cursor')
        configuration[4] = 'x'
        doJob1()
    else:
        button4.configure(image=s2, state='disabled', cursor='X_cursor')
        configuration[4] = 'o'
        doJob2()


def click5():
    if human == 'x':
        button5.configure(image=s1, state='disabled', cursor='X_cursor')
        configuration[5] = 'x'
        doJob1()
    else:
        button5.configure(image=s2, state='disabled', cursor='X_cursor')
        configuration[5] = 'o'
        doJob2()


def click6():
    if human == 'x':
        button6.configure(image=s1, state='disabled', cursor='X_cursor')
        configuration[6] = 'x'
        doJob1()
    else:
        button6.configure(image=s2, state='disabled', cursor='X_cursor')
        configuration[6] = 'o'
        doJob2()


def click7():
    if human == 'x':
        button7.configure(image=s1, state='disabled', cursor='X_cursor')
        configuration[7] = 'x'
        doJob1()
    else:
        button7.configure(image=s2, state='disabled', cursor='X_cursor')
        configuration[7] = 'o'
        doJob2()


def click8():
    if human == 'x':
        button8.configure(image=s1, state='disabled', cursor='X_cursor')
        configuration[8] = 'x'
        doJob1()
    else:
        button8.configure(image=s2, state='disabled', cursor='X_cursor')
        configuration[8] = 'o'
        doJob2()


def click9():
    if human == 'x':
        button9.configure(image=s1, state='disabled', cursor='X_cursor')
        configuration[9] = 'x'
        doJob1()
    else:
        button9.configure(image=s2, state='disabled', cursor='X_cursor')
        configuration[9] = 'o'
        doJob2()


class Node:
    def sameSign(self, configuration, i, j, k):
        if configuration[i] == 'x' and configuration[j] == 'x' and configuration[k] == 'x':
            return 'x'
        if configuration[i] == 'o' and configuration[j] == 'o' and configuration[k] == 'o':
            return 'o'
        return 'no'

    def finalState(self, configuration):
        flag = False
        l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for values in l:
            if self.sameSign(configuration, values[0], values[1], values[2]) != 'no':
                self.color = 'black'
                flag = True
                if self.sameSign(configuration, values[0], values[1], values[2]) == machine:
                    self.value = 1
                else:
                    self.value = 0 - self.depth - 1
                break
        else:
            for i in range(1, 10):
                if configuration[i] != 'x' and configuration[i] != 'o':
                    break
            else:
                self.color = 'black'
                self.value = 0
                flag = True
        return flag

    def whoWin(self, configuration):
        l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for values in l:
            if self.sameSign(configuration, values[0], values[1], values[2]) != 'no':
                if self.sameSign(configuration, values[0], values[1], values[2]) == machine:
                    if 1 in values:
                        button1['background'] = 'red'
                    if 2 in values:
                        button2['background'] = 'red'
                    if 3 in values:
                        button3['background'] = 'red'
                    if 4 in values:
                        button4['background'] = 'red'
                    if 5 in values:
                        button5['background'] = 'red'
                    if 6 in values:
                        button6['background'] = 'red'
                    if 7 in values:
                        button7['background'] = 'red'
                    if 8 in values:
                        button8['background'] = 'red'
                    if 9 in values:
                        button9['background'] = 'red'
                    return -1
                else:
                    if 1 in values:
                        button1['background'] = 'green'
                    if 2 in values:
                        button2['background'] = 'green'
                    if 3 in values:
                        button3['background'] = 'green'
                    if 4 in values:
                        button4['background'] = 'green'
                    if 5 in values:
                        button5['background'] = 'green'
                    if 6 in values:
                        button6['background'] = 'green'
                    if 7 in values:
                        button7['background'] = 'green'
                    if 8 in values:
                        button8['background'] = 'green'
                    if 9 in values:
                        button9['background'] = 'green'
                    return 1
        button1['background'] = 'yellow'
        button2['background'] = 'yellow'
        button3['background'] = 'yellow'
        button4['background'] = 'yellow'
        button5['background'] = 'yellow'
        button6['background'] = 'yellow'
        button7['background'] = 'yellow'
        button8['background'] = 'yellow'
        button9['background'] = 'yellow'
        return 0

    def findEmptyBoxes(self, configuration):
        positions = []
        for i in range(1, 10):
            if configuration[i] == '':
                positions.append(i)
        return positions

    def createChildren(self):
        if not self.finalState(self.configuration):
            positions = self.findEmptyBoxes(self.configuration)
            depth = self.depth
            cop = self.configuration
            for i in positions:
                con = self.configuration
                if self.depth % 2 == 1:
                    con[i] = 'o'
                else:
                    con[i] = 'x'
                node = Node(i, con, depth + 1)
                node.createChildren()
                self.children.append(node)
                for j in positions:
                    self.configuration[j] = ''
                node.color = 'black'
            values = []
            for child in self.children:
                values.append(child.value)
            if self.depth % 2 == 0 and machine == 'x':
                self.value = max(values)
            if self.depth % 2 == 1 and machine == 'x':
                self.value = min(values)
            if self.depth % 2 == 0 and machine == 'o':
                self.value = min(values)
            if self.depth % 2 == 1 and machine == 'o':
                self.value = max(values)

    def findNextStep(self):
        for child in self.children:
            if child.value == self.value:
                return int(child.value)

    def __init__(self, name, configuration, depth):
        self.name = name
        self.configuration = configuration
        self.depth = depth
        self.color = 'white'
        self.children = []
        self.value = 3


if random.randrange(0, 2) == 0:
    machine = 'x'
    human = 'o'
    depth = 0
else:
    machine = 'o'
    human = 'x'
    depth = 1

initial = ['' for i in range(10)]
configuration = ['' for i in range(10)]
root = Node("root", configuration, depth)


def close():
    sys.exit()


rooter = tk.Tk()
rooter.protocol('WM_DELETE_WINDOW', close)
rooter.winfo_toplevel().title("Tic Tac Toe")
rooter.geometry("620x620")
rooter.resizable(False, False)
frame1 = tk.Frame(rooter)
frame1.pack(side=tk.TOP, fill=tk.X)
s1 = tk.PhotoImage(file="x.png")
s2 = tk.PhotoImage(file="o.png")
back = tk.PhotoImage(file="back.png")


def on_enter1(e):
    if configuration[1] == '' and not root.finalState(configuration):
        if human == 'x':
            button1['image'] = s1
        else:
            button1['image'] = s2


def on_leave1(e):
    if configuration[1] == '' and not root.finalState(configuration):
        button1['image'] = back


def on_enter2(e):
    if configuration[2] == '' and not root.finalState(configuration):
        if human == 'x':
            button2['image'] = s1
        else:
            button2['image'] = s2


def on_leave2(e):
    if configuration[2] == '' and not root.finalState(configuration):
        button2['image'] = back


def on_enter3(e):
    if configuration[3] == '' and not root.finalState(configuration):
        if human == 'x':
            button3['image'] = s1
        else:
            button3['image'] = s2


def on_leave3(e):
    if configuration[3] == '' and not root.finalState(configuration):
        button3['image'] = back


def on_enter4(e):
    if configuration[4] == '' and not root.finalState(configuration):
        if human == 'x':
            button4['image'] = s1
        else:
            button4['image'] = s2


def on_leave4(e):
    if configuration[4] == '' and not root.finalState(configuration):
        button4['image'] = back


def on_enter5(e):
    if configuration[5] == '' and not root.finalState(configuration):
        if human == 'x':
            button5['image'] = s1
        else:
            button5['image'] = s2


def on_leave5(e):
    if configuration[5] == '' and not root.finalState(configuration):
        button5['image'] = back


def on_enter6(e):
    if configuration[6] == '' and not root.finalState(configuration):
        if human == 'x':
            button6['image'] = s1
        else:
            button6['image'] = s2


def on_leave6(e):
    if configuration[6] == '' and not root.finalState(configuration):
        button6['image'] = back


def on_enter7(e):
    if configuration[7] == '' and not root.finalState(configuration):
        if human == 'x':
            button7['image'] = s1
        else:
            button7['image'] = s2


def on_leave7(e):
    if configuration[7] == '' and not root.finalState(configuration):
        button7['image'] = back


def on_enter8(e):
    if configuration[8] == '' and not root.finalState(configuration):
        if human == 'x':
            button8['image'] = s1
        else:
            button8['image'] = s2


def on_leave8(e):
    if configuration[8] == '' and not root.finalState(configuration):
        button8['image'] = back


def on_enter9(e):
    if configuration[9] == '' and not root.finalState(configuration):
        if human == 'x':
            button9['image'] = s1
        else:
            button9['image'] = s2


def on_leave9(e):
    if configuration[9] == '' and not root.finalState(configuration):
        button9['image'] = back


button1 = tk.Button(frame1, height=200, width=200, image=back, command=click1, cursor="hand2")
button1.grid(row=0, column=0)
button1.bind("<Enter>", on_enter1)
button1.bind("<Leave>", on_leave1)

button2 = tk.Button(frame1, height=200, width=200, image=back, command=click2, cursor="hand2")
button2.grid(row=0, column=1)
button2.bind("<Enter>", on_enter2)
button2.bind("<Leave>", on_leave2)

button3 = tk.Button(frame1, height=200, width=200, image=back, command=click3, cursor="hand2")
button3.grid(row=0, column=2)
button3.bind("<Enter>", on_enter3)
button3.bind("<Leave>", on_leave3)

button4 = tk.Button(frame1, height=200, width=200, image=back, command=click4, cursor="hand2")
button4.grid(row=1, column=0)
button4.bind("<Enter>", on_enter4)
button4.bind("<Leave>", on_leave4)

button5 = tk.Button(frame1, height=200, width=200, image=back, command=click5, cursor="hand2")
button5.grid(row=1, column=1)
button5.bind("<Enter>", on_enter5)
button5.bind("<Leave>", on_leave5)

button6 = tk.Button(frame1, height=200, width=200, image=back, command=click6, cursor="hand2")
button6.grid(row=1, column=2)
button6.bind("<Enter>", on_enter6)
button6.bind("<Leave>", on_leave6)

button7 = tk.Button(frame1, height=200, width=200, image=back, command=click7, cursor="hand2")
button7.grid(row=2, column=0)
button7.bind("<Enter>", on_enter7)
button7.bind("<Leave>", on_leave7)

button8 = tk.Button(frame1, height=200, width=200, image=back, command=click8, cursor="hand2")
button8.grid(row=2, column=1)
button8.bind("<Enter>", on_enter8)
button8.bind("<Leave>", on_leave8)

button9 = tk.Button(frame1, height=200, width=200, image=back, command=click9, cursor="hand2")
button9.grid(row=2, column=2)
button9.bind("<Enter>", on_enter9)
button9.bind("<Leave>", on_leave9)

while not root.finalState(configuration):
    if machine == 'x':
        root = Node("root", configuration, depth)
        root.createChildren()
        next_step = 0
        for child in root.children:
            if child.value == root.value:
                next_step = int(child.name)
        if configuration == initial:
            next_step = random.randrange(1, 10)
        configuration[next_step] = 'x'
        if next_step == 1:
            button1.configure(image=s1, state='disabled', cursor='X_cursor')
        if next_step == 2:
            button2.configure(image=s1, state='disabled', cursor='X_cursor')
        if next_step == 3:
            button3.configure(image=s1, state='disabled', cursor='X_cursor')
        if next_step == 4:
            button4.configure(image=s1, state='disabled', cursor='X_cursor')
        if next_step == 5:
            button5.configure(image=s1, state='disabled', cursor='X_cursor')
        if next_step == 6:
            button6.configure(image=s1, state='disabled', cursor='X_cursor')
        if next_step == 7:
            button7.configure(image=s1, state='disabled', cursor='X_cursor')
        if next_step == 8:
            button8.configure(image=s1, state='disabled', cursor='X_cursor')
        if next_step == 9:
            button9.configure(image=s1, state='disabled', cursor='X_cursor')
        input()

    if machine == 'o':
        input()

rooter.mainloop()
