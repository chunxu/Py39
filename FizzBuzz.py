# FizzBuzz
# Description
# Build a function FizzBuzz which takes a positive integer as input. If the number is divisible by 3, the function returns "Fizz". If the number is divisible by 5, the function returns "Buzz". If the number is divisible by both 3 and 5, the function returns "FizzBuzz". Otherwise, the function returns the number itself.

# Examples
# FizzBuzz(45) returns "FizzBuzz"
# FizzBuzz(9) returns "Fizz"
# FizzBuzz(25) returns "Buzz"
# FizzBuzz(17) returns "17"

def FizzBuzz(n):
    if n % 15 ==0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 ==0:
        return "Buzz"
    else:
        return n
