
import time
import keyboard
import pyautogui
import pyperclip

print("Copy your code first.")
print("Open the target website and click its code editor.")
print("Press Ctrl+Q to type the copied code.")

def type_code():
    code = pyperclip.paste()
    if not code.strip():
        print("Clipboard is empty!")
        return

    print("Typing starts in 3 seconds...")
    time.sleep(3)

    # Type line by line to preserve indentation
    for line in code.splitlines():
        pyautogui.write(line, interval=0.001)
        pyautogui.press("enter")

keyboard.add_hotkey("ctrl+q", type_code)

print("Ready. Press Ctrl+Q when your cursor is in the editor.")
keyboard.wait()

# python copyx.py