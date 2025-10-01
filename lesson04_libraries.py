import random, time, math

print("\n--= Math Library =--\n")

print("Sqrt: \t\t", math.sqrt(4489))
print("Round up: \t", math.ceil(66.67))
print("Round down: \t", math.floor(67.67))
print("Power: \t\t", math.pow(8.18535277187245, 2))
print("Pi: \t\t", math.pi)
print("Euler's Number: ", math.e)

#-------------------------------------------------------------------------------
print("\n--= Random Library =--\n")

# computers can't generate random numbers, so they use...
# psuedorandom number generator (PRNG) --> not a TRUE random generator
# rolling a dice --> TRUE random generator
# to make a random number, computers need to make a bunch of code to make number seem random

# attempt at making a random number without random.randint or random.shuffle

seed = 676.76
seed = seed * time.time()
seed = seed / 6767
seed = math.sqrt(seed)
seed = seed * 10000000000
seed = seed % 10
seed = math.floor(seed)
#seed = str(seed)
#seed = list(seed)
#random.shuffle(seed)
print("Random number using the same seed (wow): ", seed)

print("Random integer: ", random.randint(1,10))
print("Random float between 0 and 1: ", random.random())
my_favs = ["taco", "burrito", "enchilada", "quesadilla"]
print(random.choice(my_favs))
random.shuffle(my_favs)
print(my_favs)


print("\n--= Challenges =--\n")

# ----------------------------------------------------------------
# 1)
diameter = 14
radius = diameter / 2
circle_area = math.pi * radius * radius
print("Area of circle: ", circle_area)

# 2)
die_roll = random.randint(1, 6)
print("The dice rolled", die_roll)


