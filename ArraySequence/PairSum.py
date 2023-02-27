def pairSum(Arr1,sumOfPair):

    seenElements = set()
    outputElements= set()
    if len(Arr1)<2 : return
    for number in Arr1:
        target = sumOfPair-number
        if target not in seenElements:
            seenElements.add(number)
        else:
            outputElements.add(((min(number,target)),max(number,target)))
    return outputElements

A=pairSum([1,2,2,3,3,4,5],6)
print(A)