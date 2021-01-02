import speech_recognition as sr   # Listening
import pyttsx3                    # Speaking
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)


def talk(text):
    print("Bot >> ",text)
    engine.say(text)
    engine.runAndWait()


def listen():

    with sr.Microphone() as source:
        print('Bot Listening>> ')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()

        if 'alexa' in command:
            command = command.replace('alexa', '')
            print("Human >> ",command)
            return command

        return None
    

def run_alexa():
    command = listen()
    print(command)
    if command:
    
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'search' in command:
            command = command.replace("search",'')
            pywhatkit.search(command)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('Please say the command again.')


while True:
    run_alexa()
