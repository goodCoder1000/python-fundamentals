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
    type_out("*snickers evilly*", delay=0.03)
    time.sleep(2)
    type_out("I shall be your first opponent.", delay=0.075)
    time.sleep(2)
    type_out("Don't make this too difficult...               \n actually I doubt you'll be able to.", delay=0.05)
    time.sleep(2)
    type_out("I give you the opportunity to go first... ", delay=0.075)
    time.sleep(2)
    load = random.randint(1, 6)
    revolver = [0, 0, 0, 0, 0, 0]
    for i in range(5):
        if (i == load):
            revolver[i] == 1
        else:
            revolver[i] == 0

    num = 0
    while revolver[num] == 0:
        type_out("*your hands tremble as you pick up the gun*", delay=0.02)
        time.sleep(1.5)
        type_out("*you slowly point it towards yourself and pull the trigger*", delay=0.015)
        time.sleep(2)
        type_out("Blank...", delay=0.5)
        time.sleep(2)
        i = i + 1
        type_out("Ah, yes, time for my turn.", delay=0.05)
        time.sleep(1)
        type_out("*swiftly spins the revolver around shoots*", delay=0.03)
        time.sleep(1)
        if (revolver[i] == 1):
            type_out("*BANG*", delay=0.01)
            time.sleep(2)
            type_out("*your breathing is heavy as you walk out*", delay=0.03)
            time.sleep(2)
            type_out("You survived... this time...", delay=0.05)
            

        
        

    
    
    
    

    

# revolver w/ 6 chambers
# 1 chamber has a real bullet; rest don't
# each person takes turns
# you can choose to either aim at yourself or aim at your opponent
# you can also choose to 
# YOU CAN USE random.shuffle() TO SHUFFLE WHICH ONE THE LOADED ROUND IS AHHH
