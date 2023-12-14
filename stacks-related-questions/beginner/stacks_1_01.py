# Implement a stack using an array/linked list.
# Write a function to check if a stack is empty.
# Reverse a string using a stack.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self): #check if stack is  
        return True if not self.items else False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

def reverse_string (s):
    stack = Stack()
    if len(s) < 2:
        return s

    for char in s:
        stack.push(char)

    revStr = ''

    while not stack.is_empty():
        revStr += stack.pop()

    return revStr


input_str = "Hello, world!"
reversed_str = reverse_string(input_str)
print("Reversed String:", reversed_str)

# newStack = Stack()
# newStack.push(3)
# newStack.pop()
# newStack.pop()
# print(newStack.items)
# print(newStack.is_empty())

