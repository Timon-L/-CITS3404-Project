import re
import random

def strtobool(boolstr):
    assert isinstance(boolstr, str), "input must be a string!"
    assert boolstr.lower() == "false" or boolstr.lower() == "true", f"Must be true or false but had {boolstr}!"
    return True if boolstr.lower() == "true" else False # since we checked whether boolstr is true or false only

# checks for a good password
def goodpassword(password):
    assert isinstance(password, str), "password must be a string!"
    a = False # lowercase letter
    A = False # uppercase letter
    num = False # number
    sp = False # special character (!@#$%^&*())
    for i in password:
        a = True if re.search("^[a-z]$", i) != None else a
        A = True if re.search("^[A-Z]$", i) != None else A
        num = True if re.search("^[0-9]$", i) != None else num
        sp = True if re.search("^[!@#$%^&*()]$", i) != None else sp
    return a and A and num and sp

# generates random number for the next card issued
# returns 2-tuple:
# (randomnumber, divisibility of random number by user's given number)
def generaterandomnumber(digit, max=9):
    randomnumber = random.randrange(2, max + 1) # since max is exclusive
    return (randomnumber, (digit%randomnumber == 0))

# generates a valid digit to play the game
def generatedigit(min = 100000000000, max = 900000000000):
    return random.randrange(min, max + 1)