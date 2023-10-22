import pyttsx3
import PyPDF2

def pdf_to_speech():
    book = open('al.pdf','rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    print(pages)

    specker = pyttsx3.init()
    for num in range(14, pages):
        pages = pdfreader.getPage(14)
        text = pages.extractText()
        specker.say(text)
        specker.runAndWait()
def text_to_speech():
    speech = pyttsx3.init()
    with open("C:\\\\Users\\\\Pc\\\\Desktop\\\\text\\\\evolution.txt", 'r') as file:
        text = file.read()
    speech.say(text)
    speech.runAndWait()


def text_to_speech_speed_control():
    speech = pyttsx3.init()
    with open("C:\\\\Users\\\\Pc\\\\Desktop\\\\text\\\\evolution.txt", 'r') as file:
        text = file.read()
    speech.setProperty('rate', 150)  # set the speaking rate to 150 words per minute
    speech.say(text)
    speech.runAndWait()

text_to_speech()