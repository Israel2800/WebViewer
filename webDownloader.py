from PIL import ImageGrab
import keyboard
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
                folder_path = choose_folder()
                if folder_path:
                    filename = f"{module}_{lesson}.png"
                    region.save(folder_path + "/" + filename)
                    print(f"Screenshot saved as '{filename}' in '{folder_path}'")
            break

if __name__ == "__main__":
    main()
