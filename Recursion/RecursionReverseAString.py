# PROBLEM : Reverse the string with recursion

def reverseString(s):
    # Base case is if length of s smaller than 1 returning s 
    if len(s) <= 1:
        return s   
    
    # With this recursive call reversing the string 
    return reverseString(s[1:]) + s[0]

print(reverseString("Hello World"))