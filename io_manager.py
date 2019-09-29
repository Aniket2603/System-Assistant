'''This module manages between all the inputs and output devices of the system'''
import listen
import speak


#An input class
class all_inputs:
    def listen():
        query = listen.listen()
        return query
        
    def type():
        message = 'Entered the keyboard Mode'
        outputs(message, True)
        query = input()
        return query, True

#An output class
class all_outputs:
    def talk(message):
        speak.speak(message)

    def display(message):
        print(message)



#This method is used to manage between input resources
#Status is parameter passed to know whether it should take input or not
def inputs(status):
    keyword = 'zoya'
    try:
        #Default input is audio.
        query = all_inputs.listen()

        #This is to determine whether instructions are to executed or not
        if keyword == query[:len(keyword)].lower():
            status = True
            query = query[len(keyword)+1:]
        elif 'keyboard' in query:
            status = True
            query = input()
        else:
            status = False
            
    except:
        query, status = 'Repeat Please', False

    return query, status


#This method is used to manage between output resources
def outputs(task, status):
    if task == False:
        status = False
    elif task == ' ':
        message = ''
    else:
        message = task
        all_outputs.display(message)
        status = True
    all_outputs.talk(message)
    return status
    
