import googletrans
import speech_recognition as sr
import gtts
import playsound
recongnizer = sr.Recognizer()

translate = googletrans.Translator()
input_lan = 'en'
her_lan = 'bn'
try:
    with sr.Microphone() as source:
        print('speak now')
        voice = recongnizer.listen(source)
        text = recongnizer.recognize_google(voice, language=input_lan)
        print(text)
except:
    pass

translated = translate.translate(text, dest=her_lan)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=her_lan)
converted_audio.save('romantic.mp3')
playsound.playsound('romantic.mp3')
