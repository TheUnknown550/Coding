import pyttsx3
import os
import speech_recognition as sr

def BotSpeech(Text):
    File = 'File.mp3'
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    #Reading Speed
    newVoiceRate = 170
    engine.setProperty('rate',newVoiceRate)

    #Let Ai Say the Text
    engine.say(Text)

    #File location
    engine.save_to_file(Text,File)
    engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Start Speaking")
    audio = r.listen(source)
    print("Stop Speaking")
try:
    print("Processing")
    Speech = r.recognize_google(audio,language = "th-TH")
    print("Your Said: "+ Speech)
except sr.RequestError as e: 
    print("Sorry I didnt hear you")

if "hello" in Speech:
    print("Bot: Hello!")
    BotSpeech("Hello!, What do you want?")

if "light" in Speech:
    print("Bot: Hello!")
    BotSpeech("No!")

