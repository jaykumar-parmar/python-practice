class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None
    
    def append(self, data):
        node = Node(data)

        if self.head:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            
            curr_node.next = node
        else:
            self.head = node
        
        node.next = self.head

    def prepend(self, data):
        node = Node(data)

        curr_node = self.head
        while curr_node:
            if curr_node.next is self.head:
                break
            curr_node = curr_node.next
             
        curr_node.next = node
            
        node.next = self.head
        self.head = node

    def remove(self, key):
        prev_node = None
        curr_node = self.head

        while curr_node:
            if curr_node.data is key:
                break

            if curr_node.next is self.head:
                curr_node = None
                break
            
            prev_node = curr_node
            curr_node = curr_node.next
        
        if not curr_node:
            return

        if prev_node:
            prev_node.next = curr_node.next
        else:
            last_node = self.head
            while last_node:
                if last_node.next is self.head:
                    break
                last_node = last_node.next

            self.head = self.head.next
            last_node.next = self.head

        curr_node = None


    def print_list(self):
        my_str = ""
        curr_node = self.head
        while curr_node:
            my_str += str(f"{curr_node.data} " )
            
            if curr_node.next is self.head:
                break
            
            curr_node = curr_node.next
        
        print(my_str)


