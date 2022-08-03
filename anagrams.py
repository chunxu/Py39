# Anagrams
# Description
# Build a function anagrams to determine whether two given strings are anagrams.

# Examples
# anagrams("abc", "cba") returns True
# anagrams("ab", "abc") returns False
# anagrams("abccba", "aabbbc") returns False

def anagrams(str1, str2):
    #s1=list(str1)
    #s2=list(str2)
    value=True
    if len(str1) != len(str2):
        value=False
    else:
        i=0
        while i<len(str1):
            if str1[i] != str2[-1-i]:
                value = False
                break 
            else:
                i+=1
        if i == len(str1):
            value = True
    return value
        
