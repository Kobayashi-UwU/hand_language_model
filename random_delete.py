import os
import random

def delete_two_thirds_of_images(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid directory path.")
        return

    files = os.listdir(folder_path)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    num_images = len(image_files)

    if num_images == 0:
        print("No image files found in the directory.")
        return

    num_images_to_delete = num_images * 7 // 10
    images_to_delete = random.sample(image_files, num_images_to_delete)

    for image in images_to_delete:
        image_path = os.path.join(folder_path, image)
        os.remove(image_path)
        print(f"Deleted: {image}")

# Replace 'folder_path' with the path to your folder containing images
folder_path = '/Users/tai/project for everything/hand_lang/dataset for roboflow/'
delete_two_thirds_of_images(folder_path)
