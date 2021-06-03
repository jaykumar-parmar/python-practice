


def is_unique(my_str):

    str_len = len(my_str)
    if str_len == 1:
        return True
    
    str_dict = dict()

    i = 0
    while i < str_len:
        if my_str[i].lower() in str_dict:
            return False
        else:
            str_dict[my_str[i].lower()] = 1
    
        i += 1

    return True

print(is_unique("Hello"))
print(is_unique("BAGg"))
