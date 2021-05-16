from linked_list import LinkedList


def merge_sorted_linked_list(list_1, list_2):
    node_ptr_1 = None
    node_ptr_2 = None
    merge_list = LinkedList()

    node_ptr_1 = list_1.head
    node_ptr_2 = list_2.head

    while node_ptr_1 is not None and node_ptr_2 is not None:
        new_node_data = None
        
        if node_ptr_1.data < node_ptr_2.data:
            new_node_data = node_ptr_1.data
            node_ptr_1 = node_ptr_1.next
        else:
            new_node_data = node_ptr_2.data
            node_ptr_2 = node_ptr_2.next

        merge_list.append(new_node_data)


    while node_ptr_1 is not None:
        merge_list.append(node_ptr_1.data)
        node_ptr_1 = node_ptr_1.next

    while node_ptr_2 is not None:
        merge_list.append(node_ptr_2.data)
        node_ptr_2 = node_ptr_2.next

    return merge_list.print_list()



list_1 = LinkedList()
list_1.append(1)
list_1.append(5)
list_1.append(6)
list_1.append(8)


list_2 = LinkedList()
list_2.append(2)
list_2.append(3)
list_2.append(4)
list_2.append(7)

merge_sorted_linked_list(list_1, list_2)
