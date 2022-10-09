#.Write a program that validates name and age 
# as entered by the  user 
# to determine whether the person can vote or not. 

class Error(Exception):
    pass
class NoVoteError(Error):
    """When the value is below 18"""
    pass



try:
    name = input("Enter your name :")
    age = int(input("Enter your age :"))
    if age < 18 :
        raise NoVoteError
    else :
        print("The user {} can vote !".format(name))

except NoVoteError:
    print("The user {} cannot vote".format(name))