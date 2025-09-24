import random
import time

x = random.randint(1,100)
y = time.time()

for i in range(1,100000):
    x = random.randint(1,100000)
    print(x)
    if (x == 1):
        print("gg 0.0001% chance")
        time.sleep(1)
        

print("Hello World")
print("Age: ", 24)
print("Sum: ", 6 + 7)

#print("As \nhe \ncrossed \ntoward the pharmacy at the corner he involuntarily turned his head because of a burst of light that had ricocheted from his temple, and saw, with that quick smile with which we greet a rainbow or a rose, a blindingly white parallelogram of sky being unloaded from the van-a dresser with mirrors across which, as across a cinema screen, passed a flawlessly clear reflection of boughs sliding and swaying not arboreally, but with a human vacillation, produced by the nature of those who were carrying this sky, these boughs, this gliding facade")

print("\n")
# normal integers
print(70)
print(-42)
print(100 - 30)

print("\n")
print(float((6 + 7) + (6 * 7) + (6 - 7) + (6 / 7) + (6 ** 7)))

# floats
print(4.0)
print(2.0 + 4.5)
print(2.0 + 4) #becomes float anyways

print("\n")
# ba ba bool (booleans)
print(True) # 1
print(False) # 0
#print(False + True) # 0 + 1 = 1 (True)