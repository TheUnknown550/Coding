#Imports
from gtts import gTTS
import os
  
# Text
mytext = 'Text'
#language
language = 'en'
  
#convert
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Save
myobj.save("File.mp3")

#Tell user that its done
print('Voice File is Done!')
