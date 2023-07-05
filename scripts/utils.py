from gtts import gTTS
import os

def speak(txt):
    tts = gTTS(text=txt, lang='en')
    tts.save(os.path.dirname(__file__)+"/../assets/rep.mp3")
    os.system(f"mplayer '{os.path.dirname(__file__)}/../assets/rep.mp3' > /dev/null 2>&1")

def remove_before(strValue, word):
    listOfWords = strValue.split(word, 1)
    if len(listOfWords) > 1: 
        strValue = listOfWords[1]
    return strValue

