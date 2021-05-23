
def intersection(array1, array2):
    i = 0
    j = 0
    intersection_array = []
    
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            i += 1
        elif array1[i] > array2[j]:
            j += 1
        else:
            intersection_array.append(array1[i])
            i += 1
            j += 1
    print(intersection_array)


a = [2, 3, 3, 5, 7, 11]
b = [3, 7]
intersection(a, b)