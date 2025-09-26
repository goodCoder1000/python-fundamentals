import random
import time

print("Sum: \t\t", str(41 + 26)) # add + 
print("Difference: \t", str(69 - 2)) # subtract - 
print("Product: \t", str(6.7 * 10)) # multiply *
print("Quotient: \t", str(402 / 6)) # divide / 
print("Floor Quotient: ", str(403 // 6)) # floor divide //
print("Modulo: \t", str(6767 % 100)) # modulo % 
print("Exponent: \t", str(8.18535277187245 ** 2)) # exponentation **

big_equation = ((((round(((6 + 7) * 6) / 7)) ** 7) % 6767) // 67) - 7 # "you cant make an equation using every symbol and only the numbers 6 and 7 that equals 67"
print("Big equation: \t", big_equation)

#--------------------------------------------------------------------------------
# CHALLENGES
print("\nChallenges: ")

# 1.
area_of_rect = 8 * 5
print("\nArea of Rectangle: ", area_of_rect)

# 2.
area_of_circle = 3.14 * 7 ** 2
print("Area of Circle: ", area_of_circle)

# 3.
cost = 12.99 * 3 + 3.5 * 4
print("Cost total: ", cost)
hidden_tax = 14.03 
cost = cost + hidden_tax
print("Cost total + tax (not part of challenge): ", cost)

# 4.
number = random.randint(1, 100)
if (number % 2 == 0):
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")


