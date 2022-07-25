# Palindrome
# Description
# Build a function isPalindrome which takes a string as an input and returns boolin value telling whether the string is a palindrome.

# Examples
# isPalindrome("abcba") returns True
# isPalindrome("abba") returns True
# isPalindrome("a") returns True
# isPalindrome("") returns True
# isPalindrome("abcd") returns False

def isPalindrome(s):
    i=0
    result=1
    if len(s) ==0 or len(s)==1:
        result=1
    else:
        while i<len(s)//2:
            if s[i] == s[-1-i]:
                i+=1
                
            else:
                result=0
                break
    return result
