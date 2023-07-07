# Neuron

## What is this?
Neuron is a voice assistant created for Ubuntu that interacts with your voice using [Vosk](https://github.com/alphacep/vosk), an offline speech recognition API.

## Project structure

```
Neuron
├── assets
│   ├── data.json
│   └── rep.mp3
├── README.md
├── requierements.txt
├── scripts
│   ├── microphone.py
│   ├── process_commands.py
│   ├── process_speech.py
│   └── utils.py
├── start.py
└── test.py

```

## 💡 Features
- Starting & Closing applications
- Maximizing & Minimizing windows
- Writing what you tell him to write
- Managing the display of windows 
- Playing musics on youtube
- Looking up requests on google
- Directly opening websites
- Practical voice commands for developpement such as "stop" and "restart"


## ⚙️ Getting started
Due to some python libraries not being supported by docker such as "pywhatkit" I didn't set up a DockerFile. However, I'll try to make this installation easy.

### Clone repository

```
git clone https://github.com/Luzivog/Neuron.git
cd Neuron
```

### Install dependencies

```
sudo apt update
sudo apt install -y libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0

pip install -r requierements.txt
pip install pyaudio==0.2.11 --user
```

### Install model
Vosk models are available [here](https://alphacephei.com/vosk/models), for better results I choosed the "vosk-model-en-us-0.42-gigaspeech" but depending on your machine you may want to consider a lighter model.
After downloading the model, move it to Neuron folder and extract it into a folder that you rename "model".

### All set!
Open a command prompt, make sure you're in the Neuron directory, and run:
```
python start.py
```

## ✍️ Customize assistant
All the configuration is done in Neuron/assets/data.json
You can configure:
- Trigger words: Words that will trigger the assistant.
- Command words: Words that will trigger voice commands such as "type" for the writing action.
- Applications words: Words that refer to specific applications such as "vscode" for Visual Studio Code.
- Website words: Words that refer to specific websites such as "my favorite song" with a youtube link towards it.
