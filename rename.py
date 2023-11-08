import os

# Path to the dataset folder
dataset_folder = '/Users/tai/project for everything/hand_lang/dataset'

# Iterate through each folder (class 1 to class 11)
for class_folder in os.listdir(dataset_folder):
    class_folder_path = os.path.join(dataset_folder, class_folder)
    if os.path.isdir(class_folder_path):
        # Iterate through each file in the class folder and rename them
        file_list = os.listdir(class_folder_path)
        for i, filename in enumerate(file_list):
            file_extension = os.path.splitext(filename)[1]  # Extract file extension
            new_filename = f'image{str(i + 1).zfill(4)}{file_extension}'  # Rename format: image0001, image0002, ...
            old_filepath = os.path.join(class_folder_path, filename)
            new_filepath = os.path.join(class_folder_path, new_filename)
            os.rename(old_filepath, new_filepath)
