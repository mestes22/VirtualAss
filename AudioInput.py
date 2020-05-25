import speech_recognition as sr
import pyaudio

def audio_input():
    #Set up object from speech recognition
    r = sr.Recognizer()
    #Gives access to microphone
    with sr.Microphone() as source:
        print("Talk")
        #Opens microphone for input
        audio_text = r.listen(source)
        print("Collecting Input...")
        try:
            #Translates audio to text
            return r.recognize_google(audio_text)
        except:
            print("Sorry, I did not get that")