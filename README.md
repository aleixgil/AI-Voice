# AI-Voice

sempre sudo apt-get update

sudo apt-get install python3-pip

Setuptools are out of date: pip install --upgrade setuptools

sudo pip3 install gTTS

sudo pip3 install SpeechRecognition

sudo apt-get install python3-pyaudio

sudo apt-get install mpg321

~/.config/autostart$ nano lima-start.desktop 
[Desktop Entry]
Name=LIMA
Exec=lxterminal --command="/bin/bash -c 'python3 /home/Linaro/AI-Voice/LIMA.py; /bin/bash'"
Type=Application
