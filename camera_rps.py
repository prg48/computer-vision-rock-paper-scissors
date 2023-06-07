import cv2
from keras.models import load_model
import numpy as np

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

if __name__ == "__main__":
    model = load_model("keras_model.h5")
    # start the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # read the frame
        ret, frame = cap.read()
        # show the frame in a window
        cv2.imshow('frame', frame)

        # if key p is pressed
        if cv2.waitKey(1) & 0xFF == ord('p'):
            # prepare the image
            data = np.ndarray(shape=(1,224,224,3), dtype=np.float32)
            resized_frame = cv2.resize(frame, (224,224), interpolation=cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
            data[0] = normalized_image

            # get prediction
            prediction = get_prediction(data, model)
            print(prediction)

        # if key q is pressed quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()