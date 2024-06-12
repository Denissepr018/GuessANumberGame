from random import randint
from art import logo
#Global Variables

EASY_LEVEL = 10
HARD_LEVEL = 5

#Checking the users guess vs answer 
def check_guess(guess, answer, turns):
    """Checks answer against guessed. Returns the number of turns remaining"""
    if guess > answer:       
        print("Guess is too high!")
        return turns -1 
        
    elif guess < answer:
        print("Guess is too low!")
        return turns -1 
    else: 
        print (f"You Got it the answer was  {answer}")

#Make a fuction to set game dificulty
def set_gameDificulty():
    level = input("Choose game mode 'easy' or 'hard'")
    if level =="easy": 
        return EASY_LEVEL
    else: 
        return HARD_LEVEL

#Choosing a random number from 0 100
def game(): 
 print(logo)
 print("Welcome, this a number guessing game!")
 print("I am thinking of a number between 1 and 100")

 answer = randint(1, 100)

 turns = set_gameDificulty()
 
 #print(f"The correct answer is {answer}")

 #Make a guess

 #Repeat guessing game fucntionality if number has not been guessed and still attempt available
 guess = 0
 while guess != answer:
  print(f"You have {turns} attemps remaining.")
  guess = int(input("Make a Guess: "))
  turns = check_guess(guess, answer, turns)
  if turns == 0:
   print("You ran out of guesses!!!")
   return
  elif guess != answer:
     print("Try Again!")

game()

