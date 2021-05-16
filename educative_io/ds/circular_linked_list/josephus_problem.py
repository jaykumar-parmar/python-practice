from circular_list import CircularLinkedList

def josephus_problem(circular_list, step_size):

    step_executed = 1
    curr_node = circular_list.head

    while step_executed <= step_size and curr_node.next is not curr_node:
        if step_executed is step_size:
            next_node = curr_node.next
            circular_list.remove(curr_node.data)
            curr_node = next_node
            step_executed = 1
        else:
            curr_node = curr_node.next
            step_executed += 1

    circular_list.print_list()


cl = CircularLinkedList()
cl.append("A")
cl.append("B")
cl.append("C")
cl.append("D")
cl.append("E")
cl.print_list()
josephus_problem(cl, 3)
    