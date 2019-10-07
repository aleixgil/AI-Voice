# Import the required module for text
# to speech conversion
from gtts import gTTS
from audiovoice import *
# This module is imported so that we can
# play the converted audio
import os
# The text that you want to convert to audio

# Language in which you want to convert
language = 'es'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
if "parar" or "para" in textAudio:
    mytext = 'Alarma parada'
if "hora" in textAudio:
    mytext = 'Són las 12 del mediodia'
if "llamo" in textAudio:
    mytext = 'Te llamas Dámaris'

myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("speak.mp3")

# Playing the converted file
os.system("mpg321 speak.mp3")
