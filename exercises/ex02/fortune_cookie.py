"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730483098"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...
print("Your fortune cookie says...")

random_num: int = randint(1, 4)

if(random_num == 1):
    print("Someone very special will soon come into your life.")
else:
    if(random_num == 2):
        print("A period of self-love and appreciation is near.")
    else:
        if(random_num == 3):
            print("You will find prosperity and peace in your life.")
        else:
            print("An unexpected event will bring you clarity.")

print("Now, go spread positive vibes!")