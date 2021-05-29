
def binary_search(array, key):

    a = array

    while len(a) >= 1:
        mid = int(len(a)/2)
        if(a[mid] == key):
            return True
        else:
            if a[mid] > key:
               a = a[:mid]
            else:
                a = a[mid+1:]
    return False
    

a = [6, 8, 10, 16, 21, 25]
print(binary_search(a, 21))
print(binary_search(a, 2))
print(int(1/2))