import random #importing random module for npc choice
import time #importing time module for delays


player_score = 0 #initializing player score
npc_score = 0 #initializing npc score
choices = ["rock", "paper", "scissors"] #list of choices

input_name = input('What is your name? ').lower().capitalize() #getting player's name

print(f'Hello, {input_name}! Welcome to Rock, Paper, Scissors.') #greeting the player

while True: #main game loop
    mode = input("Ready up? yes/no: ").lower() #asking if player is ready

    if mode == "no": #if player chooses not to play
        print(f"Thanks for playing, {input_name}! Final Score: {input_name}: {player_score}, NPC: {npc_score}") #displaying final score
        break #exiting the game loop

    elif mode == "yes": #if player chooses to play
        print("--- NEW ROUND ---") #indicating new round
        
        while True: #input validation loop for player's choice
            player_choice = input(f'{input_name}, choose: rock, paper, or scissors: ').lower() #getting player's choice
            
            if player_choice in choices: #validating player's choice
                break #exiting input validation loop
            else: #if invalid choice
                print("Invalid choice, please choose rock, paper, or scissors.\n") #prompting again
                continue #continuing the loop

        npc_choice = random.choice(choices) #npc randomly selects a choice
        print(f'{input_name} chose {player_choice}, NPC chose {npc_choice}') #displaying choices
        time.sleep(1) #adding delay 

        if player_choice == npc_choice: #checking for tie
            print("You Tied!") #displaying tie message
        
        elif (player_choice == "rock" and npc_choice == "scissors") or \
             (player_choice == "paper" and npc_choice == "rock") or \
             (player_choice == "scissors" and npc_choice == "paper"): #checking for player win conditions
            print("You win!") #displaying win message
            player_score += 1 #incrementing player score
        
        else: #if none of the above, npc wins
            print("You got eliminated (NPC wins)!") #displaying npc win message
            npc_score += 1 #incrementing npc score

        print(f"Current Score: {input_name}: {player_score}, NPC: {npc_score}\n") #displaying current score

        while True: #input another loop for continuing the game
            continue_input = input('Play another round? yes/no: ').lower() #asking if player wants to continue
            if continue_input == 'yes': #if player wants to continue
                break #breaking to start a new round
            elif continue_input == 'no': #if player wants to stop
                mode = "no" #setting mode to no to exit main loop
                break #breaking to exit
            else: #if invalid input
                print("Please state 'yes' or 'no'.") #prompting again
                continue #continuing the loop
        
        if mode == "no": #checking if player chose to exit
            print(f"Thanks for playing, {input_name}! Final Score: {input_name}: {player_score}, NPC: {npc_score}, ") #displaying final score
            break #exiting the game loop

    else: #if invalid response for ready up 
        print("Invalid response for 'Ready up?', please enter 'yes' or 'no'.") #prompting again
        time.sleep(1) #adding delay