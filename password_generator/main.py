import random
import string 

characters = set(string.ascii_letters) #
characters.update(string.digits)
characters.update(['!', '@', '#', '$', '%', '&', '*'])

print("Welcome to your password generator.")

def generate_password():
    password = ''

    while len(password) < int(lenght):
        new_character = random.choice(tuple(characters))
        password = password + new_character
    print("Your password is:\n", password)

def valid_number(lenght): 
    return lenght.isnumeric()

lenght = input("How many characteres do you want?\n")
    
while (not valid_number(lenght)):
    print("Invalid character, try again")
    lenght = input("How many characteres do you want?\n")

generate_password()
