# OddNums
# Description
# Build a function OddNums which takes two integers (i and j) as inputs and returns a list of ODD numbers between i and j inclusively.

# Examples
# OddNums(1, 5) returns [1, 3, 5]
# OddNums(2, 6) returns [3, 5]
# OddNums(1, 2) returns [1]

def OddNums(i,j):
    mylist = list()
    for m in range(i,j+1):
        if m % 2 ==1:
            mylist.append(m)
    return mylist
