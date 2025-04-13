# main.py
# Bulk Image Resizer 

# Imports the Image module from the Pillow Library
# Allows the user to open, manipulate, and inspect image files
from PIL import Image

# The main function that will run when the script is executed
def main():
    try:
        image_path = input("Enter the path to your image file: ") # Asks the user for the path to an image file
        img = Image.open(image_path) # Opens the image using Pillow
        
        # Prints confirmation that the Image was opened, pulls relevant qualities of image, and displays them
        print(f"Image loaded successfully: {image_path}") # Confirmation 
        print(f"Format: {img.format}") #format type (JPEG, PNG, etc.)
        print(f"Size: {img.size}")  # Size of image (Ex: 1920 x 1080)
        print(f"Mode: {img.mode}") # The "mode" (e.g. RGB, Greyscale, etc)

    # Prints error message if the image file is not found 
    except Exception as e:
        print(f" Failed to load image: {e}")

if __name__ == "__main__":
    main()
