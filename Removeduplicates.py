# Remove duplicates from a sorted list
# Description
# Build a function SortRm which removes duplicate numbers in a sorted list.

# Examples
# SortRm([1, 2, 2, 3, 4, 4, 5, 6]) returns [1, 2, 3, 4, 5, 6]
# SortRm([1, 2, 3, 4, 5, 6]) returns [1, 2, 3, 4, 5, 6]

def SortRm(mylist):
    newlist=list()
    for i in mylist:
        if i not in newlist:
            newlist.append(i)
    return newlist
