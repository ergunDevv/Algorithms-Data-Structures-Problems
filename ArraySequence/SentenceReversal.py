# PROBLEM: Given a string of words, reverse all the words. For Example:
# Given: 'This is the best'
# Return : 'best the is This'

def sentenceReversal(str):
    # First deleting the whitespaces and splitting every word in str
    str=str.strip().split()
    # Defining reversedString which is the answer
    reversedString=""
    # And lastly adding words to reversedString with reversed order.
    for word in reversed(str):
        reversedString+=word
        reversedString+=" "
    # Returning reversedString
    return reversedString


a=sentenceReversal("  Hi John,   are you ready to go?  ")
print(a)


##!--------------------------------------------------------------------------
# Second Solution

def sentenceReversal2(str):
    words=[]
    length= len(str)
    spaces= [' ']

    i=0

    while i < length:
        
        if str[i] not in spaces:
            word_start=i

            while i <length and str[i] not in spaces:
                i+=1

            words.append(str[word_start:i])
        i+=1
    return ' '.join(reversed(words))

b=sentenceReversal2("  Hi John,   are you ready to go?  ")
print(b)
