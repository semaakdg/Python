"""
# 5EASY LEVEL
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



for char in range(0, 1):
    password = ""
    for char in range(0, nr_letters):
        nr_letters = random.choice(letters)
        password += nr_letters
    for char in range(0, nr_symbols):
        nr_symbols = random.choice(symbols)
        password += nr_symbols
    for char in range(0, nr_numbers):
        nr_numbers = random.choice(numbers)
        password += nr_numbers
    print(f"Your password is: {password}")
"""
"""
for x in range(0, 1):
    password = ""
    for x in range(0, nr_letters):
        nr_letters = random.choice(letters)
        password += nr_letters
    print(f"Your password: {password}")

for x in range (0, 1):
    password = ""
    for x in range(0, nr_symbols):
        nr_symbols = random.choice(symbols)
        password += nr_symbols
    print(f"Your password: {password}")

for x in range (0, 1):
    password = ""
    for x in range(0, nr_numbers):
        nr_numbers = random.choice(numbers)
        password += nr_numbers
    print(f"Your password: {password}")
    """


    

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   random_char = random.choice(letters)
#   password += random_char //bunu yazabilirim

#   password += random.choice(letters) // ya da bunu yazabilirim. ikiside ayn?? ??ey

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
# password_list += random.choice(letters) // yukar??daki ile ayn?? ??ey asl??nda

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list) # listeyi kar??????k bir bi??imde yazd??rmam??z?? sa??l??yor. 'aDef?+!285' gibi s??ral?? bir ??ifreyi '8ae+!D5?8' gibi kar??????k bir bi??imde yazmam??z?? sa??l??yor.

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

