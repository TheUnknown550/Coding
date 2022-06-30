import pyttsx3
import os

#variables
Text = 'Text'
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

#tell user that file is done
print('File Done!')