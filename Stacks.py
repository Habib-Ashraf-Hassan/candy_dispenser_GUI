import random
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty. Cannot peek.")

    def size(self):
        return len(self.items)
    

# candy_colors = ['red', 'yellow', 'blue', 'green', 'orange', 'pink',
#                 'black', 'purple', 'brown', 'gray', 'cyan', 'magenta',
#                 'lightgray', 'darkorange', 'white', 'indigo']

# candy = random.choice(candy_colors)
# s = Stack()
# s.push(candy)
# print(type(s.pop()))
