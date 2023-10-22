import speech_recognition
import pyttsx3
import datetime
import pywhatkit
import wikipedia
listener = speech_recognition.Recognizer
alexa = pyttsx3.init()
alexa.say('how can i help you')
voices = alexa.getProperty('voices')
alexa.setProperty('voice',voices[1].id)
def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def takecommand():

    try:
        with speech_recognition.Microphone() as sourch:
            print('listening')
            voice = listener.listen(sourch)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
              command = command.replace('alexa','' )
    except:
        pass
    return command

def run_alexa():
    command = takecommand()
    if 'time' in command:
        time = datetime.now().strftime('%H:%M')
        print(time)
        talk(time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing'+ song )
        pywhatkit.playonyt(song)
    else:
        print('sorry i didnot understand')


run_alexa()