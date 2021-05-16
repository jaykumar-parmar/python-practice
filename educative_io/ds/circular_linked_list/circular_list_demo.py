from circular_list import CircularLinkedList

cl = CircularLinkedList()
cl.append("A")
cl.append("B")
cl.append("C")
cl.append("D")
cl.prepend("-A")
cl.print_list()
cl.remove("C")
cl.remove("D")
cl.remove("-A")
cl.print_list()