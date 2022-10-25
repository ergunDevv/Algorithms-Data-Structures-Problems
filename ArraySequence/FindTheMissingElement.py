# PROBLEM : Consider an array of non-negative integers. A second array is formed by shuffling the 
# elements of the first array and deleting a random element. Given these two arrays, find which
# element is missing in the second array. 
# Input: FindTheMissingElement([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])
# Output: 5 is the missing number.

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
print("FindTheMissingElement : "+str(a) +" is the missing number")

# !-----------------------------------------------------------------------------!
# Second Solution

def FindTheMissingElement2(Arr1,Arr2):
    # Sorting the both array.
    Arr1.sort()
    Arr2.sort()
    # Looping over Arr1 and Arr2 but zip version.
    # Because of sorted both array if their values are not same it is the missing number
    # If not return anything Arr1's last character that missing. 
    for num1,num2 in zip(Arr1,Arr2):
        if num1!=num2 :
            return num1
    return num1[-1]
 
b=FindTheMissingElement2([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])
print("FindTheMissingElement2 : "+str(b) +" is the missing number")

