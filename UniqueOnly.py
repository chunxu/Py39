# Unique Only
# Description
# Build a function UniqueOnly to detect whether a string only contains unique characters.

# Examples
# UniqueOnly("techlent") returns False
# UniqueOnly("abcde") returns True

def UniqueOnly(s):
    i = 0
    mylist = []
    value=True
    while i<len(s):
        if s[i] not in mylist:
            mylist.append(s[i])
            i +=1
        else:
            value = False
            break
    return value
