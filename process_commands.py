# Modules to import

from utils import speak
from pynput.keyboard import Controller
import webbrowser, json, subprocess, os, sys, pywhatkit

# Variables initialization

keyboard = Controller()

jsonfile = open("data.json")
data = json.load(jsonfile)

# Functions associated to commands

def open(speech):
    website = getElement(speech, "websites")
    if website != None:
        webbrowser.open_new_tab(website["website_url"])
        return
    app = getElement(speech, "applications")
    if app == None: return True

    window_list = subprocess.getoutput("wmctrl -l")
    for window_name in window_list.split("\n"):
        if app["window_name"] in window_name:
            os.system(f"wmctrl -a '{app['window_name']}'")
            return

    for i in range(len(app["command_to_start"])):
        print("=> Executed command :", app["command_to_start"][i]["cmd"])
        output = os.popen(app["command_to_start"][i]["cmd"]).read()
        err_output = app["command_to_start"][i]["error_output"]
        if err_output != "" and err_output in output:
            speak(app["command_to_start"][i]["error_msg"])
            return

def close(speech):
    app = getElement(speech, "applications")
    if app == None: return True
    window_list = subprocess.getoutput("wmctrl -l")
    for window_name in window_list.split("\n"):
        if app["window_name"] in window_name:
            os.system(f"wmctrl -c '{app['window_name']}'")
            return
    speak("Cette fenêtre n'est pas ouverte.")
    
    
def write(speech):
    if speech == "": return True
    keyboard.type(speech)
    
    
def maximize(speech):
    app = getElement(speech, "applications")
    if app == None: return True
    
    window_list = subprocess.getoutput("wmctrl -l")
    for window_name in window_list.split("\n"):
        if app["window_name"] in window_name:
            window_id = window_name.split(" ")[0]
            os.system(f"wmctrl -a '{app['window_name']}'")
            os.system(f"xdotool windowsize '{window_id}' 100% 100%")
            return
    
    
    
def minimize(speech):
    app = getElement(speech, "applications")
    if app == None: return True

    window_list = subprocess.getoutput("wmctrl -l")
    for window_name in window_list.split("\n"):
        if app["window_name"] in window_name:
            window_id = window_name.split(" ")[0]
            os.system(f"xdotool windowminimize '{window_id}'")
            return
    
    
def foreground(speech):
    app = getElement(speech, "applications")
    if app == None: return True

    window_list = subprocess.getoutput("wmctrl -l")
    for window_name in window_list.split("\n"):
        if app["window_name"] in window_name:
            os.system(f"wmctrl -a '{app['window_name']}'")
            return
    
    
def lookup(speech):
    if speech == "": return True
    webbrowser.open_new_tab("https://www.google.com/search?q="+"+".join(speech.split(" ")))
    
    
def goto(speech, website=None):
    website = getElement(speech, "websites")
    if website == None: return True
    webbrowser.open_new_tab(website["website_url"])
    
    
def playMusic(speech):
    if speech == "": return True
    pywhatkit.playonyt(speech)

def stop(speech):
    if speech == "":
        speak("Au revoir.")
        exit()

def restart(speech):
    if speech == "":
        os.execl(sys.executable, sys.executable, "start.py")


# Usefull functions

def getElement(text, elemType):
    for elem in data[elemType]:
        for keyword in data[elemType][elem]["keywords"]:
            if keyword in text:
                if elemType == "websites":
                    return {
                        "website_name": elem,
                        "website_url": data[elemType][elem]["website_url"]
                    }
                elif elemType == "applications":
                    return {
                        "app_name": elem, 
                        "window_name": data[elemType][elem]["window_name"],
                        "command_to_start": data[elemType][elem]["commands_to_start"]
                    }

def getWindowID(window_name):
    window_list = subprocess.getoutput("wmctrl -l")
