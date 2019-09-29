'''This is a voice navigator module that operates through voice.'''
import pyautogui as p
import string
import os
#import listen
#import speak

#This method is for returning to the previous path.
def go_back(path):
    #print('Entered go back function')
    while ( path[-1]!='\\' ):
        path = path[:-1]
    #print('Leaving go back function')
    return True, path[:-1]

#This method is to go on home page
def home():
    width, height = p.size()
    p.click(width-2, height-2)
    return False

#To find the path 
def find_file(path, query):
    print('Entered the system search function')
    all_files = os.listdir(path)
    print(all_files)
    print(query)
    for files in all_files:
        if query in files.lower():
            path = path + '\\' + files
            break

    print('Leaving the system search function')
    return True, path

#This method contains the basic instruction that are to be given.
def instruction(path, query):
    #print('Entered instruction')
    if 'go back' in query:
        status, path = go_back(path)
        
    elif 'drive' in query:
        all_drive = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        for drive in all_drive:
            if drive[:-1].lower() in query:
                path = drive
                status = True
                print(os.listdir(path))
                break;
        else:
            print('No such drive exist')
            path, status = '', 'Not Present'
            

    elif 'open' in query:
        print(query)
        status, path = find_file(path, query[5:].lower())

    elif 'close' in query:
        path, status = '', 'EXIT NAVIGATOR'

    else:
        print('This functionality is not present')
        path, status = '', 'Not Present'
    #print('Leaving Instruction')
    return path, status


def main():
    
    path = 'C:\\Users\\anike\\OneDrive\\Desktop\\Asus'
    os.startfile(path)
    
    while(True):
        try:
            query = input()
            path, status = instruction(path, query.lower())
            print(path)

            if status == True:
                #p.hotkey('alt','f4')
                os.startfile(path)
            elif status == False:
                print('File not found')
            elif status == 'EXIT NAVIGATOR':
                print('Exit Navigator')
                break
            else:
                print('Nothing found')
        except:
            print('Exception')

main()
