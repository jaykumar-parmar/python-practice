from linked_list import LinkedList



ll_reverse_itr = LinkedList()
ll_reverse_itr.append("A")
ll_reverse_itr.append("B")
ll_reverse_itr.append("C")
ll_reverse_itr.append("D")
ll_reverse_itr.append("E")
ll_reverse_itr.print_list()

print("\n reverse iterative")
ll_reverse_itr.reverse_iterative()
ll_reverse_itr.print_list()

print("\n reverse recursive")
ll_reverse_itr.reverse_recursive()
ll_reverse_itr.print_list()

print("\n-----------------------------------------------\n")

ll_swap = LinkedList()
ll_swap.append("A")
ll_swap.append("B")
ll_swap.append("C")
ll_swap.append("D")
ll_swap.print_list()

ll_swap.swap_nodes("B", "C")
ll_swap.print_list()

ll_swap.swap_nodes("A", "D")
ll_swap.print_list()

ll_swap.swap_nodes("C", "D")
ll_swap.print_list()

print("\n-----------------------------------------------\n")

ll_delete_by_value = LinkedList()
ll_delete_by_value.append("A")
ll_delete_by_value.append("B")
ll_delete_by_value.append("C")
ll_delete_by_value.append("D")
ll_delete_by_value.print_list()
ll_delete_by_value.delete_by_value("A")
ll_delete_by_value.print_list()

ll_delete_by_value.delete_by_value("C")
ll_delete_by_value.print_list()

ll_delete_by_value.delete_by_value("D")
ll_delete_by_value.print_list()



print("\n-----------------------------------------------\n")

ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
ll.append("E")
ll.prepend("1")
ll.prepend("2")
ll.prepend("3")
ll.print_list()

node_at_3 = ll.get_node_by_index(3)
print(node_at_3.data)

ll.insert_after_node(node_at_3, "A2")
ll.print_list()



