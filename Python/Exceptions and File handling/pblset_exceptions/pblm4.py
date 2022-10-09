#Write a program that randomly generates a number. 
# Raise a  user-defined exception 
# if the number is below 0.1.
class Error(Exception):
    pass
class NotApplicableError(Error):
    """When the value is below 0.1"""
    pass


import random
try:
    n = random.random()
    #n = 0.003
    if n < 0.1 :
        raise NotApplicableError
    else :
        print(n)

except NotApplicableError:
    print("The number is below 0.1")

