import tkinter as tk
from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
import playsound

def translate_and_speak():
    input_text = input_text_area.get("1.0", tk.END).strip()

    if input_text:
        translator = Translator()
        translation = translator.translate(input_text, dest='th')
        translated_text = translation.text
        output_text_area.delete("1.0", tk.END)
        output_text_area.insert(tk.END, translated_text)
        tts = gTTS(text=translated_text, lang="th")
        tts.save("output.mp3")
        playsound.playsound("output.mp3")

def transcribe_and_play():
    # Perform speech recognition
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now...")
        voice = recognizer.listen(source)
        listen = recognizer.recognize_google(voice, language="en")
    translator = Translator()
    translation = translator.translate(listen, dest='th')
    translated_text = translation.text
    output_text_area.delete("1.0", tk.END)  
    output_text_area.insert(tk.END, translated_text)
    tts = gTTS(text=translated_text, lang="th")
    tts.save("output.mp3")
    playsound.playsound("output.mp3")
window = tk.Tk()
window.title("Translate and Speak App")
input_text_area = tk.Text(window, height=5, width=50)
input_text_area.pack(pady=10)
translate_button = tk.Button(window, text="Translate and Speak", command=translate_and_speak)
translate_button.pack(pady=5)
transcribe_button = tk.Button(window, text="Transcribe and Play", command=transcribe_and_play)
transcribe_button.pack(pady=5)
output_text_area = tk.Text(window, height=5, width=50)
output_text_area.pack(pady=10)
window.mainloop()
