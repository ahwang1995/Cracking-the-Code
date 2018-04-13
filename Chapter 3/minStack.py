#stack class from http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html
#stack with the added functionality of returning the minimum element
class minStack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def minVal(self):
        return min(self.items)

s = minStack()
s.push(3)
s.push(5)
s.push(1)
print s.minVal()