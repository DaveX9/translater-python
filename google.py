"""pip install googletrans
pip install SpeechRecognition
pip install PyAudio
pip install gTTS
pip install playsound"""
import tkinter as tk
import googletrans
import speech_recognition
import speech_recognition  as sr
from gtts import gTTS
import playsound
import gtts
import playsound


recognizer = speech_recognition.Recognizer()
with sr.Microphone() as source:
    print("Speak Now...")
    voice = recognizer.listen(source)
    listen = recognizer.recognize_google(voice, language="en")
    print(listen)

#print(googletrans.LAN GUAGES)
translator = googletrans.Translator()
translate = translator.translate(listen,dest='th')
print(translate.text)
converted_audio = gtts.gTTS(translate.text, lang="th")
converted_audio.save("output.mp3")
playsound.playsound("output.mp3") 
#print(googletrans.LANGUAGES)
