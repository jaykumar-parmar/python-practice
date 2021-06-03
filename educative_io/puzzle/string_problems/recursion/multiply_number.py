
# TO DO: Use memoization to improve performance
def recursive_multiply(x, y):
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y-1)

print(recursive_multiply(1000, 1000))
