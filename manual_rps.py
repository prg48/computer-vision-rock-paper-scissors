import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    choice = input("Please pick between rock, paper and scissors: ")
    return choice

if __name__ == "__main__":
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()