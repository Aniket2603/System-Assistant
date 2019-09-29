'''This module is for finding all the files present in the system and return it in the form a list
    This list contains all the files with the path of the file
'''
import os
import string
import speak
import listen

drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

db_files = []
db_folders = []

#This function collects all the files of the path given into folders and files
def collect_files(path):
    try:
        all_files = os.listdir(path)
        for i in all_files:
            if '.' in i:
                db_files.append(path+'\\'+i)
            else:
                db_folders.append(path)
                collect_files(path+'\\'+i)
    except:
        pass

    return db_folders,db_files

#This method is used to scan the complete system
def sys_find(file):
    #Variable to contain all the required paths
    all_required_files = []
    #Variable to check between files and folders
    check = True
    
    for i in drives:
        collect_files(i)

    if check is True:
        for i in db_folders:
            if file.lower() in i.lower():
                all_required_files.append(i)
                check = False

    if check is True:        
        for i in db_files:
            if file.lower() in i.lower():
                all_required_files.append(i)
        
    return all_required_files


#This method tells whether the file is present in the system or not
def search(status, query):

    #Initialize message to null
    message = ''

    #Find the path of the required file in the system
    file_path = sys_find(query)

    #Determine the file found or not.
    if len(file_path) == 0:
        message, status = ' ', True
    elif len(file_path) == 1:
        os.startfile(file_path[0])
        message, status = ' ', False
    else:
        os.startfile(file_path[0])
        message, status = 'Multiple files found. Opening the first one.', False

    return message, status

