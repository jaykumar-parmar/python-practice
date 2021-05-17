
def can_reach_end(array, idx) -> bool:

    if idx == len(array) - 1:
        return True
    
    if array[idx] == 0:
        return False
    
    curr_idx = array[idx]

    if curr_idx + idx == len(array) - 1:
        return True
    
    while curr_idx > 0:
        if((idx + curr_idx < len(array)) and array[idx + curr_idx] != 0):
            next_jump = array[idx + curr_idx]
            while next_jump > 0:
                if((idx + curr_idx + next_jump < len(array)) and array[idx + curr_idx + next_jump] != 0):
                    return can_reach_end(array, idx + curr_idx)
                next_jump -= 1
        
        curr_idx -= 1

    return False

def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx

a = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(a, 0))

a = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(a, 0))




