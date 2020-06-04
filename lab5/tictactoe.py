import random
import tkinter as tk


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
                    self.value = self.depth
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


global machine, button1, button2, button3, button4, button5, button6, button7, button8, button9, button, buttons
depth = -1
if random.randrange(0, 2) == 0:
    print('Machine starts')
    machine = 'x'
    depth = 0
else:
    print('You start')
    machine = 'o'
    depth = 1

initial = ['' for i in range(10)]
configuration = ['' for i in range(10)]
root = Node("root", configuration, depth)
while not root.finalState(configuration):
    if machine == 'x':
        root.createChildren()
        next_step = 0
        for child in root.children:
            if child.value == root.value:
                next_step = int(child.name)
        if configuration == initial:
            next_step = random.randrange(1, 10)
        print(next_step)
        configuration[next_step] = 'x'
        root = Node("root", configuration, depth)
        if root.finalState(configuration):
            if root.value == -1:
                print('You won')
            elif root.value == 0:
                print('Draw')
            else:
                print('You lost')
            break
        posibilities = root.findEmptyBoxes(configuration)
        posibilities = list(map(str, posibilities))
        print(posibilities)
        pos = input()
        while not pos in posibilities:
            print('Select an available spot!')
            pos = input()
        configuration[int(pos)] = 'o'
        root = Node("root", configuration, depth)
        print(configuration)
        if root.finalState(configuration):
            if root.value == -1:
                print('You won')
            elif root.value == 0:
                print('Draw')
            else:
                print('You lost')
            break
    if machine == 'o':
        posibilities = root.findEmptyBoxes(configuration)
        posibilities = list(map(str, posibilities))
        print(posibilities)
        pos = input()
        while not pos in posibilities:
            print('Select an available spot!')
            pos = input()
        configuration[int(pos)] = 'x'
        root = Node("root", configuration, depth)
        root.createChildren()
        next_step = 0
        for child in root.children:
            if child.value == root.value:
                next_step = int(child.name)
        print(next_step)
        configuration[next_step] = 'o'
        root = Node("root", configuration, depth)
        if root.finalState(configuration):
            if root.value == -1:
                print('You won')
            elif root.value == 0:
                print('Draw')
            else:
                print('You lost')
            break
