# from WeatherOutput import *
from GoogleSearch import *
from AudioInput import *

#Runs untill the user says quit
while True:
    command = audio_input()
    print(command)
    if command:
        if 'google' in command.lower():
            print(command)
            search(command)
        if 'quit' in command:
            break