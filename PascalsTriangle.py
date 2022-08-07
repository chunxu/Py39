# Pascals Triangle
# Description
# Build a function PascalsT which takes an integer n as an input and generate a n layer Pascals Triangle.

# Examples
# PascalsT(3) returns [[1], [1, 1], [1, 2, 1]]
# PascalsT(5) returns [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# def PascalsT(n):
#     mylist = list()
#     if n < 1:
#         return "error"
#     elif n ==1:
#         return [[1]]
#     else:
#         mylist.append([1])
#         mylist.append([1,1])   
#         i = 2
#         while i < n:
#             j = len(mylist)
#             while j<n:
#                 new_item=list()
#                 new_item.append(1)
#                 for x in range(0,j-1):
#                     new_item.append(mylist[i-1][x]+mylist[i-1][x+1])
#                 new_item.append(1)
#                 j=j+1
#             mylist.append(new_item)
#             i=i+1
#         return (mylist)       

 #IndexError('list assignment index out of range')           
# not allowed to set list value out of current index

# too many rounds of loops included


#working code below:
def PascalsT(n):
    mylist = list()
    if n < 1:
        return "error"
    elif n ==1:
        return [[1]]
    else:
        mylist.append([1])
        mylist.append([1,1])   
        i = 2
        while i < n:
            new_item=list()
            new_item.append(1)
            for x in range(0,i-1):
                new_item.append(mylist[i-1][x]+mylist[i-1][x+1])
            new_item.append(1)
            mylist.append(new_item)
            i=i+1
        return (mylist)       
