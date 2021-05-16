from linked_list import LinkedList

def rotate_by_pivot(linked_list, pivot):
    
    curr_node = linked_list.head
    index = 1

    while index < pivot and curr_node:
        curr_node = curr_node.next
        index += 1
    
    if index < pivot and curr_node is None:
        return None
    
    pivot_node = curr_node.next
    curr_node.next = None
    
    prev_node = None
    last_node = pivot_node.next
    
    while last_node:
        prev_node = last_node
        last_node = last_node.next

    prev_node.next = linked_list.head
    linked_list.head = pivot_node

    linked_list.print_list()


list_1 = LinkedList()
list_1.append(1)
list_1.append(2)
list_1.append(3)
list_1.append(4)
list_1.append(5)

rotate_by_pivot(list_1, 3)
