
def find_closest(array, num):

    if len(array) == 0:
        return None
    
    if len(array) == 1:
        return array[0]

    while len(array) >= 2:
        mid = int(len(array) / 2)

        if(array[mid] == num):
            return num
        else:
            if array[mid] > num:
                array = array[:mid]
            else:
                array = array[mid+1:]

    return array[0]

a = [1, 2, 4, 5, 6, 6, 8, 9]
print(find_closest(a, 11))
print(find_closest(a, 4))