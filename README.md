# 🧠 Basic Offline Chatbot

This is a lightweight, fully offline personal chatbot built using Python, Tkinter, and TinyLlama via Ollama. It supports both GUI input and keyboard (Enter) interaction, and stores chat history locally in a json file named as "Chat_history.json".
As this is a very simple and basic chatbot so it is only able to do chatting. If you want it so solve numeric problems or you want to seek informations from it, it is not a good choice.
The models that run offline will take large space. And this models is build by keeping in mind that it could take least space. So this is the reason that this Chatbot is a Low Power Chatbot, but besides it you can run it in your own computer fully offline for free.

## 📝 NOTE: To run this, you must need atleast 8GB RAM.

## 💻 Features
- Works offline using the TinyLlama model
- Friendly GUI built with Tkinter
- Resettable conversation memory
- Local chat history
- Custom icons and styling

## 📶 Steps to run Chatbot
- first step to go to the website and download the OLLAMA: https://ollama.com/
- Second step is to open cmd and run this command: 
```
ollama run tinyllama
```
- After doing all this you are now free to use the Chatbot App or use the Source code.

## 🗂 Project Folder Structure
```
Basic Offline Chatbot/
│
├── Chatbot App/                 # Compiled app files
│   ├── Personal Chatbot Application.exe       # Actual Application file
│   ├── Logo image.png
│   ├── Chatbot icon.png
│   ├── Chat_history.json
│
├── Source Code/                 # Editable Python code
│   ├── Chatbot.py
│   ├── Logo image.png
│   ├── Chatbot icon.png
│   ├── Chat_history.json
│
├── README.md                    # Instructions
└── LICENSE
```

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
