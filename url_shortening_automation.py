import pyttsx3
import speech_recognition as sr
from pywikihow import search_wikihow
from playsound import playsound
from tkinter import *
from tkinter.messagebox import *
import pyshorteners
from tkinter import *
import pyperclip

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
# I have used this path to open every thing
# in chrome rather than opening in edge by default


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
        # command.pause_threshold=1
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

def UrlShortener(url):
    url_short=pyshorteners.Shortener().tinyurl.short(url)
    return url_short

def CopyUrl(url_short):
    pyperclip.copy(url_short)

def automatic_url_shortening():

    while True:
        Speak("Please enter the URL you want to Shorten")

        class GetEntry():
            def __init__(self, master):
                self.master = master
                self.entry_big_url_contents = None
                self.bigurllbl=Label(master,text="Enter URL to be shortened: ",font=("Ariel",13,"bold"),bg="lightblue")
                self.bigurlentry = Entry(master,font=("Ariel",15,"bold"),bd=2,width=25)

                self.bigurllbl.grid(row=0, column=0,padx=5,pady=10)
                self.bigurlentry.grid(row=0, column=1,padx=5,pady=10)
                self.bigurlentry.focus_set()

                Button(master, text="get", width=10, bg="yellow",
                        command=self.callback).grid(row=1, column=1, padx=5,pady=10,sticky="w")

            def callback(self):
                """ get the contents of the Entry and exit
                """
                self.entry_big_url_contents = self.bigurlentry.get()
                self.master.quit()
                self.master.destroy()

        master = Tk()
        master.geometry("670x120+100+100")
        master.title("Enter Big URL")
        master.config(background="lightblue")
        GE = GetEntry(master)
        master.mainloop()

        while True:
            big_url = GE.entry_big_url_contents
            short=UrlShortener(big_url)
            CopyUrl(short)
            Speak("Shortened URL copied to your clipboard mam")
            break
        break