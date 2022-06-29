# C2F
# Description
# Build a function C2F which converts a list of temperatures in degrees from Celsius to Fahrenheit. F=C*1.8+32.

# Examples
# C2F([0, 38]) returns [32.0, 100.4]

def C2F(mylist):
    newlist=list()
    for i in range(0,len(mylist)):
        newlist.append(mylist[i] *1.8 +32)
    return newlist
