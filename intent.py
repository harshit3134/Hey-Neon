import webbrowser
import pyautogui
import subprocess
import json

def open_website(*args):
    for url in args:
        webbrowser.open(url)
    return None


def simulate_key_press(*args):
    pyautogui.hotkey(*args)
    return None


def open_application(command):
    subprocess.Popen(command, shell=True)
    return None

# if __name__ == "__main__":
#     open_website("https://www.google.com", "https://www.youtube.com")
#     simulate_key_press("win", "shift", "T") 
#     open_application("notepad")
