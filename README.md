# CopyX

CopyX types the text currently in your clipboard into the active code editor.

## Run without installing Python

1. Download `copyx-windows.zip` from GitHub.
2. Extract the ZIP file.
3. Double-click `copyx.exe`.
4. Copy your code, click the target editor, and press **Ctrl+Q**.

The executable already contains Python and the required packages. No Python, pip, or other installation is required.

The program waits in the background until **Ctrl+Q** is pressed. Close its console window to stop it.

## Source version

`copyx.py` is included as the source code. Running the source directly requires Python and the packages listed below:

```text
keyboard
pyautogui
pyperclip
```

## Supported platform

The included executable is built for 64-bit Windows. It is not a macOS or Linux executable.
