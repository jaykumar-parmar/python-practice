
class MyQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items = self.items[1: self.len()]
    
    def len(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0]

    def is_empty(self):
        return self.len == 0

    def print_queue(self):
        print(self.items)
