# Maximum Stock Gain
# Description
# Build a function MaxGain to find the maximum you can gain by buying and selling stocks. The strock prices represented as a list of numbers. You need to buy stocks before you sell them.

# Examples
# MaxGain([3, 4, 1, 5, 7, 2]) returns 6 --Explanation: Buy stocks when the price is 1 and sell them when the price is 7.
# MaxGain([5, 4, 3, 2, 1]) returns 0

def MaxGain(mylist):
    maxgain = 0
    for i in range(0, len(mylist)):
        j=i
        while j<len(mylist):
            if mylist[j] - mylist[i] > maxgain:
                maxgain = mylist[j] - mylist[i]
            j = j + 1
    return maxgain
