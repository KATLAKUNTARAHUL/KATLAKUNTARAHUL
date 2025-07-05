import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import time

engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    print("🎙 rahul:", text)
    engine.say(text)
    try:
        engine.runAndWait()
    except Exception as e:
        print(f"⚠️ Speech error: {e}")

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        listener.adjust_for_ambient_noise(source)
        try:
            voice = listener.listen(source, timeout=5, phrase_time_limit=10)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("🗣 You said:", command)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            talk("Network issue with Google service.")
            return ""
        except sr.WaitTimeoutError:
            return ""
        except Exception as e:
            print(f"Other recognition error: {e}")
            return ""
    return command

def run_rahul():
    command = take_command()

    if command and "rahul" in command:
        command = command.replace("rahul", "").strip()

        if "play" in command:
            song = command.replace("play", "").strip()
            if song:
                talk(f"Playing {song} on YouTube 🎶")
                pywhatkit.playonyt(song)
            else:
                talk("Please tell me which song to play.")

        elif "what's the time" in command:
            time_now = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"It’s {time_now} ⏰")

        elif "who is rahul codes" in command or "who is rahul_codes" in command:
            info = (
                "Rahul, known as rahul_318, is a coding content creator. "
                "He teaches Python projects in Telugu and runs udaycodes.in 💻"
            )
            talk(info)

        elif "who is" in command:
            person = command.replace("who is", "").strip()
            if person:
                try:
                    info = wikipedia.summary(person, sentences=1)
                    talk(info)
                except Exception:
                    talk("Sorry, I couldn’t find information about that person.")
            else:
                talk("Please say the name clearly after 'who is'.")

        elif "joke" in command:
            joke = pyjokes.get_joke()
            talk(joke)

        elif "open chrome" in command:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            if os.path.exists(chrome_path):
                talk("Opening Chrome 🚀")
                os.startfile(chrome_path)
            else:
                talk("Chrome path not found 😬")

        elif "open code" in command or "open vs code" in command:
            talk("Opening VS Code 💻")
            os.system("code")

        elif "exit" in command or "stop" in command:
            talk("Okay bro, see you later 👋")
            sys.exit()

        elif command != "":
            talk("I heard you, but I don’t understand that yet 😅")

talk("Yo! I'm rahul – your personal voice assistant 💡")

while True:
    run_rahul()
    time.sleep(0.5)
