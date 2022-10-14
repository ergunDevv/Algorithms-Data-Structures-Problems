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