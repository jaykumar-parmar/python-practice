def find_n(A):

  if len(A) == 1:
    return 0;

  high = len(A) - 1

  while A[high] <= A[0] and high > 0:
      high -= 1

  if high == len(A) - 1:
      return 0
  else:
      return high + 1


def find(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = int((low + high)/2)

        if A[mid] <= A[0]:
            high = mid
        else:
            low = mid + 1
    
    return low

A = [6, 7, 1, 2, 3, 4, 5]
print(find(A))
