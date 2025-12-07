import pyttsx3

# Initialize engine once at import time
_engine = pyttsx3.init()
_rate = _engine.getProperty('rate')
_engine.setProperty('rate', _rate - 70)


def text_to_speech(text):
    # Ensure we always send a string to the engine
    _engine.say(str(text))
    _engine.runAndWait()
