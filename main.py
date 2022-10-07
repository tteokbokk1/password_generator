import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

pw_letters = ""
for character in range(0, num_letters):
    pw_letters = pw_letters + random.choice(letters)

pw_numbers = ""
for num in range(0, num_numbers):
    pw_numbers = pw_numbers + random.choice(numbers)

pw_symbols = ""
for sym in range(0, num_symbols):
    pw_symbols = pw_symbols + random.choice(symbols)

easy_pw = pw_letters + pw_numbers + pw_symbols

#create list of characters from the easy_pw characters so they can be randomly ordered for the hard_pw
pw_list = []
for letter in easy_pw:
    pw_list.append(letter)

hard_pw = ""
for n in range(0, len(pw_list)):
    hard_pw += random.choice(pw_list)
print(hard_pw)