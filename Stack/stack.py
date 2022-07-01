from sys import maxsize

class stack:

    # initializing empty stack
    def __init__(self):
        self.stack = []

    # function to check if stack is empty or not
    def isEmpty(self):
        return len(self.stack) == 0

    # function for pussing elements in stack
    def push(self, item):
        self.stack.append(item)

        print(f"{item} pushed into stack")

    # function to pop elements from stack
    def pop(self):
        if self.isEmpty():
            return -maxsize - 1

        return self.stack.pop()

    # function to print element at the top of stack
    def peek(self):
        if self.isEmpty():
            return -maxsize - 1

        return self.stack[len(self.stack) - 1]

    # size of the stack
    def size(self):
        return len(self.stack)


s = stack() # creating stack
s.push(23)
s.push(12)
s.push(54)
s.push(20)
print(f"{s.pop()} is popped from stack ")
print(f"{s.peek()} is at top of the stack")
print(f"Size of stack is {s.size()}")

## printing stack elements
print("Elements present in stack are :")
while(not s.isEmpty()):
    print(s.peek(), end = " ")
    s.pop()







