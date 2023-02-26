def pairSum(Arr1,sumOfPair):
    # Created 2 sets in seenElements set adding the number if pair of number(target) not exists in
    # seenElements if exists in seenElements adding the number and target pair to the output element
    # then returning the output elements.
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