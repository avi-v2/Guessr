import random
import pygame
import os
pygame.init()
pygame.mixer.init()
def play_sound(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    
def winsound():
    play_sound("w.wav")

def losesound():
    play_sound("l.wav")

attempts=0
def check():
    target = (random.randint(1,100))
    global attempts
    attempts=0
    while True: 
        try:
            inp=int(input("Enter your guess:  "))
            attempts+=1
            if inp==target:
                print("You won!")
                print(f"attempts={attempts}")
                winsound()
                break
            elif inp< target:
                losesound()
                print ("Target is larger than your guess.")
            elif inp> target:
                losesound()
                print ("Target is smaller than your guess.")
       
        except ValueError :
            print("Invalid input")   
            
while True:
    check()
    try:
        a=int(input("Press 1 to play again or any other key to quit:  "))

        if a!=1:
            print("Bye Bye")
            break
    except ValueError:
        print("Bye Bye")
        break