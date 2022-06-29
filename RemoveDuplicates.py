# Remove Duplicates from a List
# Description
# Build a function RmDuplicate which remove all the duplicates from a list.

# Examples
# RmDuplicate([3, 1, 2, 3, 4, 5, 6]) returns [1, 2, 3, 4, 5, 6]
# RmDuplicate([1, 3, 5]) returns [1, 3, 5]

def RmDuplicate(mylist):
    mylist.sort()
    newlist = list()
    
    for i in range(0,len(mylist)):
        if mylist[i] not in newlist:
            newlist.append(mylist[i])

    return newlist
