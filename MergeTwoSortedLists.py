# Merge Two Sorted Lists
# Description
# Build a function MergeSorted which merges two sorted lists as one sorted list.

# Examples
# MergeSorted([1, 3, 5], [2, 4, 6]) returns [1, 2, 3, 4, 5, 6]
# MergeSorted([1, 2, 3], [4, 5, 6]) returns [1, 2, 3, 4, 5, 6]

def MergeSorted(list1, list2):
    newlist = (list1 + list2)
    newlist.sort()
    return newlist
