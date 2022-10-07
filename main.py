import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

pw_letters = []
for character in range(0, num_letters):
    pw_letters.append(random.choice(letters))

pw_numbers = []
for num in range(0, num_numbers):
    pw_numbers.append(random.choice(numbers))

pw_symbols = []
for sym in range(0, num_symbols):
    pw_symbols.append(random.choice(symbols))

#insert ordered passwords into a single list to shuffle
temp_pw = pw_letters + pw_numbers + pw_symbols
random.shuffle(temp_pw)

final_pw = ""
for n in range(0, len(temp_pw)):
    final_pw += temp_pw[n]
print(final_pw)