# Implement a stack using an array/linked list.
# Write a function to check if a stack is empty.
# Reverse a string using a stack.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return True if not self.items else False

    def push(self, item):
        self.items.append(item)


# print(Stack().push(4))
# print(Stack().is_empty())