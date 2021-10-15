import random
import string 


print("Welcome to your password generator.")
def generate_password():
    characters = set(string.ascii_letters) #
    characters.update(string.digits)
    characters.update(['!', '@', '#', '$', '%', '&', '*'])
    password = random.choice(tuple(characters)) 
    
    lenght = input("How many characteres do you want?\n")
    
    valid_number(lenght)
    
    while len(password) < int(lenght):
        new_character = random.choice(tuple(characters))
        password = password + new_character
    print("Your password is:\n", password)

def valid_number(lenght): 
    if lenght.isnumeric():  
        True
        lenght = int(lenght)
    else:
        print("Invalid character, try again")
        return generate_password()


generate_password()