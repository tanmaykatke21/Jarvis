import tkinter as tk
from tkinter.ttk import *
from PIL import Image,ImageTk
from pygame import mixer
from time import sleep
from datetime import datetime
import threading

def alarm():
    root=tk.Tk()
    root.title("Alarm Clock")
    root.geometry("350x150+600+200")
    root.config(bg="white")

    #upper frame
    frame_line=tk.Frame(root, width=400, height=5,background="purple")
    frame_line.grid(row=0,column=0)

    frame_body=tk.Frame(root, width=400, height=290,background="white")
    frame_body.grid(row=1,column=0)

    #configuring frame body
    img=Image.open(r'icons8-alarm-100.png')
    img.resize((100,100))
    img=ImageTk.PhotoImage(img)

    app_img=tk.Label(frame_body,height=100,image=img,bg="white")
    app_img.place(x=10,y=10)

    name=tk.Label(frame_body,text="ALARM",height=1,font=("Ivy",18,"bold"),background="white")
    name.place(x=125,y=10)

    hour=tk.Label(frame_body,text="Hour",height=1,font=("Ivy",10,"bold"),background="white",foreground="purple")
    hour.place(x=127,y=40)
    c_hour=Combobox(frame_body,width=2,font=("Ariel",15,"bold"))
    c_hour['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12")
    c_hour.current(0)
    c_hour.place(x=130,y=58)

    mins=tk.Label(frame_body,text="Min",height=1,font=("Ivy",10,"bold"),background="white",foreground="purple")
    mins.place(x=177,y=40)
    c_mins=Combobox(frame_body,width=2,font=("Ariel",15,"bold"))
    c_mins['values']=("00","01","02","03","04","05","06","07","08","09","10",
                    "11","12","13","14","15","16","17","18","19","20",
                    "21","22","23","24","25","26","27","28","29","30",
                    "31","32","33","34","35","36","37","38","39","40",
                    "41","42","43","44","45","46","47","48","49","50",
                    "51","52","53","54","55","56","57","58","59"
                    )
    c_mins.current(0)
    c_mins.place(x=180,y=58)

    secs=tk.Label(frame_body,text="Sec",height=1,font=("Ivy",10,"bold"),background="white",foreground="purple")
    secs.place(x=227,y=40)
    c_secs=Combobox(frame_body,width=2,font=("Ariel",15,"bold"))
    c_secs['values']=("00","01","02","03","04","05","06","07","08","09","10",
                    "11","12","13","14","15","16","17","18","19","20",
                    "21","22","23","24","25","26","27","28","29","30",
                    "31","32","33","34","35","36","37","38","39","40",
                    "41","42","43","44","45","46","47","48","49","50",
                    "51","52","53","54","55","56","57","58","59"
                    )
    c_secs.current(0)
    c_secs.place(x=230,y=58)

    period=tk.Label(frame_body,text="Period",height=1,font=("Ivy",10,"bold"),background="white",foreground="purple")
    period.place(x=277,y=40)
    c_period=Combobox(frame_body,width=3,font=("Ariel",15,"bold"))
    c_period['values']=("AM","PM")
    c_period.current(0)
    c_period.place(x=280,y=58)

    t=threading.Thread(target=alarm)
    def activate_alarm():
        # t=threading.Thread(target=alarm)
        t.start()

    def deactivate_alarm():
        print("Deactivated alarm: ",selected.get())
        mixer.music.stop()

    selected=tk.IntVar()
    rad1=tk.Radiobutton(frame_body,font=("Ariel",10,"bold"),value=1,text="Activate",bg="White",command=activate_alarm,variable=selected)
    rad1.place(x=125,y=95)

    def sound_alarm():
        mixer.music.load('alarm_ringtone.mp3')
        mixer.music.play()
        selected.set(0)

        rad2=tk.Radiobutton(frame_body,font=("Ariel",10,"bold"),value=2,text="Deactivate",bg="White",command=deactivate_alarm,variable=selected)
        rad2.place(x=207,y=95)

    def alarm():
        while True:
            control = selected.get()
            print(control)

            alarm_hour=c_hour.get()
            alarm_minute=c_mins.get()
            alarm_sec=c_secs.get()
            alarm_period=c_period.get()
            alarm_period=str(alarm_period).upper()

            now=datetime.now()
            hour = now.strftime("%I")
            minute=now.strftime("%M")
            second=now.strftime("%S")
            period=now.strftime("%p")

            if control==1:
                if alarm_period==period:
                    if alarm_hour==hour:
                        if alarm_minute==minute:
                            if alarm_sec==second:
                                print("Time to take a break")
                                sound_alarm()
            sleep(1)

    mixer.init()
    root.mainloop()  
      