'''This files is to set up the assistant requirement.'''
import time
import pyautogui

def command_prompt():
    pyautogui.hotkey('win','r')
    pyautogui.typewrite('cmd\n')

def all_libraries():
    pyautogui.typewrite('pip install speechrecognition\n')
    pyautogui.typewrite('pip install webbrowser\n')
    pyautogui.typewrite('pip install wikipedia\n')
    pyautogui.typewrite('pip install pyttsx3\n')

command_prompt()
time.sleep(0.5)
all_libraries()
