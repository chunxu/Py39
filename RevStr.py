# Reverse String
# Description
# Build a function RevStr to reverse a string.

# Examples
# RevStr("abcd") returns "dcba"

def RevStr(mystring):
    mylist=list(mystring)
    newlist=list()
    for i in range(0,len(mylist)):
        newlist.append(mylist.pop())
    newstring=""
    newstring = newstring.join(newlist)
    return newstring
