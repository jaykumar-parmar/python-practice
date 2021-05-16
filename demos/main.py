def fibonacii(n):
    if(n == 0 or n == 1):
        return n
    else:
        return fibonacii(n-2) + fibonacii(n-1)



print(fibonacii(9))
print("****************************")

def print_fibonaci(n):
    fibo = ""
    n1 = 0
    n2 = 1
    for i in range(n+1):
        if(i<2):
            fibo += " " + str(i)
        else:
            result = n1 + n2
            fibo += " " + str(result)
            n1 = n2
            n2 = result
    return fibo.strip()

print(print_fibonaci(9))