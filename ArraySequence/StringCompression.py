# PROBLEM: Given a string in the form 'AAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'
# For this problem, you can falsely "compress" strings of single of double letters.
# For instance, it is okay for 'AAB' to return 'A2B1' even though this technically 
# takes more space. The function should also be case sensetive, so that a string 
# 'AAAaaa' returns 'A3a3'

def stringCompression(stringForComp):
    stringForComp = stringForComp.replace(" ", "")
    numberOfLetter={}
    stringForReturn=""
    for letter in stringForComp:
        print(letter)
        if numberOfLetter.get(letter):
           numberOfLetter[letter]+=1
        else:
            numberOfLetter[letter]=1

    for (key,value) in numberOfLetter.items():
        stringForReturn+=key
        stringForReturn+=str(value)


    return stringForReturn

a=stringCompression("AAABBBBcDDDddhB")
print(a)
