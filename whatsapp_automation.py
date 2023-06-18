import pyttsx3
import speech_recognition as sr
from tkinter import *
from tkinter.messagebox import *
import webbrowser as web
from time import sleep
from keyboard import press
from keyboard import press_and_release
from keyboard import write

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
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone(1) as source:  # use Microphone(1) if you have
        print("Listening...")
        command.adjust_for_ambient_noise(source)
        command.energy_threshold = 250
        audio = command.listen(source,0,5)
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


def WhatsappMsg(name,message):

    web.open("https://web.whatsapp.com/")
    sleep(20) #sleep while whatsapp web is loading
    press_and_release('CTRL + ALT + /') #selecting search tab of whatsapp
    sleep(5) #sleep after selecting the search tab
    write(name) #writing name on search tab of whatsapp
    sleep(5) #sleep while the name is being entered int he whatapp search tab
    press_and_release('down') #selecting first best search result of whatsapp    
    sleep(5) #sleep while selecting the first search of the name
    press('enter') #selecting chat box of whatsapp
    sleep(5) # sleep while selecting the chat box 
    write(message) #Writing the msg in whatsapp chat box
    press('enter') #pressing the enter key to send the message

def WhatsappChat(name):
    web.open("https://web.whatsapp.com/")
    sleep(20) #sleep while whatsapp web is loading
    press_and_release('CTRL + ALT + /') #selecting search tab of whatsapp
    sleep(5) #sleep after selecting search tab
    write(name) #writing name on search tab of whatsapp
    sleep(5) #sleep while the name is being entered int he whatapp search tab
    press_and_release('down')#selecting first best search result of whatsapp    
    sleep(5) #sleep while selecting the first search of the name
    press('enter')#selecting chat box of whatsapp


def wp_msg():        
        Speak("Whom do you want to send the msg to?")
        query = takecommand()        
        name = query.replace("Whatsapp Message","")
        name = name.replace("send","")
        name = name.replace("to","")
        name = str(name)
        Speak(f"Whats The Message for {name}")
        msg = takecommand()
        # from Automations import WhatsappMsg
        WhatsappMsg(name,msg)

def wp_show_chat():
        Speak("Whose whatsapp chat do you want to see?")
        name = takecommand()
        # from Automations import WhatsappChat
        WhatsappChat(name)