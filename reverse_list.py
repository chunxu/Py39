# Reverse List
# Description
# Build a function RevLst which reverses a list.

# Examples
# RevLst([3, 1, 9, 8, 4]) returns [4, 8, 9, 1, 3]

def RevLst(mylist):
    newlist=list()
    while len(mylist)>0:
        newlist.append(mylist.pop())
    return newlist
