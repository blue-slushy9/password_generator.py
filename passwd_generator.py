# This program is a secure password generator! You can input how many characters it should consist of,
# as well as what types of characters you want (letters, numbers, symbols).

import sys, string, random

print("How many characters should be in your password?")

num_of_chars = int(input())
print()

if num_of_chars <= 0:
    print("This is not a valid number of characters. The program is closing now, please run it again.")
    print()
    sys.exit()

elif num_of_chars < 30:
    print("As of April 2023, passwords with less than 30 characters are not secure. Preferably, they should be 40 characters or longer. As this program is designed to produce *secure* passwords, it will now close. Please run the program again.")
    print()
    sys.exit()

else:
    pass

print("What types of characters do you want in your password? You can type 'letters', 'numbers', 'symbols', or 'all' (if you only want two of these options, please separate them with spaces and/or commas; this prompt is not case-sensitive).")

types_of_chars = input().lower()
print()

if 'letters' in types_of_chars or 'all' in types_of_chars:
    print("You have indicated that you want letters in your password. Is this correct? Just type 'yes' or 'no', 'y' or 'n'.")
    confirm_letters = input().lower()
    print()
    
    if confirm_letters == 'yes' or confirm_letters == 'y':
        confirm_letters = True
        print("Do you want the letters to be upper-case, lower-case, or both? Please note that, unfortunately, this password generator only supports the English alphabet at this time. You can type in 'upper-case', 'lower-case', or 'both' (you can omit the '-' if you want).")
        types_of_letters = input().lower()
        print()

    elif confirm_letters == 'no' or confirm_letters == 'n':
        confirm_letters = False

if 'numbers' in types_of_chars or 'all' in types_of_chars:
    print("You have indicated that you want numbers to be included in your password. Is this correct? You can type in 'yes' or 'no', 'y' or 'n'.")
    confirm_nums = input().lower()
    print()
    
    if confirm_nums == 'yes' or confirm_nums == 'y':
        confirm_nums = True 
    elif confirm_nums == 'no' or confirm_nums == 'n':
        confirm_nums = False 

if 'symbols' in types_of_chars or 'all' in types_of_chars:
    print("You have indicated that you want symbols in your password. Is this correct? Just type 'yes' or 'no', 'y' or 'n'.")
    
    confirm_symbols = input().lower()
    print()

    if confirm_symbols == 'yes' or confirm_symbols == 'y':
        confirm_symbols = True
        print("As the supported symbols (i.e. special characters) for a password vary from website to website, I request that you please enter the symbols you would like included now.")
        types_of_symbols = list(input())
        print()

    elif confirm_symbols == 'no' or confirm_symbols == 'n':
        confirm_symbols = False 

# Phase 2 -- now we can take the user input and use it to generate the password

available_chars = []

if 'letters' in types_of_chars or 'all' in types_of_chars:
    if confirm_letters == True:
        if 'lower' in types_of_letters:
            lower_alphabet = string.ascii_lowercase
            available_chars.extend(list(lower_alphabet))
        elif 'upper' in types_of_letters:
            upper_alphabet = string.ascii_uppercase
            available_chars.extend(list(upper_alphabet))
        elif 'both' in types_of_letters:
            lower_alphabet = string.ascii_lowercase
            upper_alphabet = string.ascii_uppercase
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
    print("No characters have been designated to be included in the password. Please restart the program.\n")

else:
    passwd = []

    for n in range(num_of_chars):
        add_char = random.choice(available_chars)
        passwd.append(add_char)

    join_passwd = (''.join(passwd))

    print(f"Congratulations, here is your password: {join_passwd}\n")
