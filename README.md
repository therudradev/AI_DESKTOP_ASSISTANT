# 🌟 AI Desktop Virtual Assistant

### *A Voice + Text Controlled Smart Assistant for Windows (Python)*

Your personal AI-powered desktop assistant — capable of understanding voice commands, speaking responses, fetching weather, opening apps, telling jokes, searching the web, and much more.
Built with **Python**, **Tkinter**, **Speech Recognition**, **Text-to-Speech**, and **Web Automation**.

---

## 🎯 Features

### 🔊 Voice Interaction

* Ask questions or give commands using your microphone.
* Uses `SpeechRecognition` + Google's speech engine.

### 💬 Text Interaction

* Type commands directly into the GUI.

### 🎙 AI Responses with Speech

* Assistant talks back using `pyttsx3`.

### 🌦 Weather Information

* Fetches real-time weather for any city.

### 🔍 Smart Web Search

* “Search for python tutorial” → Opens Google search.

### ▶️ YouTube Automation

* “Play lo-fi music on youtube”

### 📰 Latest News

* Opens Google News instantly.

### 😂 Fun Jokes

* Built-in humor engine to make your day.

### 📝 System App Control

* Open Notepad
* Open Calculator
* Open major websites

### 👋 Friendly UI

* Custom GUI designed using Tkinter.

---

## 📸 Screenshots (Add Your Images)

> Replace these placeholder paths with your actual project screenshots.

| Assistant Window    | Voice Interaction     |
| ------------------- | --------------------- |
| ![](assets/gui.png) | ![](assets/voice.png) |

---

## 🛠️ Technologies Used

| Purpose          | Library                  |
| ---------------- | ------------------------ |
| GUI              | Tkinter                  |
| Speech to Text   | SpeechRecognition        |
| Text to Speech   | pyttsx3                  |
| Weather Scraping | requests + BeautifulSoup |
| Automation       | webbrowser, OS commands  |
| Image Handling   | Pillow (optional)        |

---

## 📂 Project Structure

```
AI_DESKTOP_ASSISTANT/
│
├── action.py
├── GUI.py
├── speech_to_text.py
├── text_to_speech.py
├── weather.py
│
├── /image
│   └── assistant.png
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI_Desktop_Virtual_Assistant.git
cd AI_Desktop_Virtual_Assistant
```

### 2️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

If you're not using a `requirements.txt`, install manually:

```bash
pip install speechrecognition pyaudio pyttsx3 requests beautifulsoup4 pillow
```

> ⚠️ **Note:** On some systems, `pyaudio` requires OS-level installation of **portaudio**.

---

## ▶️ Run the Assistant

```bash
python GUI.py
```

---

## 🎤 Try These Commands

### 🧠 General

* "hello"
* "what is your name?"
* "how are you?"

### ⏰ Time

* "what time is it?"

### 🎧 Media

* "play lo fi music on youtube"

### 🌦 Weather

* "what's the weather?"
* "weather in delhi"

### 🔍 Search

* "search for python tutorial"

### 📰 News

* "show me news"

### 😄 Fun

* "tell me a joke"

### 🧮 Apps

* "open calculator"
* "open notepad"

### ❌ Exit

* "shutdown"

---

## 🌍 Cross-Platform Notes

| Feature              | Windows | Linux              | macOS            |
| -------------------- | ------- | ------------------ | ---------------- |
| GUI                  | ✔️      | ✔️                 | ✔️               |
| Voice Input          | ✔️      | ✔️ Requires config | ✔️               |
| Notepad / Calculator | ✔️      | Replace commands   | Replace commands |

If you'd like a cross-platform version, I can generate one.

---

## 🧩 Upcoming Improvements (Optional Ideas)

* Wake-word activation (“Hey Assistant”)
* ChatGPT API integration
* Notifications & reminders
* Play local music
* Open specific folders / files
* Face recognition login
* Better animated GUI

Want these added? Just tell me!

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open Issues or Pull Requests.

---

## ⭐ Show Your Support

If you like this project:

### 👉 **Please give the repository a star! ⭐**

---
