'''This module take care of general functions.'''
import navigator
import pyautogui
import time
import os
#This is for speacial cases.
import speak

#This class deal with the change in the volume
class volume_change:
    def volumedown():
        pyautogui.press('volumedown')

    def volumeup():
        pyautogui.press('volumeup')

    def volumemute():
        pyautogui.press('volumemute')

    def volume(status, query):
        if 'mute' in query:
            volume_change.volumemute()
            status = False
        else:            
            for i in range(5):
                if ('down' in query) or ('decrease' in query):
                    volume_change.volumedown()
                elif ('up' in query) or ('increase' in query):
                    volume_change.volumeup()
            status = False

        return status


#This function is to type the command.
def typewrite(query):
    pyautogui.typewrite(query[5:])
    return False

def go_home():
    width, height = pyautogui.size()
    pyautogui.click(width-2, height-2)
    return False

#This function shutdown system
def shut():
    speak.speak('Bye Aniket')
    os.system("shutdown /s /t 1")
    return False

#This function restart system
def restart():
    speak.speak('Restarting the system')
    os.system("shutdown /r /t 1")
    return False

    
#This function deal with the size of the screen and closing it.
def screen(status, query):
    pyautogui.hotkey('alt','space')
    screen_func = {'close':5, 'maximize':4, 'minimize':3}
    #Variable to declare no of steps taken
    steps = 0
    for key in screen_func:
        if key in query:
            steps = screen_func[key]

    if steps != 0:
        for i in range(steps):
            pyautogui.press('down')
        time.sleep(0.1)
        pyautogui.press('enter')
        status = False
    
    return status


#Function to check whether query is for basic functionality or not.
def basic_func(status, query):
    try:
        #print('Entered basic function')
        if 'volume' in query:
            status = volume_change.volume(status, query)
        elif 'type' in query:
            status = typewrite(query)
        elif 'screen' in query:
            status = screen(status, query)
        elif 'window' in query:
            status = screen(status, query)
        elif 'home' in query:
            status = go_home()
        elif 'shutdown' in query:
            status = shut()
        elif 'restart' in query:
            status = restart()
        elif 'navigator' in query:
            navigator.main()
            status = False
            
        #print('Leaving basic function')
    except:
        print('Error in basic function')

    message = ' '
    return message, status
