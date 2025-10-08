import random
import time
import math

def type_out(text, delay=0.3):
    typed = ""
    for char in text:
        typed += char
        print("\n\n\n\n\n\n\n", typed)
        time.sleep(delay)
print("\n")

load = random.randint(0, 5)
revolver = [0, 0, 0, 0, 0, 0]
for i in range(6): # post finish message: i forgot about random.shuffle oops
    if (i == load):
        revolver[i] = 1
    else:
        revolver[i] = 0
print(revolver) # for testing purposes
time.sleep(2)

type_out("Welcome to Russian Roulette...", delay=0.075)
time.sleep(2)
type_out("This is a game of life and death...", delay=0.075)
time.sleep(2)
play_or_no = input("Are you sure you want to play? (Y/N): ")
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

    num = 0
    if (revolver[num] == 1):
        type_out("*your hands tremble as you pick up the gun*", delay=0.02)
        time.sleep(1.5)
        type_out("*you shake the gun and hear the bullet in the first container... you know you'll die right now*", delay=0.012)
        time.sleep(2.5)
        type_out("*you spin around the gun as fast as you can and shoot your opponent*", delay=0.02)
        time.sleep(2)
        type_out("*YOU SPRINT OUT OF THE ROOM AND CALL FOR HELP WHILE HE STARTS TO RUN BEHIND YOU*", delay=0.02)
        time.sleep(2)
        type_out("*HE SHOOTS* *BANG*", delay=0.1)
        time.sleep(1.5)
        type_out("All you see is black... forever...", delay=0.067)

        # end
        time.sleep(3)
        type_out("Fin", delay=1)
        time.sleep(3)
        type_out("THE GAME ENDED! RESTART USING PLAY BUTTON AT THE TOP RIGHT", delay=0.02)
        time.sleep(10000)
    
    while revolver[num] == 0:
        type_out("*your hands tremble as you pick up the gun*", delay=0.02)
        time.sleep(1.5)
        type_out("*you slowly point it towards yourself and pull the trigger*", delay=0.015)
        time.sleep(2)
        type_out("Blank...", delay=0.5)
        time.sleep(2)
        num = num + 1
        type_out("Ah, yes, time for my turn.", delay=0.05)
        time.sleep(1)
        type_out("*swiftly spins the revolver*", delay=0.03)
        time.sleep(1)
        if (revolver[num] == 1):
            if (num == 5):
                type_out("Wait... This is the last turn... I'm guaranteed death.", delay=0.03)
                time.sleep(2)
                type_out("OR AM I?!", delay=0.02)
                time.sleep(1.5)
                type_out("*turns the gun around and fires... AT YOU*", delay=0.02)
                time.sleep(2)
                type_out("*you hear him walk over to you and watch as you DIE...*", delay=0.015)
                time.sleep(2)
                type_out("THE HOUSE ALWAYS WINS >:)", delay=0.04)
                
                # end
                time.sleep(3)
                type_out("Fin", delay=1)
                time.sleep(3)
                type_out("THE GAME ENDED! RESTART USING PLAY BUTTON AT THE TOP RIGHT", delay=0.02)
                time.sleep(10000)

            type_out("*he shoots*", delay=0.05)
            time.sleep(1.5)
            type_out("*BANG*", delay=0.01)
            time.sleep(2)
            type_out("*you get up and see him lying on the floor*", delay=0.02)
            time.sleep(2)
            type_out("*your breathing is heavy as you walk out*", delay=0.03)
            time.sleep(2)
            type_out("*you hear him say* 'You survived... this time...'", delay=0.05)
            
            # end
            time.sleep(3)
            type_out("Fin", delay=1)
            time.sleep(3)
            type_out("THE GAME ENDED! RESTART USING PLAY BUTTON AT THE TOP RIGHT", delay=0.02)
            time.sleep(10000)

        else:
            type_out("*he shoots*", delay=0.05)
            time.sleep(1.5)
            type_out("*click*", delay=0.05)
            time.sleep(1)
            type_out("*laughs maniacally* Your turn again... >:)", delay=0.03)
            time.sleep(2)
            type_out("*hands the gun over*", delay=0.04)
            time.sleep(1.5)
            num = num + 1

    type_out("*your hands tremble as you pick up the gun*", delay=0.02)
    time.sleep(1.5)
    type_out("*you slowly point it towards yourself and pull the trigger*", delay=0.015)
    time.sleep(2)
    type_out("*BANG*", delay=0.01)
    time.sleep(2)
    type_out("*you hear him walk over to you and watch as you DIE...*", delay=0.02)

    # end
    time.sleep(3)
    type_out("Fin", delay=1)
    time.sleep(3)
    type_out("THE GAME ENDED! RESTART USING PLAY BUTTON AT THE TOP RIGHT", delay=0.02)
    time.sleep(10000)

elif (play_or_no == "N"):
    type_out("*the door locks behind you*", delay=0.03)
    time.sleep(1.5)
    type_out("You had no choice to begin with...", delay=0.02)
    time.sleep(1.5)
    type_out("im too lazy to code this dialogue just restart plz", delay=0.02)

elif (play_or_no != "Y" and play_or_no != "N"):
    type_out("INVALID", delay=0.02)

        
            

        
        

    
    
    
    

    

# revolver w/ 6 chambers
# 1 chamber has a real bullet; rest don't
# each person takes turns
# you can choose to either aim at yourself or aim at your opponent
# you can also choose to 
# YOU CAN USE random.shuffle() TO SHUFFLE WHICH ONE THE LOADED ROUND IS AHHH
