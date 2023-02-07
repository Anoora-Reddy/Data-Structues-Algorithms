"Importing Stack Class from Stack.py"

from Stack import Stack

def balanced_parenthesis(paren_string):
    
    s = Stack()
    
    match = {'}':'{', ']':'[', ')':'('}
    for i in paren_string:
        if i == "{" or i == "[" or i == "(":
            s.push(i)
        else:
            if not s.is_empty():
                top = s.pop()
                if top != match[i]:
                    return False
            else:
                return False
    if s.is_empty():
        return True
    return False

input_parenthesis = input('Input Parenthesis: ')

print(balanced_parenthesis(input_parenthesis))