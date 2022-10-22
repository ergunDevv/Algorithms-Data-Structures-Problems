# PROBLEM : Given an array of integers (positive and negative) find the largest continuous sum.
# INPUT : large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
# OUTPUT : 29

def large_cont_sum(Arr1):
    # Edge case check
    if(len(Arr1))==0: return 0
    # Creating 2 variables for algorithm
    max_sum = current_sum = Arr1[0]

    for num in Arr1[1:]:
        # Down below checking is current_sum+num higher than num and 
        # assign the higher one to current_sum
        current_sum = max(current_sum+num,num)
        # Then checking again is current_sum is higher than max_sum if it is 
        # assigning current_sum value to the max_sum 
        max_sum = max(max_sum,current_sum)
    # Return the max_sum
    return max_sum


a = large_cont_sum([1, 2, -1, 3, 4, -1])
print(a)
