# N Grams
# Description
# Build a function NGram which takes a string s and an integer n as inputs, returns a list of n grams of s.

# Examples
# NGram("techlent", 2) returns ["te", "ec", "ch", "hl", "le", "en", "nt"]
# NGram("abc", 3) returns ["abc"]
# NGram("abc", 4) returns [   ]
# NGram("abc", 1) returns ["a", "b", "c"]

def NGram(s,n):
    charlist=list(s)
    newlist=[]
    if n>len(charlist):
        return newlist
    else:
        for i in range(0,len(charlist)-n+1):
            newstring=""
            for j in range(i,n+i):#move index to the start of str
                newstring+=charlist[j]
            newlist.append(newstring)
        return newlist
    
