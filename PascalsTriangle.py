# Pascals Triangle
# Description
# Build a function PascalsT which takes an integer n as an input and generate a n layer Pascals Triangle.

# Examples
# PascalsT(3) returns [[1], [1, 1], [1, 2, 1]]
# PascalsT(5) returns [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

def PascalsT(n):
    mylist = list()
    if n < 1:
        return "error"
    elif n ==1:
        return [[1]]
    else:
        mylist[0] = [1]
        mylist[1] = [1,1]
        i = 2
        while i < n:
            mylist[i][0] = mylist[i][-1] = 1
            j = 1
            while j <= n/2:
                mylist[i][j] = mylist[i][-j-1] = mylist[i-1][j-1] + mylist[i-1][j]
                j = j + 1
            i = i + 1
    return mylist    

 #IndexError('list assignment index out of range')           
