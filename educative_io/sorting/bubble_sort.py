
def bubble_sort(array):
    swapped = True

    if len(array) > 1:
        while(swapped):
            swapped = False
            for i in range(len(array)-1):
                if array[i] > array[i+ 1]:
                    swap(i, i+1, array)
                    swapped = True
    

    print(array)

def swap(idx1, idx2, array):
    temp = array[idx2]
    array[idx2] = array[idx1]
    array[idx1] = temp



a = [4, 2, 1, 3]
bubble_sort(a)
