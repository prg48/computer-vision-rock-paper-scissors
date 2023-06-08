import random

def get_computer_choice():
    """
    This function returns a random choice. either rock, paper or scissors.
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    """
    This function asks the user to enter their choice from either rock, paper or scissors. It validates the input and returns it.

    Returns:
    choice (str): input entered by the user.

    Raises:
    ValueError: If value is not either rock, paper, scissors or q; a ValueError with message "Please enter a valid input." is raised.
    """
    valid_choices = ["rock", "paper", "scissors", "q"]
    choice = input("Please pick between rock, paper or scissors: ")
    if choice.lower() in valid_choices:
        return choice.lower()
    else:
        raise ValueError("Please enter a valid input.")

def get_winner(computer_choice, user_choice):
    """
    This function decides the winner and prints the correct win statement.

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
    game_finish_str = "Thank you for playing rock, paper and scissors game.\nPlease visit again."

    print("Welcome to rock, paper and scissors game........................")
    print("To quit, press 'Ctrl + c'")
    print("OR")
    print("Enter 'q' and press return when asked to choose between rock, paper or scissors.......\n")
    while True:
        computer_choice = get_computer_choice()

        try:
            user_choice = get_user_choice()

            ## if user has entered 'q', quit the game
            if user_choice == 'q':
                print(game_finish_str)
                break
            print(f"You chose {user_choice}")
            print(f"Computer chose {computer_choice}")
            get_winner(computer_choice, user_choice)
            print()

        except ValueError:
            print("Please enter a valid input.\n")

        except KeyboardInterrupt:
            print("\n" + game_finish_str)
            break

if __name__ == "__main__":
    play()