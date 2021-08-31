"""Prints number info messages based on user input."""

__author__ = "730483098"

num1: str = input("Left-hand side: ")
num2: str = input("Right-hand side: ")

exponent: int = int(num1) ** int(num2)
print(num1 + " ** " + num2 + " is " + str(exponent))

division: float = int(num1) / int(num2)
print(num1 + " / " + num2 + " is " + str(division))

integer_division: int = int(num1) // int(num2)
print(num1 + " // " + num2 + " is " + str(integer_division))

modulo: int = int(num1) % int(num2)
print(num1 + " % " + num2 + " is " + str(modulo))