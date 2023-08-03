import pyautogui
import keyboard

def take_screenshot():
    """Take a screenshot of the screen."""
    print("Click and drag to select the region for the screenshot.")
    region = pyautogui.screenshot()
    return region

def ask_questions():
    """Ask questions to store the screenshot."""
    module = input("Module? ")
    lesson = input("Lesson? ")
    return module, lesson

def main():
    print("Press CTRL + S to take a screenshot.")
    while True:
        if keyboard.is_pressed('ctrl+s'):
            screenshot = take_screenshot()
            module, lesson = ask_questions()
            filename = f"{module}_{lesson}.png"
            screenshot.save(filename)
            print(f"Screenshot saved as '{filename}'")
            break

if __name__ == "__main__":
    main()
