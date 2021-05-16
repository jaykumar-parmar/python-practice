from doubly_list import DoublyLinkedList

dl = DoublyLinkedList()
dl.append("A") 
dl.append("B")
dl.append("C")
dl.append("D")
dl.append("E")
dl.append("F") #ABCDEF
dl.prepend("-A") #-AABCDEF
dl.insert_after("E", "E+") #-AABCDEE+F
dl.insert_after("F", "G")  #-AABCDEE+FG
dl.insert_after("A", "A+") #-AAA+BCDEE+FG

dl.insert_before("-A", "-B") #-B-AAA+BCDEE+FG
dl.insert_before("G", "F+") #-B-AAA+BCDEE+FF+G

dl.delete_node("-B")
dl.delete_node("-A")
dl.delete_node("E+")
dl.delete_node("A+")
dl.delete_node("F+") # ABCDDEFG
dl.print_list()