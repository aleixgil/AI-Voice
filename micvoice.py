#coding=UTF-8

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak: ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
    except:
        print("I can't hear you well.")

# cp lib/.libs/libportaudio.a /home/aleixgil/Dropbox
# cp /usr/local/lib/libportaudio.a /home/aleixgil/Dropbox
# gcc main.c libportaudio.a -lrt -lm -lasound -ljack -pthread -o voice
