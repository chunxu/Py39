# Letter Palindrome
# Description
# Build a function LettPalind to determine a string is a palindrome or not. We only consider letters this time.

# Examples
# LettPalind("909@,.") returns True
# LettPalind("He is Sieh!") returns True
# LettPalind("His name is Sieh.") returns False

def LettPalind(s):
    mystring ="".join(ch for ch in s if ch.isalnum())
    
    i=0
    j=True
    while i<len(mystring)//2:
        if mystring[i].lower() == mystring[-1-i].lower():
            i+=1
            continue
        else:
            j=False
            break
    return j

