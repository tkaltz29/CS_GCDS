import random

def chorus():

    '''
 Prints the chorus of a song
    Args:
        None
    Returns:
        print: chorus
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
    Use the chorus function to sing the entire song
    Args:
        None
    Returns:
        print: entire song
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
        num 1 (int): first number
        num 2 (int): second number
    Returns:
        print: sum of the two numbers
    '''    
    print(f"The sum of {num1} and {num2} is: {num1 + num2}")

def print_list(lst):
    '''
Gets elements from user and prints it in a list

Args:
PARAMETER (lst): Gets premade list
Print: 
OUTPUT: (print) Prints a list
    '''
    for element in lst:
        print(element)

def in_list(lst, element):
    '''
Looks for item in a list

Args:
PARAMETER: 
(lst): Premade List
(element): Specific thing in list
Returns:
OUTPUT (Boolean): Checks if the element in the list or not
    '''
    return element in lst

def is_integer(user_input):
    '''
Checks to see if user input is an integer

Args:
PARAMETER (user_input): user input
Return:
OUTPUT (Boolean): Checks if the value is a integer
Raises:
(value error): If the user input is not a integer
    '''
    try:
        int(user_input)
        return True
    except ValueError:
        return False

def get_integer(prompt="Enter an integer: "):
    while True:
        user_input = input(prompt)
        if is_integer(user_input):
            return int(user_input)
        else:
            print("Invalid input! Please make sure you enter a whole number.")

def get_random():
    print("--- Let's generate a random number ---")
    min_val = get_integer("Enter the starting integer (minimum): ")
    max_val = get_integer("Enter the ending integer (maximum): ")
    
    if min_val > max_val:
        min_val, max_val = max_val, min_val
        
    random_num = random.randint(min_val, max_val)
    print(f"\nYour random number between {min_val} and {max_val} is: {random_num}")

def count_vowels(text):
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
    return text[::-1]

def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    reversed_text = reverse_string(clean_text)
    return clean_text == reversed_text

def main():
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