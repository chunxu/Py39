# Remove Punctuations
# Description
# Build a function RmPunct to remove punctuations from a string.

# Examples
# RmPunct("He said, that is great!!") returns "He said that is great"


def RmPunct(mysen):
    newsen=""
    for i in mysen:
        if i !="," and i!="!" and i!="." and i!="?":
            newsen+=i
    return newsen
  
