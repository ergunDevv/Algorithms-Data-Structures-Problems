# PROBLEM: Given a string of words, reverse all the words. For Example:
# Given: 'This is the best'
# Return : 'best the is This'

def sentenceReversal(str):
    str=str.strip().split()
    reversedString=""
    for word in reversed(str):
        reversedString+=word
        reversedString+=" "

    return reversedString


a=sentenceReversal("  Hi John,   are you ready to go?  ")
print(a)
