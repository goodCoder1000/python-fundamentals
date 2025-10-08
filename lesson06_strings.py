# Basic string creation and indexes:
greeting = "Hello"
name = "Ada"
print(greeting, name)

# 0 1 2 3 4 
# H e l l o
second_letter = greeting[1]
print(second_letter)

message = greeting + " " + name + "!!!!"
print("Concatenated message:", message)

print()

word = "Super-cali-fragil-istic-expi-ali-docious"
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Range of letters (non-inclusive):", word[-7:-2])
print(word[:5])
print("Last seven letters:", word[-7:])
print("Step through every second character:", word[::2])
print("Reversed, stepping every third letter:", word[::-3])

## Built in functions

country = "Finland"
length_of_word = len(country)
print(length_of_word)

phrase = "cHicKEN_cuTlY9000"
print("\nUppercase:", phrase.upper())
print("Lowercase:", phrase.lower())
print("Capitalize:", phrase.capitalize())
print("Title Format:", phrase.title())

print()

#Find and replace text
sentence = "I'm a goofy goober"
new_sentence = sentence.replace("I'm", "You're")
next_replacement = sentence.replace("goofy", "goober")
print(sentence)
print(new_sentence)
print(next_replacement)

# FORMATTED STRINGS IN PYTHON
# f-strings allow variables and expressions inside strings

print("\n--- Formatted Strings ---")

name = "Adam"
age = 400
city = "Valhalla"

print(f"Hello, my name is {name}. I am {age} years old and live in {city}.")

# f-strings can do math and function calls inside {}

print(f"Next year, I'll be {age + 1}. My name in uppercase is {name.upper()}.")

# Challenge 1
quote = input("gimme fav quote plz: ")
print(f"Your amount of chars in your quote is {len(quote)}")

# Challenge 2
first = input("first name: ")
last = input("last name: ")
print(f"{last.capitalize()}, {first.capitalize()}")

# i did it in 1 line because thats funny haha
print(f"{input("What is your last name: ")}, {input("What is your first name: ")}")

# Challenge 3
wordd = input("give word: ")
print("\nUppercase:", wordd.upper())
print("Lowercase:", wordd.lower())
print("Backwards:", wordd[::-1])