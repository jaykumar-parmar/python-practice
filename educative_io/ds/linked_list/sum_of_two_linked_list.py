from linked_list import LinkedList


def get_number_from_linked_list(linked_list):
    number = 0
    tens = 1

    curr_node = linked_list.head

    while curr_node:
        number += tens * int(curr_node.data)
        tens *= 10
        curr_node = curr_node.next

    return number


def sum_two_lists(llist1, llist2):
    num1 = get_number_from_linked_list(llist1)
    num2 = get_number_from_linked_list(llist2)
    sum = num1 + num2

    sum_linked_list = LinkedList()

    while sum > 0:
        sum_linked_list.append(int(sum % 10))
        sum = int(sum/10)

    return sum_linked_list.print_list()


ll_1 = LinkedList()
ll_1.append(5)
ll_1.append(6)
ll_1.append(3)

ll_2 = LinkedList()
ll_2.append(8)
ll_2.append(4)
ll_2.append(2)

sum_two_lists(ll_1, ll_2)
