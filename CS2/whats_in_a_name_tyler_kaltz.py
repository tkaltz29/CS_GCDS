def get_word():
    word = input("Enter your name or a word: ")

    char_array = []
    for letter in word:
        char_array.append(letter)

    return char_array


def reverse_and_display(char_array):
    reversed_array = []

    index = len(char_array) - 1
    while index >= 0:
        reversed_array.append(char_array[index])
        index = index - 1

    reversed_word = ""
    for letter in reversed_array:
        reversed_word = reversed_word + letter

    return reversed_word


def count_vowels(char_array):
    vowel_count = 0

    for letter in char_array:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            vowel_count = vowel_count + 1
        elif letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
            vowel_count = vowel_count + 1

    return vowel_count


def return_uppercase(char_array):
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""
    for letter in char_array:
        found = False
        i = 0
        while i < len(lowercase_letters) and not found:
            if letter == lowercase_letters[i]:
                result = result + uppercase_letters[i]
                found = True
            i = i + 1
        if not found:
            result = result + letter

    return result


def show_menu():
    print("1. Reverse and display")
    print("2. Count vowels")
    print("3. Convert to uppercase")
    print("4. Quit")


my_array = get_word()

choice = ""
while choice != "4":
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        print(reverse_and_display(my_array))
    elif choice == "2":
        print(count_vowels(my_array))
    elif choice == "3":
        print(return_uppercase(my_array))
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Not a valid option, try again.")
