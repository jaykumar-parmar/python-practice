from linked_list import LinkedList

def remove_dups(linked_list):
    unique_node_data = dict()
    prev = None
    curr = linked_list.head

    while curr:
        if curr.data in unique_node_data:
            prev.next = curr.next
            curr = None
        else:
            unique_node_data[curr.data] = curr
            prev = curr
            
        curr = prev.next

        
    return linked_list.print_list()


link_list = LinkedList()
link_list.append(1)
link_list.append(2)
link_list.append(3)
link_list.append(4)
link_list.append(3)
link_list.append(3)
link_list.append(3)
remove_dups(link_list)


