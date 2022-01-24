import datetime
import pyttsx3
import pywhatkit
import smtplib
import calendar
import os
import requests
engine=pyttsx3.init()
engine.setProperty("rate",150)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour<12:
        speak("good morning,how may i help you")
    elif hour<16:
        speak("good afternoon,how may i help you")
    else:
        speak("good evening, how may i help you")
wishme()
tell=input("COMMAND ME")
def Youtube():
    try:
        pywhatkit.playonyt(n)
        print("playing...")
        exit()
    except:
        pass
Youtube()
def googlesearch():
    try:
        pywhatkit.search(s)
        print("Searching...")
        exit()
    except:
        pass
googlesearch()
def Whatsapp():
    try:
        pywhatkit.sendwhatmsg(no,m,h,mi)
        print("Successfully Sent")
    except:
        pass
Whatsapp()
def Searching():
    try:
        pywhatkit.info(inf,lines=5)
        print("\nSearch Successful")
    except:
        pass
Searching()
def calender():
    pass
def News():
    url="https://newsapi.org/v1/articles?sourc..."
    open_bbc=requests.get(url).json()
    article=open_bbc["articles"]
    res=[]
    for ar in article:
        res.append(ar["title"])
    for i in range(len(res)):
        print(i+1,res[i])

News()

if "video" in tell:
    speak("enter the video u want to play")
    n=input("ENTER A VIDEO TO PLAY")
    speak("just a moment")
    Youtube()
if "search" in tell:
    speak("what do u want to search")
    s=input("ENTER SOMETHING TO SEARCH")
    speak("searching")
    googlesearch()
if "message" in tell:
    speak("Whom do u want to send the message")
    no=input("enter the number to send message : ")
    speak("Type your message")
    m=input("type the message : ")
    speak("Enter at which hour in 24 format")
    h=int(input("enter the hours : "))
    speak("enter at which minute in 24 format")
    mi=int(input("enter the minutes : "))
    Whatsapp()

if "calendar" in tell:
    yy = int(input("Enter the year"))
    speak(f"getting calendar of year {yy}")
    print(calendar.calendar(yy))
    calender()
if "news" in tell:
    News()



