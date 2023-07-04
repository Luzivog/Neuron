from utils import *
from process_commands import *

activated = False

def take_speech(speech):
    global activated
    print(speech)

    if speech in data["trigger"]:
        speak("Yes ?")
        activated = True

    elif "neuron" in speech or activated:
        if not activated:
            speech = speech.split(" ")
            speech.remove("neuron")
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
            speak("I didn't understand.")
            return
        else:
            print("=> Detected command :", cmd)
            print("=> Detected speech :", speech)
            error = eval(cmd + '("' + speech+ '")')
            if error: speak("I didn't understand.")
            else: activated = False
            return