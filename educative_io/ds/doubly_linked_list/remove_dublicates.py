from doubly_list import DoublyLinkedList


def remove_dups(input_list):
    list_dict = dict()

    node = input_list.head
    while node:
        if node.data in list_dict:
            input_list.delete_node_by_node(node)
        else:
            list_dict[node.data] = node
        
        node = node.next

    input_list.print_list()


dllist = DoublyLinkedList()
dllist.append(8)
dllist.append(4)
dllist.append(4)
dllist.append(6)
dllist.append(4)
dllist.append(8)
dllist.append(4)
dllist.append(10)
dllist.append(12)
dllist.append(12)
dllist.append(12)
remove_dups(dllist)

# dllist = DoublyLinkedList()
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.append(4)

# dllist.delete_node(1)
# dllist.delete_node(6)
# dllist.delete_node(4)

# dllist.delete_node(3)
# dllist.print_list()
