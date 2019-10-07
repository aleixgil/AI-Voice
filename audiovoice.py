
#Python 2.x program to transcribe an Audio file
import speech_recognition as sr
import subprocess

#execute bash command to record audio
subprocess.check_call('arecord -d 3 /home/aleixgil/Dropbox/TFG/test.wav'.split())

AUDIO_FILE = ("test.wav")

# use the audio file as the audio source

r = sr.Recognizer()

if AUDIO_FILE:
    print("File OK")

with sr.AudioFile(AUDIO_FILE) as source:
    #reads the audio file. Here we use record instead of
    #listen
    audio = r.record(source)

textAudio = ""

try:
    textAudio = r.recognize_google(audio, language="es-ES")
    print("The audio file contains: " + textAudio)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
