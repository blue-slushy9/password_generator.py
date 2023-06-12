# This program is a secure password generator! You can input how many 
# characters it should consist of, as well as what types of characters you want
# (letters, numbers, symbols);

#import sys, string, random
from sys import exit
from string import ascii_uppercase,ascii_lowercase
from random import choice

print()
print("How many characters should be in your password?")
print()

num_of_chars = int(input())
print()

if num_of_chars <= 0:
    print("This is not a valid number of characters. The program is closing\n" 
           "now, please run it again.")
    print()
    
    # Special method that allows you to exit a program;
    exit()

elif num_of_chars < 30:
    print("As of April 2023, passwords with less than 30 characters are not\n" 
            "secure. Preferably, they should be 40 characters or longer. As\n" 
            "this program is designed to produce *secure* passwords, it will\n" 
            "now close. Please run the program again.")
    print()
    exit()

else:
    pass

print("What types of characters do you want in your password? You can type\n" 
        "'letters', 'numbers', 'symbols', or 'all' (if you only want two of\n" 
        "these options, please separate them with spaces and/or commas; this\n" 
        "prompt is not case-sensitive).")
print()

types_of_chars = input().lower()
print()

if 'letters' in types_of_chars or 'all' in types_of_chars:
    print("You have indicated that you want letters in your password. Is\n"
            "this correct? [Y/N]")
    print()

    confirm_letters = input().lower()
    print()
    
    if confirm_letters == 'y':
        confirm_letters = True
        print("Do you want the letters to be upper-case, lower-case, or\n"
                "both? Please note that, unfortunately, this password\n" 
                "generator only supports the English alphabet at this time.\n"
                "You can type in 'upper-case', 'lower-case', or 'both'\n" 
                "(you can omit the '-' if you want).")
        print()

        types_of_letters = input().lower()
        print()

    elif confirm_letters == 'n':
        confirm_letters = False

if 'numbers' in types_of_chars or 'all' in types_of_chars:
    print("You have indicated that you want numbers to be included in your\n" 
            "password. Is this correct? [Y/N]")
    print()

    confirm_nums = input().lower()
    print()
    
    if confirm_nums == 'y':
        confirm_nums = True 
    elif confirm_nums == 'n':
        confirm_nums = False 

if 'symbols' in types_of_chars or 'all' in types_of_chars:
    print("You have indicated that you want symbols in your password. Is\n" 
            "this correct? [Y/N]")
    print()

    confirm_symbols = input().lower()
    print()

    if confirm_symbols == 'y':
        confirm_symbols = True
        print("As the supported symbols (i.e. special characters) for a\n" 
                "password vary from website to website, I request that you\n" 
                "please enter the symbols you would like included now.")
        print()

        types_of_symbols = list(input())
        print()

    elif confirm_symbols == 'n':
        confirm_symbols = False 

# Phase 2 -- now we can take the user input and use it to generate the password

available_chars = []

if 'letters' in types_of_chars or 'all' in types_of_chars:
    if confirm_letters == True:
        
        if 'lower' in types_of_letters:
            lower_alphabet = ascii_lowercase
            available_chars.extend(list(lower_alphabet))
        
        elif 'upper' in types_of_letters:
            upper_alphabet = ascii_uppercase
            available_chars.extend(list(upper_alphabet))
        
        elif 'both' in types_of_letters:
            lower_alphabet = ascii_lowercase
            upper_alphabet = ascii_uppercase
            available_chars.extend(list(lower_alphabet))
            available_chars.extend(list(upper_alphabet))

if 'numbers' in types_of_chars or 'all' in types_of_chars:
    if confirm_nums == True:
        for i in range(10):
            available_chars.append(str(i))

if 'symbols' in types_of_chars or 'all' in types_of_chars:
    if confirm_symbols == True:
        available_chars.extend(types_of_symbols)

if len(available_chars) <= 0:
    print("No characters have been designated to be included in the\n" 
            "password. Please restart the program.\n")

else:
    passwd = []

    for n in range(num_of_chars):
        add_char = choice(available_chars)
        passwd.append(add_char)

    join_passwd = (''.join(passwd))

    print(f"Congratulations, here is your password: {join_passwd}\n")
