from Stack import Stack


class AreBracketsBalanced:
    def __init__(self):
        self.open_brackets = "([{"
        self.closed_brackets = ")]}"

    def is_bracket_balanced(self, bracket_string):
        stack = Stack()
        is_balanced = True
        
        for item in bracket_string:
            if item in self.open_brackets:
                stack.push(item)
            else:

                if(item not in self.closed_brackets):
                    continue

                if stack.is_empty() == False and self.is_match(item, stack.peek()):
                    stack.pop()
                else:
                    is_balanced = False
                    break;

        return stack.is_empty() and is_balanced

    def is_match(self, current_bracket, stack_bracket):
        return (stack_bracket == "(" and current_bracket == ")") or (
            stack_bracket == "[" and current_bracket == "]" or (stack_bracket == "{" and current_bracket == "}")
        )


bracketBalanced = AreBracketsBalanced()
print(bracketBalanced.is_bracket_balanced("(()"))
print(bracketBalanced.is_bracket_balanced("{{{)}]"))
print(bracketBalanced.is_bracket_balanced("[ ] [ ] ] ]"))


print(bracketBalanced.is_bracket_balanced("{ }"))
print(bracketBalanced.is_bracket_balanced("{ } { }"))
print(bracketBalanced.is_bracket_balanced("( ( { [ ] } ) )"))
