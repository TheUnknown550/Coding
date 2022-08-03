import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Start Speaking")
    audio = r.listen(source)
    print("Stop Speaking")
try:
    print("Processing")
    Speech = r.recognize_google(audio,language = "en")
    print("Your Said: "+ Speech)
except sr.RequestError as e: 
    print("Sorry I didnt hear you")

if "hello" in Speech:
    print("Bot: Hello!")