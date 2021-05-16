class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.node_count = 0

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head

            while last_node.next:
                last_node = last_node.next

            last_node.next = new_node

        self.node_count += 1

    def prepend(self, data):
        new_node = Node(data)

        if self.head is Node:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.node_count += 1

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        node = self.head
        my_str = ""

        while node:
            my_str += str(node.data)
            node = node.next

        print(my_str)

    def get_node_by_index(self, index):

        if index > self.len():
            return None

        node = self.head
        while index > 0:
            node = node.next
            index -= 1

        return node

    def delete_by_value(self, value):

        if self.head is None:
            return

        node_to_be_deleted = self.head
        if node_to_be_deleted.data == value:
            self.head = self.head.next
            node_to_be_deleted = None
            return

        parent_node = node_to_be_deleted
        node_to_be_deleted = node_to_be_deleted.next

        while node_to_be_deleted:
            if node_to_be_deleted.data == value:
                parent_node.next = node_to_be_deleted.next
                break
            else:
                parent_node = node_to_be_deleted
                node_to_be_deleted = node_to_be_deleted.next

    def len(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def swap_nodes(self, node_data_1, node_data_2):
        if self.head is None:
            return

        if node_data_1 == node_data_2:
            return

        node_1 = self.head
        node_1_parent = None

        while node_1 and node_1.data != node_data_1:
            node_1_parent = node_1
            node_1 = node_1.next

        if node_1 is None:
            return

        node_2 = self.head
        node_2_parent = None

        while node_2 and node_2.data != node_data_2:
            node_2_parent = node_2
            node_2 = node_2.next

        if node_2 is None:
            return

        if node_1 == self.head or node_2 == self.head:

            if node_1_parent is None:
                self.head = node_2
                node_2_parent.next = node_1
            else:
                self.head = node_1
                node_1_parent.next = node_2
        else:
            node_1_parent.next = node_2
            node_2_parent.next = node_1

        nex_node_link = node_1.next  # C
        node_1.next = node_2.next  # D
        node_2.next = nex_node_link  # C

    def reverse_iterative(self):
        prev_node = None
        curr_node = self.head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node

    def reverse_recursive(self, node=None):

        if node is None:
            node = self.head

        if node.next is None:
            self.head = node
            return node
        else:
            result_node = self.reverse_recursive(node.next)
            result_node.next = node
            node.next = None
            return node



