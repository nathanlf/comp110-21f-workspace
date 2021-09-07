"""Repeating a beat in a loop."""

__author__ = "730483098"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
repeats: int = int(input("How many times do you want to repeat it? "))

i: int = 0
beat_string: str = ""

if(repeats > 0):
    while(i < repeats):
        beat_string = beat_string + beat

        if(i < repeats - 1):
            beat_string = beat_string + " "
        
        i = i + 1

    print(beat_string)  # Prints the final beat string all in one print line
else:
    print("No beat...")