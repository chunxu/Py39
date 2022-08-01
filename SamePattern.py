# Same Pattern
# Description
# Build a function SamePattern takes two strings as inputs and determines whether they are in the same pattern.

# Examples
# SamePattern("egg", "zoo") returns True
# SamePattern("abb", "ab") returns False
# SamePattern("hello", "agree") returns False
# SamePattern("aaa", "abc") returns False
# SamePattern("abc", "aaa") returns False

def SamePattern(str1, str2):
    s1=list(str1)
    s2=list(str2)
    value=True
    if len(s1) != len(s2):
        value=False
    else:
        i=0
        while i<(len(s1)-1):
            a = ord(s1[i]) - ord(s1[i+1])
            b = ord(s2[i]) - ord(s2[i+1])
            if a==0:
                if b==0:
                    i+=1
                    continue
                else:
                    value=False
                    break
            else:
                if b==0:
                    value=False
                    break
                else:
                    i+=1
                    continue
    return value
