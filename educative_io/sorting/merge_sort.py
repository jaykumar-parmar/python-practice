def merge_sort(array):

    if len(array) == 1:
        return array
    else:
        mid = int(len(array)/2)
        left_array = merge_sort(array[:mid])
        right_array = merge_sort(array[mid:])

        i = 0
        j = 0
        sorted_array = []

        while(i < len(left_array) and j < len(right_array)):
            if(left_array[i] < right_array[j]):
                sorted_array.append(left_array[i])
                i += 1
            else:
                sorted_array.append(right_array[j])
                j += 1
        
        while(i < len(left_array)):
            sorted_array.append(left_array[i])
            i += 1

        while (j < len(right_array)):
            sorted_array.append(right_array[j])
            j += 1
        
        return sorted_array





a = [6,5, 3, 1, 8, 7, 2, 4]
print(merge_sort(a))
