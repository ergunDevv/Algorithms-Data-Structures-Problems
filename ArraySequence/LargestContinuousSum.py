# PROBLEM : Given an array of integers (positive and negative) find the largest continuous sum.
# INPUT : large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
# OUTPUT : 29

def large_cont_sum(Arr1):
    if(len(Arr1))==0: return 0
    
    max_sum = current_sum = Arr1[0]

    for num in Arr1[1:]:
        current_sum = max(current_sum+num,num)
        print(current_sum)
        max_sum = max(max_sum,current_sum)

    return max_sum


a = large_cont_sum([1, 2, -1, 3, 4, -1])
print(a)
