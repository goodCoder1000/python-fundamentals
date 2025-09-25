import random
import time

# other starting things
taco = "Hello world"
password = "123456"
randpass = random.randint(1,1000000)
email = "ethan@gmail.com"
print("\nEmail: \t\t" + email + "\nPassword: \t" + str(randpass))

temperature = random.randint(-30, 130)
print(type(temperature))

# for fun
if (temperature <= -15):
    print("Today the temp is Freezing: ", temperature)
if (temperature <= 0 and temperature > -15):
    print("Today the temp is Very Very Cold: ", temperature)
if (temperature <= 30 and temperature > 0):
    print("Today the temp is Very Cold: ", temperature)
if (temperature <= 50 and temperature > 30):
    print("Today the temp is Cold: ", temperature)
if (temperature <= 75 and temperature > 50):
    print("Today the temp is Warm: ", temperature)
if (temperature <= 100 and temperature > 75):
    print("Today the temp is Hot: ", temperature)
if (temperature <= 115 and temperature > 100):
    print("Today the temp is Very Hot: ", temperature)
if (temperature <= 130 and temperature > 115):
    print("Today the temp is Boiling: ", temperature)

# for floats
price = 3.99

# for booleans
enabled = False
is_complete = True
print("Is_complete is:  ", is_complete)
enabled = True
print("Enabled is: ", enabled)

# for math problems
num1 = 6
num2 = 7
print("Answer: " + str(num1 + num2))

# counting (uh oh WHAT IS THAT COUNTDOWN)
count = 11 
for i in range(1, 11):
    countdown = count - i
    print("Warning! Time before immenent death: ", countdown)
    time.sleep(1)
print("*boom noises*")



#------------------------------------------------------------------------------
x = random.randint(1,100)
y = time.time()

for i in range(1,1):
    x = random.randint(1,1000067)
    print(y)
    y = time.time()
    if (x == 676767):
        print("gg 0.0000067% chance")
        time.sleep(0.67)

#------------------------------------------------------------------------------
# Challenges

#1
namee = "Radia Perlman"
agee = 34
occupationn = "Networking Engineer"

#2
countt = 10
new_countt = countt + 5
print(new_countt)

#3
xx = 4
yy = "hello"
swapper = xx
xx = yy
yy = swapper
print("x = ", xx)
print("y = ", yy)

#4
is_raining = False
is_raining = True
print("Is it raining? Here is the answer: ", is_raining)