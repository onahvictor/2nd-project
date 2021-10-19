import random
import string

print("welcome to the pi password Generator")

def password():

    password = ""
    letters = input("How many letters would you like in your password? ")
    if letters:
        letters = int(letters)
        for char in range(letters):
            password += random.choice(string.ascii_letters)

    symbols = input("How many symbols would you like? ")
    if symbols:
        symbols = int(symbols)
        for sym in range(symbols):
            password += random.choice(string.punctuation)

    numbers = input("How Many numbers would you like? ")
    if numbers:
        numbers = int(numbers)
        for num in range(numbers):
            password += str(random.randint(0,9))
            
    password = list(password)
    random.shuffle(password)

    for element in password:
        generate_password = ''.join(password)

    print(f'your password is {generate_password}')


password()