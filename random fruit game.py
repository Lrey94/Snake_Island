import sys
import random

WORDS = ["orange", "banana", "apple", "kiwi", "passionfruit", "pear"]
random_word = random.choice(WORDS)
guesses = 0
correct = random_word

print("I have selected a fruit at random. Try to guess the fruit in 3 attempts")

user_guess = input("Enter your guess")

while guesses < 2:
    if user_guess == correct:
        print("Thats right! Well done! Thanks for playing.")
        break
    else:   
        print("Sorry, thats not correct")
        user_guess = input("Try Again:")
        guesses = guesses + 1
 
if guesses >= 2:
    print("Sorry, you've had too many guesses. Better luck next time")
    sys.exit





    
    
    
    
    
