# Description
# Build a function RevSen to reverse a sentence.

# Examples
# RevSen("we are all friends") returns "friends all are we”

def RevSen(mysentence):
    setencelist=mysentence.split()
    newlist=list()
    while len(setencelist)>0:
        newlist.append(setencelist.pop())
    return " ".join(newlist)

