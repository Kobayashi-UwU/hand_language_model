import cv2
import numpy as np
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential, load_model

# 1 = background 2 4
# 2 = stand 4 bad
# 3 = bad 1 2 3
# 4 = good 3 bad
# 5 = angry 1 2 3 4
# 6 = hungry 1 2
# 7 = like 1 bad
# 8 = food 1 2 3
# 9 = look 1 2 3 4
# 10 = sit 1 2 3
# 11 = work 2 3 4

model_dic1 = {1:'good',3:'bad',2:'food',4:'angry',5:'like',6:'hungry',7:'sit',8:'working',9:'look',10:'stand',11:'background'}
model_dic2 = {5:'good',3:'bad',4:'food',1:'angry',7:'like',6:'hungry',9:'sit',11:'working',8:'look',10:'stand',2:'background'}


# Load your trained model
model1 = load_model('/Users/tai/project for everything/hand_lang/model/MobileNetV2_10epoch_with_finetune.h5')  # Replace with the path to your .h5 model file
model2 = load_model('/Users/tai/project for everything/hand_lang/model/MobileNetV2_20epoch_with_finetune.h5')  # Replace with the path to your .h5 model file
model3 = load_model('/Users/tai/project for everything/hand_lang/model/MobileNetV2_30epoch_with_finetune.h5')  # Replace with the path to your .h5 model file
model4 = load_model('/Users/tai/project for everything/hand_lang/MobileNetV2_10epoch_with_extremedata.h5')  # Replace with the path to your .h5 model file

# Define the function for processing the video feed
def process_frame(frame):
    # Preprocess the frame to match the input requirements of your model
    frame = cv2.resize(frame, (224, 224))  # Adjust dimensions as per your model
    frame = np.expand_dims(frame, axis=0)  # Add batch dimension
    frame = frame / 255.0  # Normalize the pixel values


    return frame

# Open a connection to the camera (in this case, the default camera)
video = cv2.VideoCapture(0)  # Change the parameter if you have multiple cameras

while True:
    ret, frame = video.read()  # Capture a frame
    if not ret:
        break

    frame_pro = process_frame(frame)

    # Perform prediction using your model
    predictions1 = model1.predict(frame_pro)
    predictions2 = model2.predict(frame_pro)
    predictions3 = model3.predict(frame_pro)
    predictions4 = model4.predict(frame_pro)

    # Get the class with the highest probability
    predicted_class1 = np.argmax(predictions1)
    predicted_class2 = np.argmax(predictions2)
    predicted_class3 = np.argmax(predictions3)
    predicted_class4 = np.argmax(predictions4)

    # Get the class labels
    label1 = model_dic1[predicted_class1 + 1]
    label2 = model_dic1[predicted_class2 + 1]
    label3 = model_dic1[predicted_class3 + 1]
    label4 = model_dic2[predicted_class4 + 1]

    # Display the predicted class labels on the frame
    cv2.putText(frame, f"Model 1: {label1}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Model 2: {label2}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Model 3: {label3}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Model 4: {label4}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame with class labels
    cv2.imshow('Real-time Camera', frame)

    # Exit the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video object and close windows
video.release()
cv2.destroyAllWindows()
