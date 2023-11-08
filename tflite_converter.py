import tensorflow as tf

# Load your TensorFlow model
model = tf.keras.models.load_model('/Users/tai/project for everything/hand_lang/MobileNetV2_10epoch_with_extremedata.h5')  # Example, replace 'your_model.h5' with your model file

# Convert the model to TFLite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model to a file
with open('/Users/tai/project for everything/hand_lang/final_model/model4.tflite', 'wb') as f:
    f.write(tflite_model)
