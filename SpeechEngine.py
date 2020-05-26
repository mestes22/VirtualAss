from gtts import gTTS
import playsound
from tempfile import TemporaryFile

j=0

def talk(audio):
    global j
    j+=1

    text_to_speech = gTTS(text=audio, lang="en-uk")
    text_to_speech.save("audio"+str(j)+".mp3")
    playsound.playsound("audio"+str(j)+".mp3")