#**************************************************************
# Name: Tyler Kaltz
#
# Description: This program asks the user for their name (or
#   any word) and turns it into an array (list) of characters.
#   Then a menu lets you pick different functions that mess with
#   the array, like reversing it, counting vowels, pulling out
#   the first/middle/last name, making it upper or lowercase,
#   scrambling it, and checking for palindromes.
#   No string class functions are used (no .upper(), .split(),
#   etc). Everything is done with loops.
#
# Bugs:
#   - If you only type one word, first name and last name both
#     come back as that same word.
#   - Typing two spaces in a row can make the name functions
#     act weird because they think there is an empty name.
#   - Titles like "Dr." get counted as the first name.
#   - The scramble can sometimes give back the same order it
#     started with (it's random).
#   - Palindrome check does not ignore punctuation.
#
# Bonus:
#   - #13 Built a menu so the user can pick which function to test
#
# Log:
#   9/18 - Started project. Made get_word, reverse, and count vowels
#   9/18 - Added uppercase function and the menu
#   9/24 - Added make initials, made reverse shorter
#   9/29 - Added first/middle/last name, hyphen check, lowercase,
#          consonants, scramble, and palindrome. Wrote documentation.
#**************************************************************

import random


#--------------------------------------------------------------
# get_word
# Description: Asks the user for a name or word and puts each
#   letter into a list one at a time.
# Parameters: none
# Returns: char_array - list of characters the user typed
#--------------------------------------------------------------
def get_word():
    word = ""
    char_array = []

    word = input("Enter your name or a word: ")

    # add each letter to the end of the list
    for letter in word:
        char_array.append(letter)

    return char_array


#--------------------------------------------------------------
# reverse_and_display
# Description: Flips the name backwards.
# Parameters: char_array - list of characters
# Returns: reversed_word - the name backwards as a string
#--------------------------------------------------------------
def reverse_and_display(char_array):
    reversed_word = ""
    index = len(char_array) - 1

    # start at the last letter and go backwards to index 0
    while index >= 0:
        reversed_word = reversed_word + char_array[index]
        index = index - 1

    return reversed_word


#--------------------------------------------------------------
# count_vowels
# Description: Counts how many vowels are in the name. Checks
#   both lowercase and uppercase.
# Parameters: char_array - list of characters
# Returns: vowel_count - number of vowels
#--------------------------------------------------------------
def count_vowels(char_array):
    vowel_count = 0

    for letter in char_array:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            vowel_count = vowel_count + 1
        elif letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
            vowel_count = vowel_count + 1

    return vowel_count


#--------------------------------------------------------------
# count_consonants
# Description: Counts how many consonants are in the name.
#   A consonant is any letter that isn't a vowel, so spaces
#   and hyphens don't count.
# Parameters: char_array - list of characters
# Returns: consonant_count - number of consonants
#--------------------------------------------------------------
def count_consonants(char_array):
    consonant_count = 0

    for letter in char_array:
        # first make sure it's actually a letter
        if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z'):
            # then make sure it's not a vowel
            if letter not in "aeiouAEIOU":
                consonant_count = consonant_count + 1

    return consonant_count


#--------------------------------------------------------------
# return_first_name
# Description: Gets the first name (everything before the
#   first space).
# Parameters: char_array - list of characters
# Returns: first_name - the first name as a string
#--------------------------------------------------------------
def return_first_name(char_array):
    first_name = ""
    index = 0

    # keep adding letters until we hit a space or the end
    while index < len(char_array) and char_array[index] != " ":
        first_name = first_name + char_array[index]
        index = index + 1

    return first_name


#--------------------------------------------------------------
# return_last_name
# Description: Gets the last name (everything after the last
#   space).
# Parameters: char_array - list of characters
# Returns: last_name - the last name as a string
#--------------------------------------------------------------
def return_last_name(char_array):
    last_name = ""
    index = len(char_array) - 1

    # start at the end and go backwards until we hit a space.
    # the letter goes in FRONT of last_name so it doesn't come
    # out backwards
    while index >= 0 and char_array[index] != " ":
        last_name = char_array[index] + last_name
        index = index - 1

    return last_name


#--------------------------------------------------------------
# return_middle_name
# Description: Gets the middle name(s), which is everything
#   between the first space and the last space.
# Parameters: char_array - list of characters
# Returns: middle_name - the middle name(s) as a string, or a
#   message if there isn't one
#--------------------------------------------------------------
def return_middle_name(char_array):
    middle_name = ""
    first_space = -1
    last_space = -1
    index = 0

    # find where the first and last spaces are.
    # -1 means we haven't found one yet
    while index < len(char_array):
        if char_array[index] == " ":
            if first_space == -1:
                first_space = index
            last_space = index
        index = index + 1

    # if there's 0 or 1 spaces, there's no middle name
    if first_space == last_space:
        return "No middle name"

    # grab everything between the two spaces
    index = first_space + 1
    while index < last_space:
        middle_name = middle_name + char_array[index]
        index = index + 1

    return middle_name


#--------------------------------------------------------------
# has_hyphen
# Description: Checks if the last name has a hyphen in it
#   (like Smith-Jones).
# Parameters: char_array - list of characters
# Returns: True if there's a hyphen, False if not
#--------------------------------------------------------------
def has_hyphen(char_array):
    last_name = return_last_name(char_array)

    for letter in last_name:
        if letter == "-":
            return True

    return False


