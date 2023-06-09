import cv2
from keras.models import load_model
import numpy as np
import random
import time

def get_prediction(image, model):
    """
    This function calculates the prediction for an image and returns it.
    Args:
        image (np.ndarray): image to get predict
        model (Model): A Tensorflow Keras model that makes the prediction on the image

    Returns:
        choice (str): string value, "rock", "paper", "scissors" or "nothing"
    """
    prediction = model.predict(image)

    # get index of the highest probability
    max_idx = np.argmax(prediction[0])

    if max_idx == 0:
        return "nothing"
    elif max_idx == 1:
        return "rock"
    elif max_idx == 2:
        return "paper"
    elif max_idx == 3:
        return "scissors"
    
def get_computer_choice():
    """
    This function returns a random choice. either rock, paper or scissors.
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

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
        return tie
    elif computer_choice == "rock" and user_choice.lower() == "paper":
        return player_wins
    elif computer_choice == "rock" and user_choice.lower() == "scissors":
        return computer_wins
    elif computer_choice == "paper" and user_choice.lower() == "rock":
        return computer_wins
    elif computer_choice == "paper" and user_choice.lower() == "paper":
        return tie
    elif computer_choice == "paper" and user_choice.lower() == "scissors":
        return player_wins
    elif computer_choice == "scissors" and user_choice.lower() == "rock":
        return player_wins
    elif computer_choice == "scissors" and user_choice.lower() == "paper":
        return computer_wins
    elif computer_choice == "scissors" and user_choice.lower() == "scissors":
        return tie
    elif computer_choice == "rock" and user_choice.lower() == "nothing":
        return tie
    elif computer_choice == "paper" and user_choice.lower() == "nothing":
        return tie
    elif computer_choice == "scissors" and user_choice.lower() == "nothing":
        return tie
    
def print_final_results(computer_wins, user_wins):
    """
    This function prints the result of the game.
    Args:
        computer_wins (int): The number of times computer has won
        user_wins (int): The number of times user has won
    """
    final_score = f"computer has won {computer_wins} rounds.\nplayer has won {user_wins} rounds."
    print("THE GAME IS OVER!")
    if computer_wins == 3:
        print(final_score)
        print("Computer has won the game.")

    elif user_wins == 3:
        print(final_score)
        print("Player has won the game. CONGRATULATIONS!!!")

def play():
    """
    This function simulates the game of rock, paper and scissors. Finally, it prints the winner.
    """
    # load the model
    model = load_model("keras_model.h5")

    # start the webcam
    cap = cv2.VideoCapture(0)

    # setup initial wins for computer and user
    computer_wins = 0
    user_wins = 0

    # set start time
    start_time = time.time()

    while True:
        # read the frame
        ret, frame = cap.read()
        # show the frame in a window
        cv2.imshow('frame', frame)

        # set the end time
        end_time = time.time()
        # calculate how many seconds have passed
        elapsed_time = end_time - start_time

        # if 3 seconds have passed 
        if elapsed_time > 3:
            # reset the start time
            start_time = end_time

            # prepare the image
            data = np.ndarray(shape=(1,224,224,3), dtype=np.float32)
            resized_frame = cv2.resize(frame, (224,224), interpolation=cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
            data[0] = normalized_image

            # get user choice as prediction from model
            prediction = get_prediction(data, model)
            print(f"you chose {prediction}.")

            # get computer choice
            computer_choice = get_computer_choice()
            print(f"computer chose {computer_choice}.")

            # print the winner
            winner = get_winner(computer_choice, prediction)
            print(winner)
            print('\n')

            # track computer and user wins
            if winner.lower() == "you lost":
                computer_wins += 1
            elif winner.lower() == "you won!":
                user_wins += 1

            # if either user or computer has won 3 times, the game is over!
            if computer_wins == 3 or user_wins == 3:
                print_final_results(computer_wins, user_wins)
                break

        # if key q is pressed quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    play()