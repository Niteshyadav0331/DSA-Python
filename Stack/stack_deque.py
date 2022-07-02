from collections import deque
from sys import maxsize

class stack:

    def __init__(self):
        self.stack = deque()

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

        print(f"{item} pushed into stack")

    def pop(self):
        if self.isEmpty():
            return -maxsize - 1

        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return -maxsize - 1

        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)


s = stack()
s.push(24)
s.push(26)
s.push(28)
s.push(30)
print(f"{s.pop()} popped from stack ")
print(f"{s.peek()} is at top of the stack")
print(f"Size of stack is {s.size()}")

print("Elements of stack are: ")
while(not s.isEmpty()):
    print(s.peek(), end = " ")
    s.pop()

    

