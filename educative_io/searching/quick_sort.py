
def quick_sort(array, low, high):
    if len(array) == 0 or low >= high:
        return array
    
    pivot = partition(array, low, high)
    quick_sort(array, low, pivot-1)
    quick_sort(array, pivot+1, high)
    return array

def partition(array, low, high):
    i = low
    j = high -1
    curr = array[high]

    while i <= j:
        while array[i] < curr:
            i += 1
        while array[j] > curr:
            j -= 1
        swap(i,j,array)

    swap(j, high, array)
    
    return j

def swap(i, j, array):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


a = [4, 11, 7]
print(quick_sort(a, 0, (len(a) - 1)))

