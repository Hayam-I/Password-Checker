'''
Created on Mar 26, 2023

@author: hayam

Premise of the program:
Write a program that will validate a user password and check if it meets the password strength requirements
The requirements are:
1) The password length must be at least 10 characters long and at most 20 characters
2) The password must have at least one digit
3) The password must contain at least one upper-case letter (A-Z)
4) The password must have at least one lower-case letter (a-z)
5) The password must have at least one special character (!@#$%^&*?)
6) The password must not contain a white space character
'''
'''
input: password (String)

output:
> password does not meet all requirement:
    display: your password must have [missing] requirement(s).
> password matches all the requirements:
    display: password created successively.
'''
'''
Sample run:

Choose a password for your account: abc123
Your password has not met the following requirement(s):
    - The password length must be at least 10 characters long and at most 20 characters
    - The password must contain at least one upper-case letter (A-Z)
    - The password must have at least one special character (!@#$%^&*?)

Choose a password for your account: ABCabc@123
Password created successively
'''
'''
further instructions:
    > create a GUI application that applies this premise.
'''
'''
Thought process:

Python re-module => bool(re.search(pattern,string))

If pattern is in the string, return the position of pattern in string, otherwise, return none

def check_digit(pwd: str) -> bool:
    return bool(re.search(r'[0-9]',pwd))
    
def check_length(pwd)
    return 10<=len(pwd)<=20
could also be written as:
def check_length(pwd)
    return True if 10<=len(pwd)<=20 else False

patterns:
> pattern = r'[0-9]' ->digits
> pattern = r'[a-z]' -> lowercase
> pattern = r'[A-Z]' -> capital
> pattern = r'[!@#$%^&*?]' -> special charcters
> pattern = r'\s' -> white spaces

and each condition should have a function so that we know exactly which condition is not met (returns False)
'''