# Separate Numbers
# Description
# Build a function SepNum which extracts the odd numbers from a given list ands append the odd numbers at the end of the list.

# Examples
# SepNum([1, 2, 3, 4, 5, 6]) returns [2, 4, 6, 1, 3, 5]
# SepNum([1, 3, 5]) returns [1, 3, 5]
# SepNum([2, 4, 6]) returns [2, 4, 6]

def SepNum(mylist):
    newlist1=list()
    newlist2=list()
    for i in range(0,len(mylist)):
        if mylist[i] %2 ==0:
            newlist1.append(mylist[i])
        else:
            newlist2.append(mylist[i])
    return newlist1 + newlist2
