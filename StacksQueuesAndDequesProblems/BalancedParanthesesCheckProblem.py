# PROBLEM: Given a string of opening and closing parentheses,
# check whether it's balanced. We have 3 types of parentheses: 
#round brackets:(), square brackets : [], and curly brackets: {}.
# Assume that the string doesn't contain any other character than these, 
#no spaces words or numbers.
# As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened.
# For example '([])' is balanced but '([)]' is not. You can assume the input string has no spaces 


def balance_check(s):

    if len(s)%2 !=0: return False

    openings = set('({[')
    matches = set([('(',')'),('{','}'),('[',']')])

    stack = []
    
    for parantheses in s :
        if parantheses in openings:
            stack.append(parantheses)
        else:
            if len(stack)==0:
                return False
            last_open=stack.pop()
            if(last_open,parantheses) not in matches:
                return False
    return len(stack) == 0
            



print(balance_check("()"))
print(balance_check("())[]"))

