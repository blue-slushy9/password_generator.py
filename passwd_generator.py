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

else:
    pass

####################### LETTERS, NUMBERS, SYMBOLS? 

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

# Create the types_of_symbols variable and assign an empty list to it BEFORE
# the if statement, so that the list will be accessible outside of the if 
# statement block (we will need it in the last part of the program);
types_of_symbols = []

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
        
        types_of_symbols = input()
        print()

    elif confirm_symbols == 'n':
        confirm_symbols = False 

#################### PHASE 2---NOW WE CAN TAKE THE USER INPUT AND USE IT TO 
#################### GENERATE THE PASSWORD;

# Create a list which will store all of the types of
# characters the user specified they want included in their password;
available_chars = []

# These double if statements below SEEM repetitive and unnecesssary, but we 
# actually get an error without the first one, and the user may end up making
# a mistake without the confirm prompts; the reason we get an error without
# the first one is that the 'confirm_x' variables do not exist if the user
# never typed in that character type to be included in their password;
if 'letters' in types_of_chars or 'all' in types_of_chars:
    if confirm_letters == True:
        
        if 'lower' in types_of_letters:
            # Import lower-case letters of English alphabet and assign them
            # to a new variable;
            lower_alphabet = ascii_lowercase
            
            # .extend() built-in method is used to expand the available_chars
            # list by adding all elements in lower_alphabet string at the same
            # time (as opposed to .append(), which does it one by one);
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
        # Loop through all numbers between 0 and 9...
        for i in range(10):
            # appending each number to the list, one by one;
            available_chars.append(str(i))

if 'symbols' in types_of_chars or 'all' in types_of_chars:
    if confirm_symbols == True:
        available_chars.extend(types_of_symbols)

# All characters that user has indicated they want (potentially) included in
# their password should be in the available characters list now---if there are
# <= 0 characters in the list, the password cannot be created, so we exit;
if len(available_chars) <= 0:
    print("No characters have been designated to be included in the\n" 
            "password. Please restart the program.\n")
    exit()

else:
    # Create an empty list that will hold all characters in string, we cannot
    # initialize it as a string because we first need to manipulate its
    # elements;
    passwd = []

    # Create a loop that will iterate a number of times equal to the number of
    # characters the user wants in their password;
    for n in range(num_of_chars):
        
        # random.choice() method is used to select a character at random from
        # our list of available characters, which were established based on
        # user input;
        add_char = choice(available_chars)
       
        # Each one of these randomly selected characters then gets appended to
        # the end of our passwd list one by one;
        passwd.append(add_char)

    # .join() method is used to concatenate the elements of the passwd list
    # into a single string;
    join_passwd = (''.join(passwd))

    # The former passwd list then gets printed as a string;
    print(f"Congratulations, here is your password: {join_passwd}\n")
