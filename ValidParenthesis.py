# Valid Parenthesis
# Description
# Build a function ValidParenthesis to determine the parenthesis in a string are valid.

# Examples
# ValidParenthesis("((()))()") returns True
# ValidParenthesis("()()()") returns True
# ValidParenthesis("()()()(") returns False
# ValidParenthesis("((())))") returns False

def ValidParenthesis(s):
    if len(s)%2!=0:
        return False
    else:
        if s.count('(') == s.count(')'):
            return True
        else:
            return False
