import speech_recognition as sr
import pyaudio

def audio_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        try:
            # using google speech recognition
            return r.recognize_google(audio_text)
        except:
            print("Sorry, I did not get that")