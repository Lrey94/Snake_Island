import sys
import random

random_number = random.randint(1, 100)
guesses = 0
print("I have set a random number between 1 and 99. Try to guess this number in 3 attempts")

user_guess_input = input("Enter your guess")
user_guess = int(user_guess_input)

while guesses < 2:
    if user_guess == random_number:
        print("That's right! Well Done!!")
        sys.exit()
    else:
        user_guess_input = input("Enter your guess")
        user_guess = int(user_guess_input)
        guesses = guesses + 1
        
if guesses >= 2 and user_guess > random_number:
    difference = user_guess - random_number
    print("Sorry, you didnt guess the number correctly, You were", difference, "off the random number.")
else:
    difference = random_number - user_guess
    print("Sorry, you didnt guess the number correctly, You were", difference, "off the random number.")
sys.exit

   
        
    

