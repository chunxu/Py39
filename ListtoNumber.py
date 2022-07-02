# List to Number
# Description
# Build a function Lst2Num which convert a number list into one number.

# Examples
# Lst2Num([1, 3, 5]) returns 135
# Lst2Num([0, 1, 2, 0, 3]) returns 1203

def Lst2Num(mylist):
    p = len(mylist)
    num=0
    i=0
    while i<len(mylist):
        num = num+ mylist[i]*10**(p-1)
        i = i + 1
        p = p - 1
    return num
