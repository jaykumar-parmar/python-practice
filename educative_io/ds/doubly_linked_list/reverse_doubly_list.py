from doubly_list import DoublyLinkedList

def reverse_doubly(doubly_list):

    curr_node = doubly_list.head

    while curr_node:
        temp_node = curr_node.next
        curr_node.next = curr_node.prev
        curr_node.prev = temp_node
        curr_node = temp_node

        if curr_node:
            doubly_list.head = curr_node
    
    doubly_list.print_list()


dl = DoublyLinkedList()
dl.append("A")
dl.append("B")
dl.append("C")
dl.append("D")

reverse_doubly(dl)