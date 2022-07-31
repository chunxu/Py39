# Character Frequency
# Description
# Build a function ChaFreq to calculate the frequencies of characters in a string. Store the results in a dictionary.

# Examples
# ChaFreq("techlent") returns {"c": 1, "e": 2, "h": 1, "l": 1, "n": 1, "t": 2}

def ChaFreq(s):
    cha_list=[]
    #fre_list=[]
    mydic = {}
    for char in s:
        if char not in cha_list:
            cha_list.append(char)
            mydic[char] = 1
        else:
            mydic[char] +=1
    return mydic
