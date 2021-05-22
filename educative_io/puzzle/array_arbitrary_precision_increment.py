def increment(array):
    s = ''.join(map(str, array))
    print(int(s) + 1)


increment(['1', '4', '9'])
increment(['9', '9', '9'])