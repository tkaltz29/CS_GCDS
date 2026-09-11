import random
user_name = input("Please enter your name: ")
print ("Good luck", user_name)

while True:
    number = random.randint(1, 10)
    break 
    
guesses_left = 5
correct_guesses = 0
round_number = 0
print ("The computer chose a number between 1 and 10. Guess what it is!")
while guesses_left > 0:
    guesses_left = guesses_left - 1
    user_guess = int(input("Enter your guess: "))
    if user_guess == number:
        print("Correct!")
        correct_guesses += 1
        break
    elif user_guess < number:
        print("Too low.")
    else:
        print("Too high.")
    print("you have", guesses_left, "guesses left.")
    round_number += 1
    
    
    print ("round:", round_number)
    print ("would you like to play again?")
    play_again = input("Enter 'yes' or 'no': ")
    if play_again.lower() == 'yes':
        continue
    if play_again.lower() == 'no':
        print("Thanks for playing!")
        break
    
    

      
    
    
    
    
    
    
    
    