#PROBLEM : Given a string, determine if it is compreised of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True
# The string 'aabcde' contains duplicate characters and should return false


def uniqueCharacter(s):
    
    i=1
    length=len(s)
    while i<length:
        if s[i] == s[i-1]:
            return False
        i+=1
    return True


a = uniqueCharacter("")
print(a)