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
    elif computer_choice == "rock" and user_choice.lower() == "nothing":
        print(tie)
    elif computer_choice == "paper" and user_choice.lower() == "nothing":
        print(tie)
    elif computer_choice == "scissors" and user_choice.lower() == "nothing":
        print(tie)

def play():
    """
    This function simulates the game of rock, paper and scissors. Finally, it prints the winner.
    """
    # load the model
    model = load_model("keras_model.h5")

    # start the webcam
    cap = cv2.VideoCapture(0)

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

            # prints the winner
            get_winner(computer_choice, prediction)
            print('\n')

            # sleep for a second to check the result
            time.sleep(1)

        # if key q is pressed quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    play()