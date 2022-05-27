import random

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["~","!","@","#","$","%","^","&","*","(",")","_","+"]

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))

password = []

for i in range(nr_letters):
    password.append(random.choice(letters))

for i in range(nr_numbers):
    password.append(random.choice(numbers))

for i in range(nr_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)

print(''.join(password))
