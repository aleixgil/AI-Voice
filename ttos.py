from gtts import gTTS
import os

class Ttos:

    def say(self, mytext):
        myobj = gTTS(text=mytext, lang="es")
        myobj.save("instantAudio.mp3")
        os.system("mpg321 instantAudio.mp3")
        os.remove("instantAudio.mp3")
        
    def intro(self):
        os.system("mpg321 audios/intro.mp3")
    
    def error(self):
        os.system("mpg321 audios/error.mp3")

    def deNada(self):
        os.system("mpg321 audios/deNada.mp3")
