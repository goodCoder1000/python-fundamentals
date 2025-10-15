import random
import math
import time

# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

print()
print("--- Conditionals in Python ---")
# Boolean refresher:
print( 3 == 2 )
print("Hello" == "Hi there")
print( 7 != 4)
print(4 > 5)

print()
print()
print()
print()

# if
num1 = 10 
if num1 == 10: 
    print("Your number is equal to 10")

num2 = 5
print(num2 <= 12)
if num2 <= 12:
    print("Your number is less than or equal to 12")

temperature = random.randint(-30, 150)

if (temperature <= -15):
    print("Today the temp is Freezing: ", temperature)
elif (temperature <= 0):
    print("Today the temp is Very Very Cold: ", temperature)
elif (temperature <= 30):
    print("Today the temp is Very Cold: ", temperature)
elif (temperature <= 50):
    print("Today the temp is Cold: ", temperature)
elif (temperature <= 75):
    print("Today the temp is Warm: ", temperature)
elif (temperature <= 100):
    print("Today the temp is Hot: ", temperature)
elif (temperature <= 115):
    print("Today the temp is Very Hot: ", temperature)
elif (temperature <= 130):
    print("Today the temp is Boiling: ", temperature)
else:
    print("you are finished bhaiyaa: ", temperature)

print()
print("--- Comparing Values with if/elif/else ---")

x = 20
y = 20

if x == y: 
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y: 
    print("x is less than y")
else: 
    print("error")


# Logical operator: and
# Both sides of the 'and' must  be true, otherwise it's false. 
print()
print()
print()

age = 17
has_permission = True

if age >= 17 and has_permission:
    print("You can drive")
else:
    print("Can't drive yet")

# Using 'or' and 'not'
print("--- Using 'or' --- ")

day = "Saturday"

if day is "Saturday" or  day is "Sunday":
    print("It's the weekend!")
elif day is "Monday" or day is "Tuesday" or "Wednesday":
    print("It's Monday or Tuesday")
else:
    print("It's Wed,Thur, or Fri")

if day is not "Monday":
    print("It's not Monday")

# Challenges
print("\n--- Challenges ---\n")

# Challenge 1
num = int(input("please give number hehe: "))
if num % 2 == 0: print(f"{num} is even.\n")
else: print(f"{num} is odd.\n")

# one liner hehe haha
# print(f"{(num := int(input('please give number hehe: ')))} is {'even' if num % 2 == 0 else 'odd'}.\n")


# Challenge 2
password = 1234
if input("enter pass: ") == str(password): print("access granted")
else: print("wrong imagine")

# Challenge 3
grade = random.randint(0, 101)
if (grade < 60): print("you got F: ", grade)
elif (grade < 70): print("you got D: ", grade)
elif (grade < 80): print("you got C: ", grade)
elif (grade < 90): print("you got B: ", grade)
elif (grade <= 100): print("you got A: ", grade)
elif (grade <= 101): print("good boy: ", grade)