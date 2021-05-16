from circular_linked_list.circular_list import CircularLinkedList
from linked_list.linked_list import LinkedList

def is_circular_list(input_list):
    is_circular = False
    curr_node = input_list.head

    while curr_node:
        if(curr_node.next is input_list.head):
            is_circular = True
            break

        curr_node = curr_node.next
    
    return is_circular



cl = CircularLinkedList()
cl.append("A")
cl.append("B")
cl.append("C")
cl.append("D")
print(is_circular_list(cl))

ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
print(is_circular_list(ll))