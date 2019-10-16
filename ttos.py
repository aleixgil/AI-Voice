from gtts import gTTS
import os
from repo import TINKER

class Ttos:
    '''
    Classe Text-to-speech.
    '''
    
    def say(self, mytext):
        '''
        Convertir text a fitxer d'àudio i reproduir-lo.
        '''
        myobj = gTTS(text=mytext, lang="es")
        myobj.save(TINKER[1]+"instantAudio.mp3")
        os.system("mpg321 "+TINKER[1]+"instantAudio.mp3")
        os.remove(TINKER[1]+"instantAudio.mp3")
        
    def intro(self):
        '''
        Reproducció de fitxer d'àudio preestablert.
        '''
        os.system("mpg321 "+TINKER[1]+"audios/intro.mp3")
    
    def error(self):
        '''
        Reproducció de fitxer d'àudio preestablert.
        '''
        os.system("mpg321 "+TINKER[1]+"audios/error.mp3")

    def deNada(self):
        '''
        Reproducció de fitxer d'àudio preestablert.
        '''
        os.system("mpg321 "+TINKER[1]+"audios/deNada.mp3")

    def clockalarm(self):
        '''
        Reproducció de fitxer d'àudio preestablert.
        '''
        os.system(TINKER[3]+"'mpg321 "+TINKER[1]+'audios/clockalarm.mp3'+TINKER[4]+"'"+'"')

