#coding=UTF-8
#!/usr/bin/python
from filterop import Filterop
from ttos import Ttos
from repo import ALARM_F
from timeop import Timeop

import speech_recognition as sr

rec = sr.Recognizer()
mic = sr.Microphone()

#rec.energy_threshold = 100
#rec.pause_threshold = 0.8
#rec.dynamic_energy_threshold = True
#rec.dynamic_energy_adjustment_damping = 0.15
#rec.dynamic_energy_adjustment_ratio = 1.5

#Ttos().say("Hola, cómo te llamas?")

#Ttos().intro()

while True:
    print(ALARM_F[1])
    if (ALARM_F[0] == True) and Timeop().check_alarm():
        print("PI PI PI PI PI PI PI PI PI PI PI PI PI....")
        #print("La alarma ha sonado a las {}.".format(ALARM_F[1]))
        ALARM_F[0] = False

    with mic as source:
        print("Speak to loop...")
        rec.adjust_for_ambient_noise(source, duration = 1)  # adjust 1 sec
        audio = rec.listen(source, timeout = 10) # timout 10 sec
        print("OK")
        try:
            #text = rec.recognize_google(audio, language="es-ES")
            text = input("Say something: ")
            print("You said: {}".format(text))
            if "Lima" in text:
                Filterop().options(rec, mic, text)
            elif "gracias" in text:
                Ttos().deNada()
            elif text == "q":
                break
        except:
            print("Sorry could not recognize your voice.")
