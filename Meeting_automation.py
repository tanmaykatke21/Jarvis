import pyttsx3
import speech_recognition as sr
from tkinter import *
from tkinter.messagebox import *
import webbrowser as web
import time
import keyboard

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

def meet_automate(link):
    web.open(link)
    time.sleep(5)
    keyboard.press_and_release('CTRL + E')
    time.sleep(5)    
    keyboard.press_and_release('CTRL + d')
    time.sleep(5)
    for i in range (0,10):
        keyboard.press_and_release('tab')
    keyboard.press_and_release('enter')

def start_meet():
    while True:
        Speak("should i start your personal meet mam?")
        query = takecommand()

        if "yes" in query:
            link="https://meet.google.com/kky-vmxt-qft"
            meet_automate(link)
            Speak("Task done mam.")
            break                                

        elif "no" in query:
            Speak("Please give me the meet link")
            # link=input("Enter meet link")
            class GetEntry():
                def __init__(self, master):
                    self.master = master
                    self.entry_name_contents = None
                    self.entry_email_contents = None
                    self.meetlbl=Label(master,text="Enter Meet Link: ",font=("Ariel",12,"bold"))
                    self.meetent = Entry(master,font=("Ariel",15,"bold"),bd=2)
                    self.meetlbl.grid(row=0, column=0)
                    self.meetent.grid(row=0, column=1)
                    self.meetent.focus_set()

                    Button(master, text="get", width=10, bg="yellow",
                            command=self.callback).grid(row=1, column=1,sticky="e")

                def callback(self):
                    """ get the contents of the Entry and exit
                    """
                    self.entry_meet_contents = self.meetent.get()
                    self.master.quit()
                    self.master.destroy()

            master = Tk()
            master.geometry("550x90+100+100")
            master.title("Enter new contact")
            master.config(background="lightblue")
            GE = GetEntry(master)
            master.mainloop()

            while True:
                link=GE.entry_meet_contents
                meet_automate(link)
                Speak("Task done mam.")
                break        
            break