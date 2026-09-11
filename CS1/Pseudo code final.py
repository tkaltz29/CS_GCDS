import random

user_name = input("Please enter your name: ")
print("Good luck,", user_name + "!")


total_rounds = 0
correct_guesses = 0

while True:
   
    number = random.randint(1, 10) 
    guesses_left = 5
    round_number = total_rounds + 1 
    print("\n--- Round", round_number, "---")
    print("The computer chose a number between 1 and 10. Guess what it is!")

    guessed_correctly_in_round = False
    
    while guesses_left > 0:
        
        
        while True:
            try:
                user_guess = int(input(f"Enter your guess (Guesses left: {guesses_left}): "))
                if 1 <= user_guess <= 10:
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number thats 1 through 10.")
            guesses_left -= 1 
                        
        guesses_left -= 1

        if user_guess == number:
            print("You got it!")
            correct_guesses += 1
            guessed_correctly_in_round = True
            break 
        elif user_guess < number:
            print("Your # is too low.")
        else: 
            print("Your # is too high.")
        
        if guesses_left > 0:
             print(f"You have {guesses_left} guesses left.")
        
    total_rounds += 1
    
    if not guessed_correctly_in_round:
        print(f"\nYou lost! The number was {number}.")
        
    print("\nDo you want to play again?")
    play_again = input("Enter 'yes' or 'no': ").lower()
    
    if play_again not in ('yes', 'y'):
        print(f"\n--- Final Score for {user_name} ---")
        print(f"Rounds Played: {total_rounds}")
        print(f"Rounds Won: {correct_guesses}")
        print("Thanks for playing! Goodbye.")
        break 