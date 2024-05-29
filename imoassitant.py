import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Ino Sir. Please tell me how may I help you")

def clean_transcript(transcript):
    cleaned_transcript = ' '.join(transcript.split())
    return cleaned_transcript

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        cleaned_query = clean_transcript(query)
        print(f"User said: {cleaned_query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return cleaned_query

def sendEmail(to, content):
    # Fill in your email sending code here
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your-email@gmail.com', 'your-password')
        server.sendmail('your-email@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("I am not able to send this email")

if __name__ == "__main__":
    wishMe()
    while True:
        cleaned_query = takeCommand().lower()

        if 'wikipedia' in cleaned_query:
            speak('Searching Wikipedia...')
            cleaned_query = cleaned_query.replace("wikipedia", "")
            results = wikipedia.summary(cleaned_query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in cleaned_query:
            webbrowser.open("youtube.com")

        elif 'open google' in cleaned_query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in cleaned_query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in cleaned_query:
            # Play music logic
            music_dir = 'path_to_music_directory'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in cleaned_query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in cleaned_query:
            codePath = "path_to_code_editor"
            os.startfile(codePath)
        elif 'email to ankit' in cleaned_query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ankit@example.com"    
                sendEmail(to, content)
            except Exception as e:
                speak("I am not able to send this email")
