# class AnagramProblem():
#     def isAnagramString(self,text1,text2):
#         countOfSame=0;
#         print(text1,text2)
#         comparisonText1=text1.replace(' ', '').lower()
#         comparisonText2=text2.replace(' ', '').lower()
#         print(comparisonText1,comparisonText2)
#         if (len(comparisonText1) != len(comparisonText2)): return False
#         countOfText=len(comparisonText1)
#
#         for i in comparisonText1.strip().lower():
#             print(i)
#             for j in comparisonText2.strip().lower():
#                 if (j == i):
#                     print("count increased 1")
#                     countOfSame+=1
#                     break
#
#
#         if countOfSame == countOfText:
#             print("Return true")
#             return True
#         else:
#             print("Return false")
#             return False
#
#
# hey=AnagramProblem()
# hey.isAnagramString("123","1 2")

def isAnagramString(text1,text2):

    text1=text1.replace(" ","").lower()
    text2=text2.replace(" ","").lower()
    if len(text1) != len(text2) :  return False

    count = {}
    for letter in text1:
        if letter in count:
            count[letter]+=1
        else:
            count[letter]=1

    for letter in text2:
        if letter in count:
            count[letter]-=1
        else:
            return False

    # for letter in count:
    #     if count[letter] != 0:
    #         return False

    return True

a = isAnagramString("Neir","Reinn")
print(a)

