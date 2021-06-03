from pygments import highlight


def is_palindrome(s):
    low = 0
    high = len(s) - 1

    while low < high:

        while not s[low].isalnum() and low < high:
            low += 1
        while not s[high].isalnum() and low < high:
            high -= 1

        if str(s[low]).capitalize() != str(s[high]).capitalize():
            return False
        
        low += 1
        high -= 1
    
    return True

print(is_palindrome("Was it a cat I saw"))