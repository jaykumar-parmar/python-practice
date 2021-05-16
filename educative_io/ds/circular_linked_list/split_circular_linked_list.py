from circular_list import CircularLinkedList

def get_length(input_list):
    list_length = 0
    curr_node = input_list.head
    while curr_node:
        list_length += 1

        if curr_node.next is input_list.head:
            break
        else:
            curr_node = curr_node.next
        
    return list_length

def sub_list(start_index, end_index, circular_list):
     
     curr_node = circular_list.head
     temp_index = 0
     while temp_index is not start_index:
         curr_node = curr_node.next
         temp_index += 1

     half_circular_linked_list = CircularLinkedList()
    
     while start_index < end_index:
        half_circular_linked_list.append(curr_node.data)
        curr_node = curr_node.next
        start_index += 1
    
     return half_circular_linked_list

def split(input_list):

    list_length = get_length(input_list)
    mid = int(list_length/2)

    stack = []
    
    half_circular_linked_list = sub_list(0, mid, input_list)
    stack.append(half_circular_linked_list)

    half_circular_linked_list = sub_list(mid, list_length, input_list)
    stack.append(half_circular_linked_list)

    stack[0].print_list()
    stack[1].print_list()




cl = CircularLinkedList()
cl.append("A")
cl.append("B")
cl.append("C")
cl.append("D")
cl.prepend("-A")
cl.print_list()
split(cl)