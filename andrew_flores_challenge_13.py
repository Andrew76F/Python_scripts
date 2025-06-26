import re

def regex_pass(password):
    if re.search(r'[a-z]', password) and len(password) >= 8 and re.search(r'[A-Z]', password) and re.search(r'[0-9]', password) and re.search(r'[@#$%*!]', password):
        return True
    return False
'''
Forgive me for the unholy search, I couldn't figure out how to require uppers, lowers, nums, and symbols AND have it be 8 characters or longer in one search
When I shoved everything in one search, it would push True even if it was 8 lowercases.
When I seperated everything into one search, but different brackets it only was valid if it was in the exact order of the search ex: letters first, 
validating length in the search was also thrown out the window with this method.
'''
password = input("Input password: ")
if regex_pass(password) == True:
    print("Password is valid.")
elif regex_pass(password) == False:
    print("Password is not valid.")
else:
    print("Error")