# from WeatherOutput import *
from GoogleSearch import *
from AudioInput import *
from SpeechEngine import *
import pyjokes
import os

#Runs untill the user says quit
while True:
    command = audio_input()
    if command:
        if 'google' in command.lower():
            talk(str("Opening New Tab"))
            search(command)
        if 'joke' in command.lower():
            talk(str(pyjokes.get_joke()))
        if 'quit' in command:
            talk(str("Talk to you later"))
            break

#CONA - Command Operated Novice Assistant