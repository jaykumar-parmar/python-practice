from Stack import Stack


my_stack = Stack()


def find_binary_by_recusrion(n):

    if n <= 1:
        my_stack.push(n)
    else:
        my_stack.push(n % 2)
        find_binary_by_recusrion(int(n / 2))

    return my_stack


def find_binary_by_iteration(n):

    if(n == 0):
        return "0"
    
    my_stack = Stack()
    my_str = "" 

    while n >= 1:
        my_stack.push(str(n % 2))
        n = int(n / 2)
    
    my_str = my_stack.to_string()
    return my_str


print(find_binary_by_iteration(0))
print(find_binary_by_iteration(1))
print(find_binary_by_iteration(2))
print(find_binary_by_iteration(3))
print(find_binary_by_iteration(242))


print("\n______________________________________________________\n")


result = find_binary_by_recusrion(0)
print(result.to_string())

result = find_binary_by_recusrion(1)
print(result.to_string())

result = find_binary_by_recusrion(2)
print(result.to_string())

result = find_binary_by_recusrion(3)
print(result.to_string())

result = find_binary_by_recusrion(242)
print(result.to_string())
