import random
import time
import math

def type_out(text, delay=0.3):
    typed = ""
    for char in text:
        typed += char
        print("\n\n\n\n\n\n", typed)
        time.sleep(delay)
print("\n")
type_out("Welcome to Russian Roulette...", delay=0.075)
time.sleep(2)
type_out("This is a game of life and death...", delay=0.075)
time.sleep(2)
play_or_no = input(print("Are you sure you want to play? (Y/N): "))
if (play_or_no == "Y"):
    type_out("Good...", delay=0.3)
    time.sleep(1.5)
    type_out("*snickers evilly*", delay=0.05)
    time.sleep(2)
    type_out("I shall be your first opponent.", delay=0.075)
    time.sleep(2)
    type_out("Don't make this too difficult...               \n actually I doubt you'll be able to.", delay=0.05)
    
    
    

    

# revolver w/ 6 chambers
# 1 chamber has a real bullet; rest don't
# each person takes turns
# you can choose to either aim at yourself or aim at your opponent
# YOU CAN USE random.shuffle() TO SHUFFLE WHICH ONE THE LOADED ROUND IS AHHH
