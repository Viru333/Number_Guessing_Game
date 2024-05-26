import random
import os

def clear():
    os.system('cls')

from logo import logo
def play_game():

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    chosen_number = random.randint(1,100)
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy": attempts = 10
    else: attempts = 5

    while(attempts > 0):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number = input("Make a guess: ")
        guessed_number = int(guessed_number)

        if guessed_number == chosen_number:
            print(f"You got it right! The answer was {chosen_number}.")
            break

        elif guessed_number > chosen_number:
            print("Too high. \n Guess again.")

        else:
            print("Too low. \n Guess again.")
        
        attempts -= 1
    
    if attempts == 0:
        print(f"You have run out of guesses, you lose. The answer was {chosen_number}.")
    
    play = input("Do you want to play another game? Type 'yes' or 'no': ")
    if play == "yes":
        clear()
        play_game()
    else:
        return


play_game()
