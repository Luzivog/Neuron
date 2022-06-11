from gtts import gTTS
import os

def speak(txt):
    tts = gTTS(text=txt, lang='fr')
    tts.save("rep.mp3")
    os.system("mplayer rep.mp3 > /dev/null 2>&1")

def remove_before(strValue, word):
    listOfWords = strValue.split(word, 1)
    if len(listOfWords) > 1: 
        strValue = listOfWords[1]
    return strValue

