from linked_list import LinkedList

def is_palindrome_using_stack(linked_list):
    s = []
    curr_node = linked_list.head

    while curr_node:
        s.append(curr_node.data)
        curr_node = curr_node.next

    
    curr_node = linked_list.head
    while curr_node:
        if curr_node.data != s.pop():
            return False
        curr_node = curr_node.next

    return True


ll = LinkedList()
ll.append("C")
ll.append("I")
ll.append("V")
ll.append("I")
ll.append("C")

print(is_palindrome_using_stack(ll))
