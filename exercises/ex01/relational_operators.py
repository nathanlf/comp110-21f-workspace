"""Demonstrates how four relational operators work in Python based on user input."""

__author__ = "730483098"

num1: str = input("Left-hand side: ")
num2: str = input("Right-hand side: ")

less_than: bool = int(num1) < int(num2)
print(num1 + " < " + num2 + " is " + str(less_than))

greater_or_equal: bool = int(num1) >= int(num2)
print(num1 + " >= " + num2 + " is " + str(greater_or_equal))

equal_to: bool = int(num1) == int(num2)
print(num1 + " == " + num2 + " is " + str(equal_to))

not_equal_to: bool = int(num1) != int(num2)
print(num1 + " != " + num2 + " is " + str(not_equal_to))