import random

def chorus():
    '''
    Prints the chorus lyrics of "my life" by J. Cole, 21 Savage, & Morray
    Args:
        None
    Return:
        None (print): Outputs the chorus lyrics line by line
    '''
    print("  My life is all I have")
    print("  My rhymes, my pen, my pad")
    print("  And I done made it out the struggle, don't judge me")
    print("  What you sayin' now won't budge me")
    print("  'Cause where I come from, so often")
    print("  People you grew up with are layin' in a coffin")
    print("  But I done made it through the pain and strife")
    print("  It's my time now, my world, my life, my life\n")

def sing_song():
    '''
    Prints the full song "my life" by J. Cole, 21 Savage, & Morray,
    calling chorus() for the repeated chorus sections
    Args:
        None
    Return:
        None (print): Outputs the full song lyrics including verses and choruses
    '''
    print("\n--- 'm y l i f e' by J. Cole, 21 Savage, & Morray ---")
    print("[Verse 1: J. Cole]")
    print("Yeah, applying pressure")
    print("Started my grind where crime festers")
    print("And nines measure the souls of adolescent minds...")
    print("\n[Chorus: Morray & 21 Savage]")
    chorus()
    
    print("[Verse 2: 21 Savage]")
    print("If I tell you I love you, I mean it")
    print("Spot a opp and I'm emptyin' the magazine in it...")
    print("\n[Chorus: Morray & 21 Savage]")
    chorus()

def add(num1, num2):
    '''
    Takes two numbers and adds them together
    Args:
        num1 (int): First number to be added
        num2 (int): Second number to be added
    Return:
        None (print): Outputs the sum of num1 and num2
    '''
    print(f"The sum of {num1} and {num2} is: {num1 + num2}")

def print_list(lst):
    '''
    Prints each element of a list on its own line
    Args:
        lst (list): A premade list of elements to be printed
    Return:
        None (print): Outputs each element in the list vertically
    '''
    for element in lst:
        print(element)

def in_list(lst, element):
    '''
    Checks whether a specific element exists inside a list
    Args:
        lst (list): The list to search through
        element (any): The item to look for in the list
    Return:
        OUTPUT (bool): True if the element is found in the list, False otherwise
    '''
    return element in lst

def is_integer(user_input):
    '''
    Checks whether a given user input can be converted to an integer
    Args:
        user_input (str): The value entered by the user to be validated
    Return:
        OUTPUT (bool): True if the input is a valid integer, False otherwise
    Raises:
        ValueError: If the input cannot be converted to an integer
    '''
    try:
        int(user_input)
        return True
    except ValueError:
        return False

def get_integer(prompt="Enter an integer: "):
    '''
    Repeatedly prompts the user until a valid integer is entered
    Args:
        prompt (str): The message displayed to the user when asking for input,
                      defaults to "Enter an integer: "
    Return:
        OUTPUT (int): The validated integer entered by the user
    '''
    while True:
        user_input = input(prompt)
        if is_integer(user_input):
            return int(user_input)
        else:
            print("Invalid input! Please make sure you enter a whole number.")

def get_random():
    '''
    Prompts the user for a min and max value, then generates and prints
    a random integer within that range
    Args:
        None
    Return:
        None (print): Outputs the randomly generated number between min and max
    '''
    print("--- Let's generate a random number ---")
    min_val = get_integer("Enter the starting integer (minimum): ")
    max_val = get_integer("Enter the ending integer (maximum): ")
    
    if min_val > max_val:
        min_val, max_val = max_val, min_val
        
    random_num = random.randint(min_val, max_val)
    print(f"\nYour random number between {min_val} and {max_val} is: {random_num}")

def count_vowels(text):
    '''
    Counts the total number of vowels in a given string and prints
    a subtotal for each individual vowel (a, e, i, o, u)
    Args:
        text (str): The word or phrase to count vowels in
    Return:
        OUTPUT (int): The total number of vowels found in the text
        None (print): Outputs the count of each vowel individually
    '''
    vowels_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    total_vowels = 0
    
    for char in text.lower():
        if char in vowels_counts:
            vowels_counts[char] += 1
            total_vowels += 1
            
    print("\n--- Vowel Subtotals ---")
    for vowel, count in vowels_counts.items():
        print(f"{vowel.upper()}: {count}")
        
    return total_vowels

def reverse_string(text):
    '''
    Reverses the characters in a given string
    Args:
        text (str): The string to be reversed
    Return:
        OUTPUT (str): A new string with the characters in reverse order
    '''
    return text[::-1]

def is_palindrome(text):
    '''
    Checks whether a given word or phrase is a palindrome,
    ignoring spaces and capitalization
    Args:
        text (str): The word or phrase to check
    Return:
        OUTPUT (bool): True if the text is a palindrome, False otherwise
    '''
    clean_text = text.replace(" ", "").lower()
    reversed_text = reverse_string(clean_text)
    return clean_text == reversed_text

def main():
    '''
    Runs the main menu loop, allowing the user to select and execute
    any of the available functions until they choose to quit
    Args:
        None
    Return:
        None (print): Displays the menu and outputs results based on user selection
    '''
    while True:
        print("\n" + "="*30)
        print("      FUNCTION MENU      ")
        print("="*30)
        print("1. Sing a Song (J. Cole - my life)")
        print("2. Add Two Numbers")
        print("3. Print a Demo List Vertically")
        print("4. Check if an Element is in a List")
        print("5. Generate a Random Number")
        print("6. Count Vowels in a String")
        print("7. Reverse a String (Challenge 1)")
        print("8. Check Palindrome (Challenge 2)")
        print("9. Quit")
        
        choice = input("\nSelect a function to run (1-9): ")
        
        if choice == '1':
            sing_song()
            
        elif choice == '2':
            num1 = get_integer("Enter the first number: ")
            num2 = get_integer("Enter the second number: ")
            add(num1, num2)
            
        elif choice == '3':
            demo_list = ["Python", "VS Code", "Functions", "Coding", "J. Cole"]
            print("\nPrinting demo list:")
            print_list(demo_list)
            
        elif choice == '4':
            demo_list = ["apple", "banana", "cherry", "date"]
            print(f"\nHere is the list to search: {demo_list}")
            search_item = input("Enter an element to search for: ").lower()
            found = in_list(demo_list, search_item)
            if found:
                print(f"True! '{search_item}' is in the list.")
            else:
                print(f"False! '{search_item}' is NOT in the list.")
                
        elif choice == '5':
            get_random()
            
        elif choice == '6':
            text = input("\nEnter a word or phrase to count the vowels: ")
            total = count_vowels(text)
            print(f"Total vowels found: {total}")
            
        elif choice == '7':
            text = input("\nEnter a string to reverse: ")
            print(f"Reversed string: {reverse_string(text)}")
            
        elif choice == '8':
            text = input("\nEnter a word or phrase to check if it's a palindrome: ")
            if is_palindrome(text):
                print(f"'{text}' IS a palindrome!")
            else:
                print(f"'{text}' is NOT a palindrome.")
                
        elif choice == '9':
            print("\nExiting program. Goodbye!")
            break
            
        else:
            print("\nInvalid selection. Please choose a number from 1 to 9.")

if __name__ == "__main__":
    main()