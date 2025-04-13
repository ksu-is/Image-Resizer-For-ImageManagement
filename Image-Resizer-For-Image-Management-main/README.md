 My project will allow the user to alter the dimensions of their image within Pyt
 The goal is to create a useful tool that helps users efficiently prepare images for use in presentations, documents, or web uploads.
 
 #Features
 - Resizes several images in one batch
 - Maintain image quality during size reduction
 - Edit images to user specific dimensions
 - Saves resized images to a seperate folder
 - Resizes several images in one batch. 
 - Maintain image quality during size reduction. 
 - Edit images to user specific dimensions. 
 - Saves resized images to a seperate folder. 
 
 #Uses
 >Python 3, 
 >Pillow (Python Imaging Library)
>

## Setup Instructions

This program was created using Python 3 and Visual Studio Code (VS Code).  
The steps below will walk you through how to install what you need, add an image, and run the program successfully.

### 1. What You’ll Need

- Python 3 installed on your computer  
- Visual Studio Code installed  
- An internet connection (just for setup)

### 2. Install the Pillow Library

This program needs something called the Pillow library to work with image files.
To install it:
1. Open VS Code  
2. Open the terminal in VS Code by clicking **View > Terminal** (or press `Ctrl + ` key)
3. In the terminal box at the bottom, type this and press Enter:

```
pip install pillow
```
Wait a moment while it installs. You're good to go when it says `Successfully installed pillow`.
---
### 3. Add an Image to the Right Place

This program expects your image file to be in the **same folder** as the file named `main.py`.
To do that:
1. In VS Code, with `main.py` open, right-click the tab at the top  
2. Click **“Reveal in File Explorer”**  
3. A folder window will open — this is where your program lives  
4. Drag and drop your image file (like `test.png`) into this folder
   
> Important: Make sure your image file is really named `test.png` and **not** `test.png.png`  
> To check, turn on **file name extensions** in File Explorer:  
> Click **View > File name extensions** and make sure it’s checked
---
### 4. Run the Program
1. In VS Code, open the terminal again  
2. In the terminal, type this and press Enter:

```
python main.py
```
3. When the program asks for your image file name, type:
```
test.png
```
(or whatever your image file is named)
---
### 5. What You’ll See
If it works, the program will tell you:
- That the image was loaded successfully
- What kind of file it is (PNG, JPEG, etc.)
- The image’s width and height
- What color mode it uses (like RGB or grayscale)
Example:
```
Image loaded successfully: test.png
Format: PNG
Size: (1920, 1080)
Mode: RGBA
```
### Need Help?

- If it says `No module named 'PIL'`, go back and repeat **Step 2**
- If it says `No such file or directory`, check that:
  - Your image is in the same folder as `main.py`
  - The file name is typed exactly right

---

This setup only needs to be done once. After that, you can run the program any time to load and check image files.

