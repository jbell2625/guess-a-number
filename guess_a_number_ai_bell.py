#Guess-A-Number AI
#
#Jake Bell
#September 1, 2016

import random

def start_screen():
    print("            .___________. __    __   __  .__   __.  __  ___      ______    _______         ___         .__   __.  __    __  .___  ___. .______    _______ .______      ")
    print("             |           ||  |  |  | |  | |  \ |  | |  |/  /     /  __  \  |   ____|       /   \        |  \ |  | |  |  |  | |   \/   | |   _  \  |   ____||   _  \    ") 
    print("             `---|  |----`|  |__|  | |  | |   \|  | |  '  /     |  |  |  | |  |__         /  ^  \       |   \|  | |  |  |  | |  \  /  | |  |_)  | |  |__   |  |_)  |    ")
    print("                 |  |     |   __   | |  | |  . `  | |    <      |  |  |  | |   __|       /  /_\  \      |  . `  | |  |  |  | |  |\/|  | |   _  <  |   __|  |      /     ")
    print("                 |  |     |  |  |  | |  | |  |\   | |  .  \     |  `--'  | |  |         /  _____  \     |  |\   | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\  \----. ")
    print("                 |__|     |__|  |__| |__| |__| \__| |__|\__\     \______/  |__|        /__/     \__\    |__| \__|  \______/  |__|  |__| |______/  |_______|| _| `._____| ")
                                                                                                                                                               
def play():

    low = 1
    high = 100
    guess = 50
    tries = 0

    print("Welcome to Numberguesser!")
    print("Please enter your name")
    name = input()
    
    print("Ok " + name +  " think of any number you want from ",low," to ",high,", and I will try to guess it.")

    input("Once you have your number, press Enter to begin")

    print("Type higher or lower to show how your number is related to the guess, and yes if I get it right.")

    print("Ok, " + name + " I guess that your number is " + str(guess) + ", is your number higher, lower, or have I guessed correctly?")
    a = input()



    while a != 'yes' or a != 'y':


            if a =='lower' or a == 'down':
                high = guess - 1
                guess = (low + high) // 2
                print("Ok, " + name + " I guess that your number is " + str(guess) + ", is your number higher, or lower, or have I guessed correctly?")
                a = input()
                tries += 1
                
            if a =='higher' or a == 'up':
                low = guess + 1
                guess = (low + high) // 2
                print("Ok, " + name + " I guess that your number is " + str(guess) + ", is your number higher, or lower, or have I guessed correctly?")
                a = input()
                tries += 1
                
            if a == 'yes' or a == 'y':
                print("I got it " + name + " ! That was too easy.")
                print("It took me " + str(tries) + " times.")
                print("game over")
                break
                
def credit_screen():
        time = 0




start_screen()
play()
credit_screen()

