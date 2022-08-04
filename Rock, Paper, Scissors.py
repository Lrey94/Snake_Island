import random
import sys

user_choice = input("Make your selection: (rock, paper, scissors)")
RPS = ["rock", "paper", "scissors"]
computer_choice = random.choice(RPS)

print("Welcome to Rock, Paper, Scissors! Try and beat me")

if user_choice == computer_choice:
    print("It's a tie! We both selected", user_choice)
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("rock smashes scissors! You Win!")
    else:
        print("paper covers rock! You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("rock covers paper! You Win!")
    else:
        print("scissors cut paper! You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("scissors cut paper! You win!")
    else:
        print("rock smashes scissors! You lose.")
    

