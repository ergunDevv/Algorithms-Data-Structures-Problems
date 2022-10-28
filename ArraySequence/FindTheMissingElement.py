def FindTheMissingElement(Arr1,Arr2):
    # Defining sum of Elements variable
    sumOfElements=0
    # First adding every number to sumOfElements
    for number in Arr1:
        sumOfElements+=number;
    # Then subtracting every number in sumOfElements
    for number in Arr2:
        sumOfElements-=number
    # And returning the value of sumOfElements. Cause after adding and subtracting there will be 
    # just one number that missing. 
    return  sumOfElements
a=FindTheMissingElement([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])
print(a)