# main.py
# Bulk Image Resizer 

# Imports the Image module from the Pillow Library
# Allows the user to open, manipulate, and inspect image files/files
import os
import glob
from PIL import Image

#Image resizing functionality 
def resize_images(images):
    if not images:
        print("There are not images to resize. Please try again")
        return
    try:
        new_width = int(input("Enter the desired width: "))
        new_height = int(input("Enter the desired height: "))
    except ValueError:
        print("Invalid input. Please enter whole numbers then try again.")
    
    for img_info in images:
        path = img_info["path"]
        img = img_info["image"]
        print(f"\nResizing: {os.path.basename(path)}")
        print(f"Original Size: {img.size}")
        resized_img = img.resize((new_width, new_height))
        print(f"Resized to: {resized_img.size}")
        img_info["resized"] = resized_img

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

# Asks the user to choose option 1 (single image processing) or option 2 (bulk image processing) and calls the corresponding function
 print("Choose an option:")
    print("1 - Process a single image file")
    print("2 - Process images in a folder (bulk processing)")

    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        image_list = process_single_image()
        resize_images(image_list)
    elif choice == '2':
        image_list = process_folder_images()
        resize_images(image_list)
    else:
        print("Invalid input. Please select one of the given options.")
        
if __name__ == "__main__":
    main()
