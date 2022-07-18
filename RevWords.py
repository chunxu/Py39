# Description
# Build a function RevWords to reverse each word of a sentence.

# Examples
# RevWords("we are all friends") returns "ew era lla sdneirf"

def RevWords(mysen):
    mylist = mysen.split()
    newstr =[]
    for i in range (0, len(mylist)):
        mystr = list(mylist[i])
        newword=""
        while(len(mystr)>0):
            newstr.append(mystr.pop())
        newstr.append(' ')
    newstr.pop() #remove the last space
    return "".join(newstr)
