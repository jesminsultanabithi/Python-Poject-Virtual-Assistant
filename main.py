#Jesmin Sultana 16103227

import datetime
import listener as listener
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices [1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
   try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command= command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
   except:
       pass
   return command

def run_alexa():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play','')
        print('playing')
        talk('playing' +song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        print('Searching')
        wiki = command.replace('tell me about','')
        info = wikipedia.summary(wiki, 3)
        print(info)
        talk(info)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('current time ' +time)
        talk('current time' +time)
    else:
        talk('Sorry! I could not understand')

run_alexa()






