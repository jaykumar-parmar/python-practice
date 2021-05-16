class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):

        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            last_node = self.head

            while last_node.next is not None:
                last_node = last_node.next

            last_node.next = node
            node.prev = last_node
        
        return node

    def print_list(self):
        node = self.head
        my_str = ""

        while node:
            my_str += str(node.data)
            if node.next is None:
                break
            else:
                node = node.next

        print(my_str)

    def prepend(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        
        return node

    def get_node_by_key(self, key):
        node = self.head

        while node:
            if node.data == key:
                return node

            node = node.next

    def insert_after(self, parent_node_data, data):
        parent_node = self.get_node_by_key(parent_node_data)

        if not parent_node:
            return

        node = Node(data)
        node.next = parent_node.next
        node.prev = parent_node

        parent_node.next = node

        if node.next:
            node.next.prev = node
        
        return node

    def insert_before(self, child_node_key, data):
        child_node = self.get_node_by_key(child_node_key)

        if not child_node:
            return

        node = Node(data)
        node.next = child_node
        node.prev = child_node.prev

        if child_node.prev:
            child_node.prev.next = node
        else:
            self.head = node

        child_node.prev = node
    
        return node

    def delete_node(self, key):
        node = self.get_node_by_key(key)
        self.delete_node_by_node(node)
       

    def delete_node_by_node(self, node):

        if not node:
            return

        if node.next:
            node.next.prev = node.prev

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        node = None
