# Target Sum
# Description
# Build a function TargetSum which takes a list and a target number as inputs. If there are two numbers in the list whose sum equals to the target number, the function returns the indice of the two numbers in list, otherwise returns -1.

# Examples
# TargetSum([1, 2, 5, 9, 8, 11], 6) returns [0, 2] (1+5=6)
# TargetSum([1, 2, 5, 9, 8, 11], 11) returns [1, 3]
# TargetSum([1, 2, 5, 9, 8, 11], 5) returns -1
# TargetSum([1, 2, 5, 9, 8, 11], 14) returns [2, 3]

def TargetSum(mylist, target):
    i = 0
    while i<len(mylist):
        j=i+1
        while j<len(mylist):
            if mylist[i]+mylist[j] == target:
                return [i,j]
                break
            else:
                j +=1
                continue
        if j==len(mylist):
            i =+1
            continue
        else:
            break
    if i == len(mylist):
        return -1
      
      
  #System is busy. Please try later. Maybe due to infinite loop.
