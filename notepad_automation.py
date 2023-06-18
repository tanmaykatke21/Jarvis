import pyttsx3
import speech_recognition as sr
from tkinter import *
from tkinter.messagebox import *
import datetime
import os
import subprocess

# sapi5 is microsoft's speech recognition IDE
Assistant = pyttsx3.init('sapi5')

# create an instance variable named as voices to get different voices
voices = Assistant.getProperty('voices')
print(voices)

# id 0 is for male and 1 is for female voice
Assistant.setProperty('voices', voices[1].id)
# rate of speed of speaking is 200 by default
Assistant.setProperty('rate', 180)

# path for google chrome.
path = "C://Program Files//Google//Chrome//Application//chrome.exe %s"
# I have used this path to open every thing in chrome by default

def Speak(audio):
    print("    ")
    Assistant.say(audio)
    print(f":{audio}")
    # print("    ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone(1) as source:  # use Microphone(1) if you have
        print("Listening...")
        command.adjust_for_ambient_noise(source)
        command.energy_threshold = 250
        audio = command.listen(source)
        x = True
        while x == True:
            try:
                print("Recognizing...")
                query = command.recognize_google(
                    audio, language='en-in').lower()
                print(f"You said: {query}\n")
                Speak(f"You said: {query}\n")
                x = False
            except Exception as error:
                print("Say that again please...")
                return "None"
            return query.lower()

def automate_notepad():
    while True:
        Speak("Do you want me to type into your notepad?")
        query = takecommand()

        if "yes" in query:
            newpath = r'Notepad' 
            if not os.path.exists(newpath):
                os.makedirs(newpath) 

            Speak("Please tell me what to write?")
            writes = takecommand()
            current_time = datetime.datetime.now()
            time = current_time.strftime("%m:%d:%Y:%H:%M:%S")

            filename = str(time).replace(":","_") + "_notepad.txt"
            filepath=r'Notepad\\'+str(filename)
            with open(filepath,"w") as file:
                file.write(writes) 
            Speak("Notepad created and saved in your notepad folder")
            break 

        elif "exit notepad" in query:
            Speak("Ok mam")
            break                         

        elif "no" in query:
            Speak("Ok, i will just open a new note for you")
            newpath = r'Notepad' 
            if not os.path.exists(newpath):
                os.makedirs(newpath) 
            writes = ""
            current_time = datetime.datetime.now()
            time = current_time.strftime("%m:%d:%Y:%H:%M:%S")

            filename = str(time).replace(":","_") + "_notepad.txt"
            filepath=r'Notepad\\'+str(filename)
            with open(filepath,"w") as file:
                file.write(writes) 
                subprocess.Popen(['notepad.exe',filepath])  
            break 