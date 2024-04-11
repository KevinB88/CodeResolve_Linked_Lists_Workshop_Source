import random


class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)


class SkipList:
    def __init__(self, max_lvl, P):
        self.MAX_LVL = max_lvl
        self.P = P
        self.header = self.createNode(self.MAX_LVL, -1)
        self.level = 0

    def createNode(self, lvl, value):
        return Node(value, lvl)

    def randomLevel(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LVL:
            lvl += 1
        return lvl

    def insert(self, value):
        update = [None] * (self.MAX_LVL + 1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current is None or current.value != value:
            rlevel = self.randomLevel()
            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                self.level = rlevel
            newNode = self.createNode(rlevel, value)
            for i in range(rlevel + 1):
                newNode.forward[i] = update[i].forward[i]
                update[i].forward[i] = newNode


    def displayList(self):
        print("Skip List")
        for lvl in range(self.level + 1):
            print("Level {}: ".format(lvl), end=" ")
            node = self.header.forward[lvl]
            while node != None:
                print(node.value, end=" ")
                node = node.forward[lvl]
            print("")

# Example Usage
skipList = SkipList(3, 0.5)
skipList.insert(3)
skipList.insert(6)
skipList.insert(7)
skipList.insert(9)
skipList.insert(12)
skipList.insert(19)
skipList.insert(17)

skipList.displayList()
