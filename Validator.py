'''
Created on Mar 26, 2023

@author: hayam
'''

import re

'first condition'
def check_length(pwd: str) -> bool:
    return 10<=len(pwd)<=20

'second condition'
def check_digit(pwd: str) -> bool:
    return bool(re.search(r'[0-9]', pwd))

'third condition'
def check_uppercase(pwd: str) -> bool:
    return bool(re.search(r'[A-Z]', pwd))

'fourth condition'
def check_lowercase(pwd: str) -> bool:
    return bool(re.search(r'[a-z]', pwd))

'fifth condition'
def check_special_character(pwd: str) -> bool:
    return bool(re.search(r'[!@#$%^&*?]', pwd))

'sixth condition'
def check_wSpace(pwd: str) -> bool:
    return bool(re.search(r'\s', pwd))

pwd = input('Choose a password:')

if all([check_digit(pwd),
       check_length(pwd),
       check_lowercase(pwd),
       check_special_character(pwd),
       check_uppercase(pwd),
       not check_wSpace(pwd)]):
    print('Password created successively ')
else:
    print('Your password has not met the following requirement(s): ')
    if not check_length(pwd):
        print('- The password length must be at least 10 characters long and at most 20 characters')
    if not check_digit(pwd):
        print('- The password must have at least one digit')
    if not check_uppercase(pwd):
        print('- The password must contain at least one upper-case letter (A-Z)')
    if not check_lowercase(pwd):
        print('- The password must have at least one lower-case letter (a-z)')
    if not check_special_character(pwd):
        print('- The password must have at least one special character (!@#$%^&*?)')
    if check_wSpace(pwd):
        print('- The password must not contain a white space character')



