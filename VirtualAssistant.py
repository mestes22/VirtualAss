# from WeatherOutput import *
from GoogleSearch import *
from AudioInput import *
from WeatherOutput import *
#Runs until the user says quit
while True:
    command = audio_input()
    print(command)
    if command:
        if 'google' in command.lower():
            print(command)
            search(command)
        if 'quit' in command:
            break
        if 'weather' in command:
            if ' weather in ' in command:
                before,keyword,after = str.partition('in')
                city = after.strip()
            else:
                city = 'manchester'
            if 'celsius' in command:
                getWeather(city, False)
            else:
                getWeather(city)