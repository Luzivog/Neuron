from utils import *
from process_commands import *

activated = False

def take_speech(speech):
    global activated
    print(speech)

    if speech == "néron" or speech == "nero" or speech == "neon":
        speak("Oui ?")
        activated = True

    elif "néron" in speech or activated:
        if not activated:
            speech = speech.split(" ")
            speech.remove("néron")
            speech = " ".join(speech)
        print(speech)

        cmd = ""

        for cmd_kw in data["commands"].items():
            for keyword in cmd_kw[1]:
                for word in speech.split(" "):
                    if word == keyword:
                        cmd = cmd_kw[0]
                        keyword_index = speech.find(keyword)
                        speech = speech[keyword_index::]
                        speech = " ".join(speech.split(" ")[1::])
                        break
                if cmd != "": break
            if cmd != "": break
        
        if cmd == "":
            speak("Je n'ai pas compris.")
            return
        else:
            print("=> Detected command :", cmd)
            print("=> Detected speech :", speech)
            error = eval(cmd + '("' + speech+ '")')
            if error: speak("Je n'ai pas compris.")
            else: activated = False
            return