#--------------------------------------------------------------
# return_uppercase
# Description: Makes every letter uppercase.
# Parameters: char_array - list of characters
# Returns: result - the name in all caps
#--------------------------------------------------------------
def return_uppercase(char_array):
    result = ""

    for letter in char_array:
        # ord() gives the ASCII number of a letter and chr() turns
        # a number back into a letter. Uppercase letters are 32
        # less than lowercase ones, so subtract 32
        if letter >= 'a' and letter <= 'z':
            result = result + chr(ord(letter) - 32)
        else:
            result = result + letter

    return result


#--------------------------------------------------------------
# return_lowercase
# Description: Makes every letter lowercase. Same idea as
#   uppercase but backwards (add 32 instead).
# Parameters: char_array - list of characters
# Returns: result - the name in all lowercase
#--------------------------------------------------------------
def return_lowercase(char_array):
    result = ""

    for letter in char_array:
        if letter >= 'A' and letter <= 'Z':
            result = result + chr(ord(letter) + 32)
        else:
            result = result + letter

    return result


#--------------------------------------------------------------
# scramble_name
# Description: Mixes up the letters to make a random name.
#   Makes a copy first so the original name doesn't get
#   messed up for the other menu options.
# Parameters: char_array - list of characters
# Returns: result - the scrambled name as a string
#--------------------------------------------------------------
def scramble_name(char_array):
    scrambled = []
    result = ""
    temp = ""
    swap_spot = 0
    index = 0

    # copy the list
    for letter in char_array:
        scrambled.append(letter)

    # go through every spot and swap it with a random spot.
    # temp holds one letter so it doesn't get lost during the swap
    while index < len(scrambled):
        swap_spot = random.randint(0, len(scrambled) - 1)
        temp = scrambled[index]
        scrambled[index] = scrambled[swap_spot]
        scrambled[swap_spot] = temp
        index = index + 1

    # turn the list back into a string
    for letter in scrambled:
        result = result + letter

    return result


#--------------------------------------------------------------
# is_palindrome
# Description: Checks if the first name is the same forwards
#   and backwards (like "Anna" or "Bob"). Makes it lowercase
#   first so "Anna" works even with the capital A.
# Parameters: char_array - list of characters
# Returns: True if it's a palindrome, False if not
#--------------------------------------------------------------
def is_palindrome(char_array):
    first_name = ""
    backwards = ""

    first_name = return_first_name(char_array)
    first_name = return_lowercase(list(first_name))
    backwards = reverse_and_display(list(first_name))

    if first_name == backwards:
        return True
    else:
        return False


#--------------------------------------------------------------
# make_initials
# Description: Takes the first letter of each word and makes
#   it uppercase (John Michael Smith -> JMS).
# Parameters: char_array - list of characters
# Returns: the initials as a string
#--------------------------------------------------------------
def make_initials(char_array):
    initials = ""
    at_start_of_word = True

    # at_start_of_word turns True after every space, so the
    # next letter gets grabbed as an initial
    for letter in char_array:
        if letter == " ":
            at_start_of_word = True
        else:
            if at_start_of_word:
                initials = initials + letter
                at_start_of_word = False

    return return_uppercase(list(initials))


#--------------------------------------------------------------
# show_menu
# Description: Prints out all the menu options.
# Parameters: none
# Returns: nothing
#--------------------------------------------------------------
def show_menu():
    print()
    print("1. Reverse and display")
    print("2. Count vowels")
    print("3. Count consonants")
    print("4. Return first name")
    print("5. Return middle name")
    print("6. Return last name")
    print("7. Check if last name has a hyphen")
    print("8. Convert to lowercase")
    print("9. Convert to uppercase")
    print("10. Scramble name")
    print("11. Check if first name is a palindrome")
    print("12. Make initials")
    print("13. Quit")


#--------------------------------------------------------------
# Main program
# Gets the name once, then keeps showing the menu until the
# user picks 13 to quit.
#--------------------------------------------------------------
my_array = []
choice = ""

my_array = get_word()

while choice != "13":
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        print("Reversed:", reverse_and_display(my_array))
    elif choice == "2":
        print("Vowels:", count_vowels(my_array))
    elif choice == "3":
        print("Consonants:", count_consonants(my_array))
    elif choice == "4":
        print("First name:", return_first_name(my_array))
    elif choice == "5":
        print("Middle name:", return_middle_name(my_array))
    elif choice == "6":
        print("Last name:", return_last_name(my_array))
    elif choice == "7":
        print("Has hyphen:", has_hyphen(my_array))
    elif choice == "8":
        print("Lowercase:", return_lowercase(my_array))
    elif choice == "9":
        print("Uppercase:", return_uppercase(my_array))
    elif choice == "10":
        print("Scrambled:", scramble_name(my_array))
    elif choice == "11":
        print("Palindrome:", is_palindrome(my_array))
    elif choice == "12":
        print("Initials:", make_initials(my_array))
    elif choice == "13":
        print("Goodbye!")
    else:
        print("Not a valid option, try again.")