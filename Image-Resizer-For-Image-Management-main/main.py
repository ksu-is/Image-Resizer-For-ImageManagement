from PIL import Image
import os
import glob

# Image resizing functionality
def resize_images(images):
    if not images:
        print("There are no images to resize. Please try again.")
        return
    try:
        new_width = int(input("Enter the desired width: "))
        new_height = int(input("Enter the desired height: "))
    except ValueError:
        print("Invalid input. Please enter whole numbers.")
        return

    for img_info in images:
        path = img_info["path"]
        img = img_info["image"]
        print(f"\nResizing: {os.path.basename(path)}")
        print(f"Original Size: {img.size}")
        resized_img = img.resize((new_width, new_height))
        print(f"Resized to: {resized_img.size}")
        img_info["resized"] = resized_img

# Create and save resized image(s) into a new folder
def save_resized_images(images):
    if not images:
        print("There are no images to save.")
        return
    resized_images = [img for img in images if "resized" in img]
    if not resized_images:
        print("No resized images found. Please resize images before saving.")
        return

    save_folder = input("Enter the name of the destination folder for saved images: ")
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for img_info in resized_images:
        original_name = os.path.basename(img_info["path"])
        name_no_ext, ext = os.path.splitext(original_name)
        save_path = os.path.join(save_folder, f"{name_no_ext}_resized{ext}")

        try:
            img_info["resized"].save(save_path)
            print(f"Saved as: {save_path}")
        except Exception as e:
            print(f"Failed to save {original_name}: {e}")

# Load single image and return attributes
def process_single_image():
    try:
        image_path = input("Enter the path to your image file: ")
        img = Image.open(image_path)
        print(f"Image loaded successfully: {image_path}")
        print(f"Format: {img.format}")
        print(f"Size: {img.size}")
        print(f"Mode: {img.mode}")
        
        return [{"path": image_path, "image": img}]
    
    except Exception as e:
        print(f"Failed to load image: {e}")
        return []

# Load folder of images and return list of image attributes
def process_folder_images():
    try:
        folder_path = input("Enter the folder containing the images: ")
        if not os.path.isdir(folder_path):
            print("The folder was not found. Please try again.")
            return []

        image_format = ('*.png', '*.jpg', '*.jpeg')
        image_files = []
        for ext in image_format:
            image_files.extend(glob.glob(os.path.join(folder_path, ext)))
        if not image_files:
            print("No images found in folder.")
            return []

        print(f"\nFound {len(image_files)} image(s):\n")
        loaded_images = []
        for file_path in image_files:
            try:
                img = Image.open(file_path)
                print(f"Image: {os.path.basename(file_path)}")
                print(f"Format: {img.format}")
                print(f"Size: {img.size}")
                print(f"Mode: {img.mode}")
                loaded_images.append({"path": file_path, "image": img})
            except Exception as e:
                print(f"Could not open {file_path}: {e}")
        return loaded_images

    except Exception as e:
        print(f"An error occurred while attempting to process the folder: {e}")
        return []

# Main function
def main():
    print("Bulk Image Resizer starting...\n")
    print("Choose an option:")
    print("1 - Process a single image file")
    print("2 - Process images in a folder (bulk processing)")

    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        image_list = process_single_image()
        resize_images(image_list)
        save_resized_images(image_list)
    elif choice == '2':
        image_list = process_folder_images()
        resize_images(image_list)
        save_resized_images(image_list)
    else:
        print("Invalid input. Please select either option 1 or 2.")

if __name__ == "__main__":
    main()
