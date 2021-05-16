def insertion_sort(array):
    for x in range(len(array)):
        curr = array[x]
        j = x-1
        while j >= 0 and array[j] > curr:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = curr
    print(array)

a = [4, 1, 5, 2, 3]
insertion_sort(a)