from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import os
import numpy as np
from PIL import Image
import cv2


# Function to apply blur to images
def apply_blur(image):
    blurred = cv2.GaussianBlur(image, (5, 5), 0)  # You can adjust the kernel size for the blur effect
    return blurred

# Path to the folder containing the original images
original_images_folder = '/Users/tai/project for everything/hand_lang/teachable_mode/augmentation_dataset/working-samples'

# Initialize ImageDataGenerator with augmentation configurations
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    brightness_range=[0.5, 1.5],
    channel_shift_range=50,
    preprocessing_function=apply_blur
)

# Retrieve the list of filenames of images in the folder
images_list = os.listdir(original_images_folder)

# Iterate through each image in the folder and apply augmentation
for image_name in images_list:
    image_path = os.path.join(original_images_folder, image_name)
    try:
        img = Image.open(image_path)  # Attempt to open the image
        x = np.array(img)  # Convert the image to a numpy array

        x = x.reshape((1,) + x.shape)  # Reshape the image

        # Generate augmented images and save to the same folder
        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir=original_images_folder, save_prefix='aug', save_format='jpeg'):
            i += 1
            if i >= 5:  # Generate and save 5 augmented images for each original image
                break  # Break the loop to move to the next original image

    except Exception as e:
        print(f"Error processing {image_name}: {e}")