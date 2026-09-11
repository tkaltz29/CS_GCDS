import random #importing the ability to make things random

while True: #Looping it
    question = input("8ball:Ask anything and ill respond. Type quit to stop.") #Encouraging user to type and telling them how to use the bot
    response = random.choice(['Yes', 'no', 'ask again later', 'maybe']) #The different responses it will output
    
    if question.lower() == "quit": #Allowing quit to be a command
        print("8ball: Goodbye!") #Making bot say goodbye once quit is recieved
        break #Stops the code completely
    else: #Stating what to do if quit isn't said
        print(response) #Say one of the responses
