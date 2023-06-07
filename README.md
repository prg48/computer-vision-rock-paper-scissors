# Milestone 2
For milestone 2 of the project, an image recognition model was trained in [teacheable machine app](https://teachablemachine.withgoogle.com/) which allows users to train an image recognition model on the browser. Four classes were labeled namely rock, paper, scissors and nothing. The image samples for all classes were uniform, i.e. 46 images so that there is balance of sample images for each class. The hyperparameters for the training of the model were as follows:
* epoch: 80
* batch size: 16
* learning rate: 0.001

The trained model was downloaded on a tensorflow keras format and was named `keras_model.h5` and the labels for the model was downloaded on a text format and named `labels.txt`. The model will be used for prediction in the upcoming milestones for the rock, paper and scissor game. One way the model can be used for the game project is by using the OpenCV keras API. The game will involve the player with the webcam on and the computer. The computer will choose either rock, paper or scissor and the player will use the webcam to gesture the same. The game will use OpenCV API and the trained model to label the gesture of the player through the webcam and classify it as either rock, paper, scissor or nothing. Then, the game can decide who has won the game.
