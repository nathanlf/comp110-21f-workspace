"""An exercise in remainders and boolean logic."""

__author__ = "730483098"


# Begin your solution here...
user_num: int = int(input("Enter an int: "))

if (user_num % 2 == 0) and (user_num % 7 == 0):
    print("TAR HEELS")
else:
    if user_num % 2 == 0:
        print("TAR")
    else:
        if user_num % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")