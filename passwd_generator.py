# This program is a secure password generator! You can input how many 
# characters it should consist of, as well as what types of characters you want
# (letters, numbers, symbols);

############## IMPORT MODULES

# sys.exit() allows you to exit a program;
from sys import exit

# These string methods allow you to import upper- and lower-case letters of
# the English alphabet, respectively;
from string import ascii_uppercase , ascii_lowercase

# random.choice() allows you to select an element at random from a list (at
# least in this program);
from random import choice

############## PHASE 1---USER ENTERS VARIOUS INPUTS IN ORDER TO SPECIFY 
############## PASSWORD LENGTH, INCLUDED TYPES OF CHARACTERS, ETC.;

# Throughout this program I insert print() statements to increase legibility;
print()

############### HOW MANY CHARACTERS IN PASSWORD?

print("How many characters should be in your password?")
print()

# User enters the total number of characters they want in their password;
num_of_chars = int(input())
print()

# This if statement controls for invalid 'number of characters' input,
# e.g. 0 or -1;
if num_of_chars <= 0:
    print("This is not a valid number of characters. The program is closing\n" 
           "now, please run it again.")
    print()
    exit()


# This if statement controls for 'number of characters' input less than 30,
# for reasons explained in the print statement;
elif num_of_chars < 30:
    print("As of April 2023, passwords with less than 30 characters are not\n" 
            "secure. Preferably, they should be 40 characters or longer. As\n" 
            "this program is designed to produce *secure* passwords, it will\n" 
            "now close. Please run the program again.")
    print()
    exit()

# If 'number of characters' meets requirements, we use pass to continue onto
# the next line of code;
else:
    pass

####################### LETTERS, NUMBERS, SYMBOLS? 

print("What types of characters do you want in your password? You can type\n" 
        "'letters', 'numbers', 'symbols', or 'all' (if you only want two of\n" 
        "these options, please separate them with spaces and/or commas; this\n" 
        "prompt is not case-sensitive).")
print()

# User types in one of the strings mentioned in the above print statement;
types_of_chars = input().lower()
print()

# If user typed in 'letters' or 'all'...
if 'letters' in types_of_chars or 'all' in types_of_chars:
    print("You have indicated that you want letters in your password. Is\n"
            "this correct? [Y/N]")
    print()

# User confirms whether they want letters in their password;
    confirm_letters = input().lower()
    print()
    
    # If user confirmed they want letters in their password...
    if confirm_letters == 'y':
        # Cast confirm_letters variable as Boolean from string;
        confirm_letters = True
        # Ask user whether they want upper-case, lower-case, or both;
        print("Do you want the letters to be upper-case, lower-case, or\n"
                "both? Please note that, unfortunately, this password\n" 
                "generator only supports the English alphabet at this time.\n"
                "You can type in 'upper-case', 'lower-case', or 'both'\n" 
                "(you can omit the '-' if you want).")
        print()
        
        # User states whether they want letters to be upper-case, lower-case, 
        # or both;
        types_of_letters = input().lower()
        print()

    # Else-if user confirmed they do NOT want letters in their password...
    elif confirm_letters == 'n':
        # Cast confirm_letters as Boolean from string;
        confirm_letters = False

if 'numbers' in types_of_chars or 'all' in types_of_chars:
    print("You have indicated that you want numbers to be included in your\n" 
            "password. Is this correct? [Y/N]")
    print()
    
    # User confirms whether they want numbers in their password;
    confirm_nums = input().lower()
    print()
    
    if confirm_nums == 'y':
        # Variable confirm_nums gets cast as Boolean from string;
        confirm_nums = True 
    elif confirm_nums == 'n':
        # Variable confirm_nums gets cast as Boolean from string;
        confirm_nums = False 

# If user entered 'symbols' or 'all' into initial prompt...
if 'symbols' in types_of_chars or 'all' in types_of_chars:
    print("You have indicated that you want symbols in your password. Is\n" 
            "this correct? [Y/N]")
    print()

    # User confirms whether they want symbols in their password;
    confirm_symbols = input().lower()
    print()

    if confirm_symbols == 'y':
        # Variable confirm_symbols gets cast as Boolean from string;
        confirm_symbols = True
        print("As the supported symbols (i.e. special characters) for a\n" 
                "password vary from website to website, I request that you\n" 
                "please enter the symbols you would like included now.")
        print()
        
        # Since accepted symbols (special characters) vary depending on the 
        # website, user is asked to enter which they would like to use;
        types_of_symbols = list(input())
        print()

    elif confirm_symbols == 'n':
        confirm_symbols = False 

#################### PHASE 2---NOW WE CAN TAKE THE USER INPUT AND USE IT TO 
#################### GENERATE THE PASSWORD;

# Create a list, available_chars, which will store all of the types of
# characters the user specified they want included in their password;
available_chars = []


if 'letters' in types_of_chars or 'all' in types_of_chars:
    if confirm_letters == True:
        
        if 'lower' in types_of_letters:
            lower_alphabet = ascii_lowercase
            # .extend() built-in method is used to expand the available_chars
            # list WITHOUT deleting anything that's already in it;
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
