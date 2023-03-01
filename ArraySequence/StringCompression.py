# PROBLEM: Given a string in the form 'AAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'
# For this problem, you can falsely "compress" strings of single of double letters.
# For instance, it is okay for 'AAB' to return 'A2B1' even though this technically 
# takes more space. The function should also be case sensetive, so that a string 
# 'AAAaaa' returns 'A3a3'

def stringCompression(stringForComp):
    # Deleting spaces
    stringForComp = stringForComp.replace(" ", "")
    # Creating dictionary for storing letters and how many of times exist in stringForComp
    numberOfLetter={}
    # And for returning creating empty string.
    stringForReturn=""

    for letter in stringForComp:
        # Checking if letter added to numberOfLetter before if it is adding 1 to number of letter 
        # that letter if not equaling to 1
        if numberOfLetter.get(letter):
           numberOfLetter[letter]+=1
        else:
            numberOfLetter[letter]=1

    for (key,value) in numberOfLetter.items():
        # Adding dictionary keys and values to stringForReturn
        stringForReturn+=key
        stringForReturn+=str(value)

    # Returning to stringForReturn
    return stringForReturn

a=stringCompression("AAABBBBcDDDddhB")
print("FIRST SOLUTION : "+a)

# !---------------------------------------------------------------------------!
# Second Solution 
def stringCompression2(stringForComp):
    # Creating r for answer that we will return and for edge case check 
    # creating l that is length of stringForComp
    r=''
    l = len(stringForComp)

    if l == 0 :
        return ""
    
    if l ==1:
        return s+"1"
    
    # Creating count variable for how many times exist in stringForComp for every letter
    cnt=1
    # Index of stringForComp
    i=1

    while i<l:
        # Checking the letter that comes before if they are same adding cnt to 1
        if stringForComp[i] == stringForComp[i-1]:
            cnt+=1
        # If they are not same resetting cnt and adding r to letter set and cnt to r
        else:
            r=r+stringForComp[i-1]+str(cnt)
            cnt=1

        i+=1  
    # Lastly adding last letter array to r
    r=r+stringForComp[i-1]+str(cnt)
    # Returning r
    return r

b=stringCompression2("AAABBCCDDDDD")
print("SECOND SOLUTION : "+b)




