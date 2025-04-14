# main.py
# Bulk Image Resizer 

# Imports the Image module from the Pillow Library
# Allows the user to open, manipulate, and inspect image files/files
import os
import glob
from PIL import Image

#Creates def function to load single image and displays its attributes
def process_single_image():
    try:
        image_path = input("Enter the path to your image file: ")
        img = Image.open(image_path)
        print(f"Image loaded successfully: {image_path}")
        print(f"Format: {img.format}")
        print(f"Size: {img.size}")
        print(f"Mode: {img.mode}")
    except Exception as e:
        print(f"Failed to load image: {e}")

#Creates def function that allows "bulk" image recognition and the image(s) attributes
def process_folder_images():
    try:
        folder_path = input ("Enter the folder containing the images: ")
        if not os.path.isdir(folder_path):
            print ("The folder was not found. Please try again: ")
            return
        image_format = ('*.png', '*.jpg', '*.jpeg')
        image_files = []
        for ext in image_format:
            image_files.extend(glob.glob(os.path.join(folder_path, ext)))
        if not image_files:
            print ("No images found in folder.")
            return 
        
        print(f"\nFound {len(image_files)} image(s): \n")
        for file_path in image_files:
            try:
                img = Image.open(file_path)
                print(f"Image: {os.path.basename(file_path)}")
                print(f"Format: {img.format}")
                print(f"Size: {img.size}")
                print(f"Mode: {img.mode}")
            except Exception as e:
                print(f"Could not open {file_path}: {e}")
    except Exception as e:
        print(f"An error occured while atempting to process the folder: {e}")    


def main():


if __name__ == "__main__":
    main()
