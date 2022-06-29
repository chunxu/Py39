# Remove an Element
# Description
# Build a function RmEl to remove a target element from a list. If the target element appears in the list for multiple times, only remove the first one.

# Examples
# RmEl([1, 2, 3, 4, 5], 2) returns [1, 3, 4, 5]
# RmEl([1, 2, 3, 4, 5], 6) returns [1, 2, 3, 4, 5]
# RmEl([1, 2, 3, 3, 4, 5], 3) returns [1, 2, 3, 4, 5]

def RmEl(mylist, n):
    if n not in mylist:
        return mylist
    else:
        for i in range(0, len(mylist)):
            if mylist[i] == n:
                mylist.pop(i)
                break
        return mylist
