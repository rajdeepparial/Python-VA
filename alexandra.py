#pip install pyttsx3
#pip install speechRecognition
#pip install pipwin
#pipwin install pyaudio
#pip install wikipedia

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

from tkinter import *
root = Tk()
root.geometry("310x300")
root.minsize(310,300)
root.maxsize(310,300)
root.title("Alexandra-Virtual Assistant")
root.configure(bg="black")
root.wm_iconbitmap("alexandra.ico")
textvalue = StringVar()
textvalue.set("")

engine = pyttsx3.init('sapi5')  #Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    '''Function helps our assistant to speak'''
    engine.say(audio)
    engine.runAndWait()

def greet():
    '''Function greets user'''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning, How can I help you?")
    elif hour>12 and hour<=18:
        speak("Good Afternoon, How can I help you?")
    else:
        speak("Good Evening, How can I help you?")

def takeCommand():
    '''Function takes voice command from user, returns string output'''
    speak("Hello I am your assistant")
    greet()
    global textvalue
    r = sr.Recognizer()
    with sr.Microphone() as source: #pip install pipwin, pipwin install pyaudio
        textvalue.set("Listening..")
        t1.update()
        r.pause_threshold = 1  #user can speak a phrase with maximum 1 sec delay in two words
        audio = r.listen(source) #audiodata object
    try:
        textvalue.set("Recognizing...")
        t1.update()
        query = r.recognize_google(audio, language='en-in')  #recognizing audio and assigning to a string
        textvalue.set(query)
        query = query.lower()
        t1.update()
    except Exception as e:   #if any error
        print("Say it again please")
        takeCommand()
        return "None"
    if 'wikipedia' in query:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        speak(results)
    elif 'what is your name' in query or 'who are you' in query or 'your name' in query:
        speak("Hello, my name is Alexandra, I am your virtual assistant")
    elif 'who made you' in query or 'who created you' in query:
        speak("AI engineer and developer Rajdeep Parial created me")
    elif 'open youtube' in query:
        webbrowser.open("www.youtube.com")
    elif 'open facebook' in query:
        webbrowser.open("www.facebook.com")
    elif 'open instagram' in query:
        webbrowser.open("www.instagram.com")
    elif 'geeksforgeeks' in query:
        webbrowser.open("www.geeksforgeeks.com")
    elif 'open twitter' in query:
        webbrowser.open("www.twitter.com")
    elif 'open flipkart' in query:
        webbrowser.open("www.flipkart.com")
    elif 'open amazon' in query:
        webbrowser.open("www.amazon.in")
    elif 'play music' in query:
        webbrowser.open("www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")
    elif 'date' in query:
        date = datetime.datetime.now().date()
        speak(f"Todays date is {date}")
    elif 'the time' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")
    elif 'open code' in query:
        codepath = "C:\\Users\\rajde\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    elif 'repeat after me' in query:
        query = query.replace("repeat after me ", " ")
        speak(query)
    elif 'stop' in query or 'shut up' in query or 'exit' in query:
        activateRecognition = False
        speak("Okay have a good time")
    else:
        speak("Sorry couldn't find anything")
        takeCommand()

t1 = Entry(root, text=textvalue, font="lucida 10 bold", width="40", borderwidth=5)
t1.grid(row=1,column=1, padx=10, pady=10, ipady=10)

f1 = Frame(root, bg="light yellow")
commandbtn = Button(f1, text="Speak", font="lucida 15 bold", bg="black", fg="red", command=takeCommand).pack(padx=5, pady=2, side=LEFT)
f1.grid(row=2,column=1, pady=50)

user_name = Label(root, text = "Copyright©Rajdeep Parial 2021", bg="black", fg="red").grid(row=3, column=1)
root.mainloop()