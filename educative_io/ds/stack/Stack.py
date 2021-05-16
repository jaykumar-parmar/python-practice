class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def get_length(self):
        return len(self.items)

    def to_string(self):
        my_str = ""

        while not self.is_empty():
            my_str += str(self.pop())

        return my_str
