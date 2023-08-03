from PIL import ImageGrab
import keyboard
import os
from tkinter import filedialog, Tk

def take_screenshot():
    """Take a screenshot of the selected region on the screen."""
    print("Click and drag to select the region for the screenshot.")
    region = ImageGrab.grab(bbox=None)
    return region

def select_region(screenshot):
    """Prompt the user to select a region by clicking and dragging on the image."""
    image = screenshot.copy()
    image.show()
    print("Please click and drag to select the region. Press Enter when done.")
    input("Press Enter after selecting the region.")
    return screenshot

def ask_questions():
    """Ask questions to store the screenshot."""
    module = input("Module: ")
    lesson = input("Lesson: ")
    return module, lesson

def create_folder():
    """Create a folder inside the project path and return its path."""
    folder_name = input("Enter the name of the folder to create: ")
    folder_path = os.path.join(os.getcwd(), folder_name)
    os.makedirs(folder_path)
    print(f"Folder '{folder_name}' created.")
    return folder_path

def choose_folder():
    """Open a folder selection dialog and return the chosen folder path."""
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

def main():
    print("Press f5 to take a screenshot.")
    while True:
        if keyboard.is_pressed('f5'):
            screenshot = take_screenshot()
            region = select_region(screenshot)
            if region:
                module, lesson = ask_questions()
                print("Do you want to create a folder inside the project path? (y/n)")
                choice = input().lower()
                if choice == 'y':
                    folder_path = create_folder()
                else:
                    folder_path = choose_folder()
                if folder_path:
                    filename = input("Enter the name for the image: ") + ".png"
                    region.save(os.path.join(folder_path, filename))
                    print(f"Screenshot saved as '{filename}' in '{folder_path}'")
            break

if __name__ == "__main__":
    main()
