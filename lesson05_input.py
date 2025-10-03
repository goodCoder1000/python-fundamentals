import random
import math
import time

print("\n--= User Input Demonstration =--\n")

name = input("Enter your name (or death): ")
print(name)

age = input("Enter your age: ")
print(type(age)) # string

age = int(input("Enter your age: "))
print(type(age)) # int

age_number = int(age)
print("Next year, you will be:", age_number + 1)

# Challenge 1
color = input("What is your fav color: ")
print("Your favorite color is: ", color)

# Challenge 2
num1 = int(input("1 number please: "))
num2 = int(input("another number please: "))
print("The sum is: ", num1 + num2)