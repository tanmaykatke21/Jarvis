from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import pyttsx3
import speech_recognition as sr
import webbrowser as web

# sapi5 is microsoft's speech recognition IDE
Assistant = pyttsx3.init('sapi5')

# create an instance variable named as voices to get different voices
voices = Assistant.getProperty('voices')
print(voices)

# id 0 is for male and 1 is for female voice
Assistant.setProperty('voices', voices[0].id)
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
    with sr.Microphone() as source:
        print("Listening..")
        command.pause_threshold = 1
        audio = command.listen(source)
        
        try: 
            print("Recognizing..")
            query = command.recognize_google(audio,language = 'en-in')
            print(f"You Said : {query}")
        
        except Exception as e:
            return "none"             
        return query
        
def WhatsappMsg(name,message):

    web.open("https://web.whatsapp.com/")
    sleep(10) #sleep while whatsapp web is loading
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
    sleep(10) #sleep while whatsapp web is loading
    press_and_release('CTRL + ALT + /') #selecting search tab of whatsapp
    sleep(5) #sleep after selecting search tab
    write(name) #writing name on search tab of whatsapp
    sleep(5) #sleep while the name is being entered int he whatapp search tab
    press_and_release('down')#selecting first best search result of whatsapp    
    sleep(5) #sleep while selecting the first search of the name
    press('enter')#selecting chat box of whatsapp