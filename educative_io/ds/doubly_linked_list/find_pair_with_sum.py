from doubly_list import DoublyLinkedList


def find_pair_equal_to_sum(sum, input_list, input_list_length):

    if input_list_length == 0:
        return []
            
    unique_data = [0] * input_list_length
    sorted_list = DoublyLinkedList()

    node = input_list.head
    last_inserted = None
    while node:

        if node.data < sum:
            if not sorted_list.head:
                last_inserted = sorted_list.append(node.data)
            else:
                if unique_data[node.data] == 1:
                    continue
                else:
                    unique_data[node.data] = 1
                    if last_inserted.data < node.data:
                        last_inserted = sorted_list.append(node.data)
                    else:
                        last_inserted = sorted_list.insert_before(last_inserted.data, node.data)
        node = node.next

    left_ptr = sorted_list.head
    right_ptr = sorted_list.head

    while right_ptr:

        if right_ptr.next is None:
            break
        
        right_ptr = right_ptr.next

    pairs = []

    while left_ptr.data < right_ptr.data:
        if left_ptr.data + right_ptr.data == sum:
            pairs.append([left_ptr.data, right_ptr.data])
            left_ptr = left_ptr.next
            right_ptr = right_ptr.prev
        elif left_ptr.data + right_ptr.data > sum:
            right_ptr = right_ptr.prev
        else:
            left_ptr = left_ptr.next

    print(pairs)


# dl = DoublyLinkedList()
# dl.append(1)
# dl.append(2)
# dl.append(3)
# dl.append(4)
# dl.append(5)
# dl.print_list()
# find_pair_equal_to_sum(5, dl, 5)

print("\n")
dl = DoublyLinkedList()
dl.append(5)
dl.append(4)
dl.append(3)
dl.append(2)
dl.append(1)
dl.print_list()
find_pair_equal_to_sum(5, dl, 5)

print("\n")
dl = DoublyLinkedList()
dl.append(2)
dl.append(4)
dl.append(6)
dl.append(8)
dl.append(10)
dl.print_list()
find_pair_equal_to_sum(14, dl, 11)

print("\n")
dl = DoublyLinkedList()
dl.print_list()
find_pair_equal_to_sum(0, dl, 0)