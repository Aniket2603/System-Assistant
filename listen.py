'''This module take in the input as voice and provide output as a string.'''
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    '''
    try:
        query = r.recognize_google(audio, language='en-in')
    except:
        return None
    return query
    '''
    
    query = r.recognize_google(audio, language='en-in')
    return query
