#!/usr/bin/env python3

import utils

utils.check_version((3,7))
utils.clear()
#All the print statements answer questions from the README
print("Hello, my name is Adhiraj Singh and I am a junior at IU majoring in CS.")
print("My main concern for this class is being able to apply what I learn to something outside the classroom since I have never made a game on my own.")
print("I'm excited to learn a lot of new things to add to my game development skills including new engines and actual coding with games which I'm yet to do.")
print("My StackOverflow number is 11985201 and the url to my profile is https://stackoverflow.com/users/11985201/adhirajs?tab=profile")
print("My github can be found at https://github.com/adsing99")
print("To figure out my favourite game we can play a short guessing game:")

guess = '' #Set the guesses to empty strings
guess2 = ''

while (guess != "Z") or (guess2 != "Zelda"): #Loop must keep going until the game is guessed
    guess = input("Guess what letter it starts with, your options are A, M, and Z ") #Ask for an input letter
   
    if (guess == "Z"): 
        guess2 = input("Nice! Second Hint: Nintendo Game that includes a character named Link ") #Ask for the title of the game
        if (guess2 == "Zelda"):
            print("You got it! Breath of the Wild is my favorite game, although Marvel's Spider-man is a close second.")
            break
        else:
            print("Try again! It's 5 letters") #If they don't get it correct the loop continues after this message and they can try again

    else:
        print("Try again!") #If they don't get it correct the loop continues after this message and they can try again
