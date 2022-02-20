"""
CSTWPY 
Python for Beginners 

=== MODULE DESCRIPTION === 
This module contains all the code for tutorial 1.

Copyright (C) 2022 therealgg13.
"""


sample_string = "breadgoesbrrr" # string 
sample_float = 0.03 # float 
sample_int = 90 # integer 
sample_boolean = True # boolean (True, False)
sample_list = ["Hello Toki Club", "Hello MsKitty"]
# ... many others

# declaring variables 
x = [i for i in range(4)]
y = x + [1]


y = "2"
y = (2,3, 4)


def bar(x: str) -> str: 
    return x + "rgrg"

# reassign variables 
x = 6 + 3 

# referencing an non-existing variable 

# What do you think would return?

# adding 
x = 4 + 3



NAME = 'therealgg13'
AGE = 21
isMajority = AGE > 18
friends = []

def addFriend(friend: str) -> None: 
    friends.append(friend)


def formatNice() -> str: 
    return f'{NAME} {AGE}'


addFriend("Mskitty")