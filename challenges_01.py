import random
import math
import time

# Challenge 1
word = input("give word: ")
if(word[::-1] == word): print("True")
else: print("False")

# Challenge 2
email = input("put email: ")
parts_of_email = email.split("@") # we didn't learn this but its soo much easier like this
print(parts_of_email[1])

# Challenge 3
alist = ["a", "b", "c"]
if (input("what is the last thing in the list: ")) == alist[-1]: print("True")
else: print("False")

# Challenge 4
aword = input("give word (again): ")
if len(aword) < 3: print(aword)
elif (aword[-3:] != "ing"): print(aword + "ing")
else: print(aword + "ly")