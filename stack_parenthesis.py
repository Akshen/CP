"""
Determine whether or not a string has balanced usage

Eg:
    (), ()() <- Balanced
    (()]     <- UnBalanced
    ([)]  <- Odd Case
"""
from stack import Stack

def is_match(p1, p2):
    return True if p1+p2 in ["()", "{}", "[]"] else False

def check(string):
    stk_obj = Stack()
    is_balanced = 1
    i = 0
    while i<len(string) and is_balanced:
        if string[i] in "[{(":
            stk_obj.push(string[i])
        else:
            if stk_obj.is_empty():
                is_balanced = 0
            else:
                top = stk_obj.pop()
                if not is_match(top, string[i]):
                    is_balanced = 0
        i +=1
    if not stk_obj.is_empty():
        is_balanced = 0
    return is_balanced

print(check("[]{}"))