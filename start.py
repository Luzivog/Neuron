import os, subprocess

audio_devices = subprocess.getoutput("python3 ./scripts/microphone.py -l")
number = None

for audio_device in audio_devices.split("\n"):
    if " default" in audio_device:
        number = [el for el in audio_device.split(" ") if el != '' and el != '*'][0]
        break

os.system(f"python3 ./scripts/microphone.py -d {number}")