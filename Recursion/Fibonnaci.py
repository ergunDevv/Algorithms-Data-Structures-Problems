

def FibonnaciRecursive(n):
    if n == 1 or n ==0:
        return n
    else: 
        
        return FibonnaciRecursive(n-1) + FibonnaciRecursive(n-2)
    
print(FibonnaciRecursive(10))

# Iteration solution
def FibonnaciIteration(n):

    a,b = 0,1

    for i in range(n):
        a,b=b,a+b
    return a



print(FibonnaciIteration(10))


