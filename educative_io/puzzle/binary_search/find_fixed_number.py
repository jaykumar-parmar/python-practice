
from operator import le
from turtle import left, right


def find_fixed_number(array):

    if len(array) == 0:
        return None
    
    left_ptr = 0
    right_ptr = len(array) - 1

    while left_ptr <= right_ptr:
        mid = int((right_ptr + left_ptr) / 2)

        if array[mid] == mid:
            return mid

        elif array[mid] < mid:
            left_ptr = mid + 1
        
        else:
            right_ptr = mid - 1

    return None


a = [-20, -10, 0, 2, 4]
print(find_fixed_number(a))