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


def main():


if __name__ == "__main__":
    main()
