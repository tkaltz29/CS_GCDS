import time #importing the time function
import datetime #importing the date function

print ("ALARM!") #displaying that alarm is ringing
current_time = datetime.datetime(2025, 11, 18, 6, 45) #putting in current time

school = input('School? ') #Asking if you'r going to school.

if school == "yes": #allowing yes to be a input for school
    gym = input('Gym? ') #asking if you'r going to gym

    if gym == "yes": #allowing yes to be a input for gym
        print ("you dress up for gym, go to school, then workout") #telling what you do when you say yes to the gym
        print ("pick your food: Bagel, Blue Berry Waffle, or Eggs") #asking what food you would like
        bagel = input("bagel?") #asking if you want a bagel
        
        blueberrywaffle = input ("blue berry waffle?") #asking if you want blueberrywaffles
        eggs = input ("eggs?") #asking if you want eggs
        print ("you go eat and get ready for the day") #you finish and the story ends
    
    if gym == "no":
        print ("Dress up for school, go to school") #telling what you do when you say no to the gym
        print ('pick your food: Bagel, Blue Berry Waffle, or Eggs ') #asking what food you would like
        bagel = input("bagel?") #asking if you want a bagel
        
        blueberrywaffle = input ("blue berry waffle?") #asking if you want blueberrywaffles
        eggs = input ("eggs?") #asking if you want eggs
        print ("you go eat and get ready for the day") #you finish and the story ends
    

    
    

    







elif school == "no": #allowing no to be a input for school
    sleep = input("Sleep?") #asking if you want to sleep

    if sleep == "yes": #making yes an answer to sleep
        print ("you sleep") #telling what you do if you say yes to sleep

    if sleep == "no": #making no an answer to sleep
        print ("you do homework") #telling what you do if you say no to sleep

