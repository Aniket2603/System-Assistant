import listen
import speak

def introduce():
    text = 'Welcome sir!. How was your day?'
    speak.speak(text)

def chatbot():
    while( True ):
        try:
            '''
            text = ''
            query = listen.listen()
            '''
            
            if 'say hello to ' in query.lower():
                text = 'Hello ' + query[13:]
                text = text + '. Its nice to meet you.'
            
            elif 'fine' in query.lower():
                text = 'Nice to hear that.'

            else:
                text = 'Sir. You have not taught me how to respond to that'
        except:
            text = 'Sir. I think somthing is wrong with the chat bot.'

        speak.speak(text)

        if 'search' in query.lower():
            speak.speak('Ok sir.')
            return False

    return False
