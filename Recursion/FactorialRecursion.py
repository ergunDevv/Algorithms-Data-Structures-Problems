def Factorial(num):

    if(num==0):
        return 1
    else:
        return num * Factorial(num-1)
    
print(Factorial(5))

# Factorial but adding numbers
def rec_sum(num):
    if(num==0):
        return 0
    else:
        return num + rec_sum(num-1)
    
print(rec_sum(4))

def sum_func(num):

    if num/10 <=0:
        return 0
    
    else:
        return num%10 + sum_func((num-num%10)/10)

print(sum_func(654321))
print(432%10)

# word_split function returns if we can create phrase with list_of_words 
def word_split(phrase,list_of_words,output=None):
    
    if output ==None:
        output=[]

    for word in list_of_words:
        if phrase.startswith(word):
            
            output.append(word)

            return word_split(phrase[len(word):],list_of_words,output)
    return output


print(word_split("themanruns",["the","mans","runs"]))

