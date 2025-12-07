import speech_recognition as sr


def speech_to_text() -> str:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        voice_data = r.recognize_google(audio)
        print("You said:", voice_data)
        return voice_data
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network.")
        return ""
