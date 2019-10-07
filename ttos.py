from gtts import gTTS
import os

class Ttos:

    def say(self, mytext):
        myobj = gTTS(text=mytext, lang="es")
        myobj.save("/home/linaro/Escritorio/AI-Voice/instantAudio.mp3")
        os.system("mpg321 /home/linaro/Escritorio/AI-Voice/instantAudio.mp3")
        os.remove("/home/linaro/Escritorio/AI-Voice/instantAudio.mp3")
        
    def intro(self):
        os.system("mpg321 /home/linaro/Escritorio/AI-Voice/audios/intro.mp3")
    
    def error(self):
        os.system("mpg321 /home/linaro/Escritorio/AI-Voice/audios/error.mp3")

    def deNada(self):
        os.system("mpg321 /home/linaro/Escritorio/AI-Voice/audios/deNada.mp3")
