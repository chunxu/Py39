# Sort a List
# Description
# Build a function SortLst which sorts a list. At this time you can just use the built-in function in Python.

# Examples
# SortLst([4, 2, 1, 3, 4, 5]) returns [1, 2, 3, 4, 4, 5]
# SortLst([1, 3, 5]) returns [1, 3, 5]

def SortLst(mylist):
    newlist = list()
    while len(mylist)>0:
        newitem = min(mylist)
        newindex = mylist.index(newitem)
        newlist.append(newitem)
        mylist.pop(newindex)
    return newlist
