
from Stack import Stack

def string_reverse(my_string):
    s = Stack()
    for char in my_string:
        s.push(char)
    
    reversed_string = ""
    while not s.is_empty():        
        reversed_string += s.pop()

    print(reversed_string)


string_reverse("Hello")
string_reverse("!evitacudE ot emocleW")



    

