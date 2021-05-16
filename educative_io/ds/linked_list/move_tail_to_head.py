from linked_list import LinkedList

def move_tail_to_head(linked_list):
    curr_node = linked_list.head
    prev_node = None

    while curr_node:

        if curr_node.next is None:
            prev_node.next = None
        
        prev_node = curr_node
        curr_node = curr_node.next

    prev_node.next = linked_list.head
    linked_list.head = prev_node

    linked_list.print_list()


linked_list = LinkedList()
linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")
linked_list.append("E")
move_tail_to_head(linked_list)

# A B C D E

# E A B C D