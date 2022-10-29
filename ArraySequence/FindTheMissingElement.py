def FindTheMissingElement(Arr1,Arr2):
    sumOfElements=0
    for number in Arr1:
        sumOfElements+=number
    for number in Arr2:
        sumOfElements-=number

    return  sumOfElements
a=FindTheMissingElement([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])
print(a)