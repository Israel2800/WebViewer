from PIL import ImageGrab
import keyboard

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
    region = input("Press Enter after selecting the region.")
    return region

def ask_questions():
    """Ask questions to store the screenshot."""
    module = input("Module? ")
    lesson = input("Lesson? ")
    return module, lesson

def main():
    print("Press f5 to take a screenshot.")
    while True:
        if keyboard.is_pressed('f5'):
            screenshot = take_screenshot()
            region = select_region(screenshot)
            if region:
                module, lesson = ask_questions()
                filename = f"{module}_{lesson}.png"
                screenshot.save(filename)
                print(f"Screenshot saved as '{filename}'")
            break

if __name__ == "__main__":
    main()
