# Square Root
# Description
# Build a function sqrt to calculate the square root of a positive integer number. If the result is not a integer, the function returns the nearest integer to the left of the result number.

# Examples
# sqrt(16) returns 4
# sqrt(17) returns 4
# sqrt(77) returns 8
# sqrt(1) returns 1

def sqrt(n):
    i =1
    while i <= (n//2+1):
        if i**2 < n:
            i= i+1
            continue
        elif i**2 == n:
            return i
            break
        else:
            return i-1
            break


