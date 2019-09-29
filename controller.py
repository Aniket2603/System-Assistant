'''This module is a controller. It manages the different functionalities of the entire system.'''
import basic_functions
import io_manager as io
import sys_search as sys
import web_search as wb

#These are keywords that decides which functionality to choose.
system_keywords = ['play','show','find']
web_keywords = ['search','web','google','chrome','internet','youtube']


#Function to check whether query is for System Search or not
def system_search(status, query):

    #Initialize message to null
    message = ''
    
    try:
        #print('Entered system function')
        for key in system_keywords:
            if key in query:
                file_name = query[len(key)+1:]
                message, status = sys.search(True, file_name)
                break
        #print('Leaving system function')
    except:
        print('Error in system search function')
        
    return message, status


#Function determines the functionality to be used. If status is returns False, the functionality has been used.
def functionality_search(status, query):
    
    #To check whether functionality has to be performed or not
    if status is True:
        #Basic Functionality Module.
        message, status = basic_functions.basic_func(status, query)

        #Web Search Module Based on Keywords.
        if status is True:
            for key in web_keywords:
                if key in query:
                    message, status = wb.search(query)

        #System Search Module.
        if status is True:
            message, status = system_search(status, query)
            #Web Search Module as unavailable in system
            if status is True:
                message, status = wb.search(query)
    #If no module is used
    else:
        message = False

    return message, status



#This method calls all the functions 
def main():
    search_status = io.outputs('Hello Sir. How may I help You?', True)

    while(True):
        try:
            #search_status is to check whether it should be performed or not.
            query, search_status= io.inputs(search_status)

            print(query, search_status)
            message, search_status = functionality_search(search_status, query.lower())
            search_status = io.outputs(message, search_status)
        except:
            print('Something is not correct')
            search_status = True
            #speak.speak('Somethong is not correct')

#main()
