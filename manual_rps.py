import random

def get_computer_choice():
    """
    This function returns a random choice. either rock, paper or scissors.
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    """
    This function asks the user to enter their choice from either rock, paper or scissors and returns it.
    """
    choice = input("Please pick between rock, paper and scissors: ")
    return choice

def get_winner(computer_choice, user_choice):
    """
    This function decides the winner.
    Args:
        computer_choice (str): The choice of the computer.
        user_choice (str): The choice of the user.
    """
    computer_wins = "You lost"
    player_wins = "You won!"
    tie = "It is a tie!"
    if computer_choice == "rock" and user_choice.lower() == "rock":
        print(tie)
    elif computer_choice == "rock" and user_choice.lower() == "paper":
        print(player_wins)
    elif computer_choice == "rock" and user_choice.lower() == "scissors":
        print(computer_wins)
    elif computer_choice == "paper" and user_choice.lower() == "rock":
        print(computer_wins)
    elif computer_choice == "paper" and user_choice.lower() == "paper":
        print(tie)
    elif computer_choice == "paper" and user_choice.lower() == "scissors":
        print(player_wins)
    elif computer_choice == "scissors" and user_choice.lower() == "rock":
        print(player_wins)
    elif computer_choice == "scissors" and user_choice.lower() == "paper":
        print(computer_wins)
    elif computer_choice == "scissors" and user_choice.lower() == "scissors":
        print(tie)

def play():
    """
    This function simulates the game of rock, paper and scissors.
    """
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    return get_winner(computer_choice, user_choice)

if __name__ == "__main__":
    play()