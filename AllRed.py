#
# Description
# Build a function AllRed that takes a list of strings as input, returns a boolean indicating whether all the strings containing word "red".

# Examples
# AllRed(["red hat", "a pair of red shoes", "three red apples"]) returns True
# AllRed(["red hat", "white shirt", "black eyes"]) returns False
# AllRed([]) returns False

def AllRed(stringlist):
    if len(stringlist) == 0:
        return False
    else:
        i=0
        while i<len(stringlist):
            if "red" in stringlist[i].split():
                i+=1
            else:
                return False
                break
        if i==len(stringlist):
            return True
        
    
