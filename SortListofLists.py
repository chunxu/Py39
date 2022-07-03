# Sort List of Lists
# Description
# Build a function SortLL which sorts a list of lists by their last elements.

# Examples
# SortLL([[1, 3, 5], [2, 4], [9, 7], [3]]) returns [[3], [2, 4], [1, 3, 5], [9, 7]]

def SortLL(mylist):
    newlist = list()
    itemlist = list()
    for i in range(0,len(mylist)):
        itemlist.append(mylist[i][-1])
    while len(itemlist)>0:
        min_value = min(itemlist)
        min_index = itemlist.index(min_value)
        newlist.append(mylist[min_index])
        itemlist.pop(min_index)
        mylist.pop(min_index)
    return newlist



    
