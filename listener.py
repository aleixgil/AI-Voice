#coding=UTF-8
#!/usr/bin/python

import speech_recognition as srec

class SR:
    '''
    Classe de RV.
    '''
    def listener(self, rec, mic):
        with mic as source:
            print("Speak to listener...")
            rec.adjust_for_ambient_noise(source) # adjust 1 sec
            audio = rec.listen(source, timout = 3)
            print("OK")
            try:
                text = rec.recognize_google(audio, language="es-ES")
                print("You said: {}".format(text))
                return(text)
            except:
                print("Sorry could not recognize  your voice.")


# SR().listener()
'''
for index, name in enumerate(srec.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
'''