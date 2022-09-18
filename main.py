import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening.................")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.replace("alexa", "")
    except Exception as e:
        print(e)
    return command


def run_alexa():
    command = take_command()
    command = command.lower()

    if 'alexa' in command:
        command = command.replace("alexa", "")
        print(command)

        if 'play' in command:
            song = command.replace('play', "")
            talk(f'playing {song}')
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk(f"current time is {time}")

        elif 'who is' in command:
            person = command.replace("who is", "")
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)

        else:
            talk("Please say it again i can't understand.")
    else:
        talk("If you want to talk with me say my name alexa.")


while True:
    run_alexa()
