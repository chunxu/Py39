# Description
# Build a function CapLett to capitalize the first letter of each word in a sentence.

# Examples
# CapLett("we are all friends") returns "We Are All Friends"

def CapLett(mysen):
    mylist = mysen.split()
    mystring = ""
    for i in range(0,len(mylist)):
        mylist[i] = mylist[i].capitalize() 
    for i in range(0,len(mylist)):
        mystring += (mylist[i]+" ") # not join
    return mystring[:-1] # remove last space
