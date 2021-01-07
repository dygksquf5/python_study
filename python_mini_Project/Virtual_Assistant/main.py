import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_command():
    try:
        with sr.Microphone() as source:
            print(" listening ... ")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bixby' in command:
                command = command.replace('bixby', '')
                print(command)

        return command

    except:
        pass



def run_bixby():
    command = get_command()
    # print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current time is "+time)
    elif 'where is' in command:
        info = command.replace('where is', '')
        finding = wikipedia.summary(info, 1)
        print(finding)
        talk(finding)
    elif 'what is' in command:
        info = command.replace('where is', '')
        finding = wikipedia.summary(info, 1)
        print(finding)
        talk(finding)
    elif 'who is' in command:
        info = command.replace('where is', '')
        finding = wikipedia.summary(info, 1)
        print(finding)
        talk(finding)
    elif 'find ' in command:
        info = command.replace('find', '')
        finding = pywhatkit.search(info)
        print(finding)
        talk(finding)

    else:
        talk("please say the command again")


while True:
    run_bixby()