#PROBLEM : Given a string, determine if it is compreised of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True
# The string 'aabcde' contains duplicate characters and should return false


def uniqueCharacter(s):
    # Defining dictionary for add all letters to allLetters
    allLetters = {}
    
    for letter in s:
        # If letter is created in allLetters returning False
        if allLetters.get(letter):
            return False
        # Else creating letter in allLetters
        else:
            allLetters[letter]=1
    # If did not return False returning True
    return True

a = uniqueCharacter("abcedd")
print("Unique Character In String Problem : " + str(a))




# !-----------------------------------------------------------------------
# Second Solution

def uniqueCharacter2(s):
    # Because of sets in python must unique characters. Comparing lengths of set of s 
    # and string s if they are not equal returning false if it is returning True
    return len(set(s))==len(s)

b = uniqueCharacter2("abced")
print("Unique Character In String Solution2 : " + str(b))


