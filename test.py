import os

# adb connect 192.168.1.134:5555 & scrcpy & disown

output = os.popen("adb connect 192.168.1.134:5555").read()
if "failed" in output:
    print("Connexion au téléphone échouée.")
else:
    output = os.popen("scrcpy & disown").read()