#coding=UTF-8
#!/usr/bin/python
from filterop import Filterop
from ttos import Ttos
from repo import ALARM_F, CN
from timeop import Timeop

import speech_recognition as sr

rec = sr.Recognizer() # Creació instància reconeixedor.
mic = sr.Microphone() # Creació instància micròfon.

rec.energy_threshold = 90 # Llindar del nivell de so. Valors per sota del llindar es consideren silenci.
rec.pause_threshold = 1 # Llindar de pausa. Minim temps (sec) de silenci per registrar el final d'una frase.

Ttos().intro() # Introducció de Lima.

while True: # Inici bucle principal.
    # Detecció de l'hora per fer sonar l'alarma.
    if (ALARM_F[0] == True):
        Ttos().clockalarm()
    elif Timeop().check_alarm():
        ALARM_F[0] = True
        ALARM_F[1] = ""

    try:
        with mic as source:
            print("Ajustant soroll...")
            rec.adjust_for_ambient_noise(source, duration = 0.8)  # Reajustament del soroll. duration (sec)
            print("Escoltant...")
            audio = rec.listen(source, timeout = 10) # Escolta si algú parla. timeout (sec) salta excepció i torna al bucle
            print("OK")
            text = rec.recognize_google(audio, language="es-ES") # Reconéixer la frase, si l'entent converteix l'audio en text, sinó salta excepció.
            print("Has dit: {}".format(text))
            if ("Lima" in text) and ("adiós" in text): # Comanda de veu per tancar el programa.
                # Reproduir àudio de comiat.
                break
            elif "Lima" in text: # Comanda de veu per analitzar la frase.
                Filterop().options(rec, mic, text)
            elif "gracias" in text:
                Ttos().deNada()
            elif "parar alarma" in text:
                ALARM_F[0] = False
    except:
        pass
