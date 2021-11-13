import speech_recognition as sr
# import pyaudio
import pywhatkit
from gTTS import gtts
from pygame import mixer as mx

def speech(text):
    print(text)
    language="en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("./sounds/output.mp3")
    mx.init()
    mx.music.load("./sounds/output.mp3")
    mx.music.set_volume(0.8)
    mx.music.play()

speech("Hello Sir!")

def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recorder.listen(source)
        text = recorder.recognize_google(audio)
        print(f"You said: {text}.")
        return text

text = get_audio()
