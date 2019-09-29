'''This module manages search based on web'''
import webbrowser
import wikipedia

#This class contains all the methods of websearch
class websearch:
    def google_search(task):
        url = "https://www.google.com.tr/search?q= " + task
        webbrowser.open_new_tab(url)

    def youtube_search(task):
        url = "https://www.youtube.com.tr/search?q= " + task
        webbrowser.open_new_tab(url)


#This function determine which method to call for the given query
#It return True always for status because resuult is always available on google.
def search(task):
    try:
        print('Entered web search module')
        result = ''
        if 'youtube' in task:
            websearch.youtube_search(task[:-10])
        elif 'search' in task:
            result = wikipedia.summary(task[6:], sentences = 2)
        elif 'show' in task:
            result = wikipedia.summary(task[6:], sentences = 2)
        else:
            websearch.google_search(task)
        print('Leaving web search module')
    except:
        print('Error in web search module')

    return result, False
