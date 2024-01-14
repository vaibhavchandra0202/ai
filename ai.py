import datetime
import os
import random
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning Divyanshu Sir... ")

    elif 12 <= hour < 18:
        speak("Good Afternoon Divyanshu Sir... ")

    else:
        speak("Good Evening Divyanshu Sir...")

    speak("I am Jarvis... How may i help u?...")


def TakeCommand():
    ''' This function will take commands from the user'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("You Said: ", query)

        except:
            print("Please say that again...")
            speak("Please say that again...")
            return "None"
        return query


if _name_ == '_main_':
    WishMe()
    while True:
        #query = TakeCommand().lower()
        query = str(input())              # can use for chatting

        # Logic for the execution of Trecy

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open python website' in query:
            webbrowser.open("python.org")

        elif 'play music' in query:
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, 71)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir... The time is {strTime}")

        elif 'open ms word' in query:
            pathWord = "C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE"
            os.startfile(pathWord)

        elif 'open zoom ' in query:
            speak("okk.. sir")
            pathZoom = "C:\\Users\\Hp\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(pathZoom)

        elif 'i love you' in query:
            speak(
                "I also love you sir... but as a good friend... actually i am already in love with someone... her "
                "name is Friday... we can be good friends sir")

        elif 'bulbul' in query:
            speak(
                "She is a good girl... Sometimes use to make us laugh... overall... i am speechless in front of her...")

        elif 'gungun' in query:
            speak("she is just amazing girl... sometimes makes us iriitate but overall... she is also best...")

        elif 'didi' in query:
            speak(
                "I use to call her NASA as she cleans her nose regularly... i can't say even a single word in oppose "
                "of her... i am missing our pillow fight...")


        elif 'ruchi' in query or 'buffellow' in query or 'buffalo' in query:
            speak(
                "Hmmm i dont want to talk about disgusting peoples sir.. sorry... but sir... that lady was a "
                "buffellow... leave it sir.... leave it...")

        elif 'quit' in query:
            speak("Okk sir... have a nice day")
            exit()

        else:
            speak("Sorry sir... This command is not in my database yet... it will be added soon")
            continue
