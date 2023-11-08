import os
import shutil
import random

# Directory where your dataset is located
dataset_dir = '/Users/tai/project for everything/hand_lang/extreme_dataset/dataset'
train_dir = '/Users/tai/project for everything/hand_lang/extreme_dataset/train'
validation_dir = '/Users/tai/project for everything/hand_lang/extreme_dataset/validation'
test_dir = '/Users/tai/project for everything/hand_lang/extreme_dataset/test'

# Make directories for train, validation, and test sets if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(validation_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Define the ratio for splitting the data
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

for class_folder in os.listdir(dataset_dir):
    class_path = os.path.join(dataset_dir, class_folder)
    if not os.path.isdir(class_path):
        continue  # Skip non-directory items

    images = os.listdir(class_path)
    random.shuffle(images)
    
    num_images = len(images)
    num_train = int(train_ratio * num_images)
    num_val = int(val_ratio * num_images)

    train_images = images[:num_train]
    val_images = images[num_train:num_train + num_val]
    test_images = images[num_train + num_val:]

    # Move images to the respective directories (train, validation, test)
    for img in train_images:
        src = os.path.join(class_path, img)
        dst = os.path.join(train_dir, class_folder, img)
        os.makedirs(os.path.join(train_dir, class_folder), exist_ok=True)
        shutil.copy(src, dst)

    for img in val_images:
        src = os.path.join(class_path, img)
        dst = os.path.join(validation_dir, class_folder, img)
        os.makedirs(os.path.join(validation_dir, class_folder), exist_ok=True)
        shutil.copy(src, dst)

    for img in test_images:
        src = os.path.join(class_path, img)
        dst = os.path.join(test_dir, class_folder, img)
        os.makedirs(os.path.join(test_dir, class_folder), exist_ok=True)
        shutil.copy(src, dst)
