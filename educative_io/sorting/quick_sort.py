def quick_sort(array, low, high):

    if low < high:
        p = partition(array, low, high)
        quick_sort(array, low, p-1)
        quick_sort(array, p+1, high)
    
    return array

def partition(array, low, high):
    
    pivot = array[low]
    i = low
    j = high

    while i < j:
        
        while i < len(array) and array[i] <= pivot:
            i += 1
        
        while array[j] > pivot:
            j -= 1
    
        if i < j:
            swap(i, j, array)
    
    swap(j, low, array)
    return j

def swap(i, j, array):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


a = [11, 13, 7, 12]
print(quick_sort(a, 0, (len(a) - 1)))