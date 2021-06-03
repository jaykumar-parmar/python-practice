
# TO DO : Combine both while loop
def integer_square_root(k):

    mid_value = int(k / 2)

    if (mid_value * mid_value) == k:
        return mid_value
    
    low = mid_value

    while (low * low) > k:
        low = int(low / 2)

    high = (low * 2) - 1
    last_low = low
   
    while low <= high:
        mid = int((high + low) / 2)

        if mid * mid > k:
            high = mid - 1
        else:
            last_low = low
            low = mid + 1
    
    return last_low
    


print(integer_square_root(300))