import random
import time

x = random.randint(1,100)
y = time.time()

for i in range(1,100067):
    x = random.randint(1,100067)
    print(x)
    if (x == 1):
        print("gg 0.0001% chance")
        time.sleep(0.67)
        

print("Hello World")
print("Age: ", 24)
print("Sum: ", 6 + 7)

print("\n")
print("Good \nmorning \npopatlaal")
print("\tIt is me... \tpopatlaal!")

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
print(False + True) # 0 + 1 = 1 (True)
print(1 == 1) # True
print(1 == 0) # False
print(1 != 1) # False
print(1 != 0) # True
print("Hello" == "hello") # False!! CASE SENSITIVE (because in ASCII, the "H" has a different binary than "h")
print(6 + 7 == 67) # False

# how do I know what data type I'm working with?
# this is the solution!
print("\n")
print(type("hi"))
print(type(3))
print(type(3.14159265358979323846264338327950288419716939937510))