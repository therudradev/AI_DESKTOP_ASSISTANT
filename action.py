import datetime
import os
import random
import urllib.parse
import webbrowser

import text_to_speech
import weather


# A few simple jokes
JOKES = [
    "Why did the computer go to the doctor? Because it had a virus.",
    "Why don’t programmers like nature? It has too many bugs.",
    "I would tell you a UDP joke, but you might not get it.",
    "Why do Java developers wear glasses? Because they don't C sharp.",
    "My boss told me to have a good day, so I went home."
]


def Action(data: str) -> str:
    # Make sure we always have a safe string
    if not isinstance(data, str):
        data = "" if data is None else str(data)

    user_data = data.lower().strip()
    reply = "I'm not able to understand."

    # -------- BASIC CONVERSATION --------
    if ("what is your name" in user_data or
        "what's your name" in user_data or
        "what is you name" in user_data):
        reply = "My name is virtual assistant."

    elif "hello" in user_data or "hye" in user_data or "hi" in user_data:
        reply = "Hey, sir. How can I help you?"

    elif "good morning" in user_data:
        reply = "Good morning sir."

    elif "how are you" in user_data:
        reply = "I am functioning within normal parameters. How are you, sir?"

    # -------- TIME --------
    elif "time now" in user_data or "what time" in user_data or "current time" in user_data:
        current_time = datetime.datetime.now()
        reply = f"The time is {current_time.hour:02d} hours {current_time.minute:02d} minutes."

    # -------- SHUTDOWN / EXIT --------
    elif "shutdown" in user_data or "quit" in user_data or "close" in user_data or "exit" in user_data:
        # IMPORTANT: GUI checks exactly for 'ok sir'
        reply = "ok sir"

    # -------- WEATHER --------
    elif "weather" in user_data:
        # You can say: what's the weather in delhi
        city = "patna"
        trigger = "weather in "
        if trigger in user_data:
            # Get text after 'weather in '
            city = user_data.split(trigger, 1)[1].strip()
            if not city:
                city = "patna"

        ans = weather.weather(city)
        reply = f"Current weather in {city} is {ans}"

    # -------- JOKES --------
    elif "joke" in user_data or "make me laugh" in user_data:
        reply = random.choice(JOKES)

    # -------- WEB SEARCH --------
    elif user_data.startswith("search ") or "search for " in user_data:
        # Examples:
        # "search python tutorial"
        # "search for best music"
        if "search for " in user_data:
            query = user_data.split("search for ", 1)[1].strip()
        else:
            query = user_data.split("search ", 1)[1].strip()

        if query:
            encoded_query = urllib.parse.quote_plus(query)
            url = f"https://www.google.com/search?q={encoded_query}"
            webbrowser.open(url, new=2)
            reply = f"Searching Google for {query}"
        else:
            reply = "What should I search for, sir?"

    # -------- YOUTUBE SEARCH --------
    elif "youtube" in user_data:
        # Examples:
        # "play lo-fi music on youtube"
        # "open youtube"
        words_after = ""
        if "on youtube" in user_data:
            words_after = user_data.split("play", 1)[-1]
            words_after = words_after.replace("on youtube", "").strip()
        elif "youtube" in user_data and "play" in user_data:
            # "play despacito youtube"
            parts = user_data.split("play", 1)[1]
            words_after = parts.replace("youtube", "").strip()

        if words_after:
            encoded_query = urllib.parse.quote_plus(words_after)
            url = f"https://www.youtube.com/results?search_query={encoded_query}"
            webbrowser.open(url, new=2)
            reply = f"Playing {words_after} on YouTube."
        else:
            webbrowser.open("https://www.youtube.com", new=2)
            reply = "Opening YouTube."

    # -------- NEWS --------
    elif "news" in user_data:
        webbrowser.open("https://news.google.com", new=2)
        reply = "Here are the latest news headlines."

    # -------- OPEN WEBSITES --------
    elif "open google" in user_data:
        webbrowser.open("https://google.com/", new=2)
        reply = "google.com is now ready for you."

    elif "open facebook" in user_data:
        webbrowser.open("https://facebook.com", new=2)
        reply = "Opening Facebook."

    elif "open instagram" in user_data:
        webbrowser.open("https://instagram.com", new=2)
        reply = "Opening Instagram."

    elif "play music" in user_data or "open gaana" in user_data:
        webbrowser.open("https://gaana.com/", new=2)
        reply = "gaana.com is now ready for you."

    # -------- OPEN DESKTOP APPS (WINDOWS) --------
    elif "open notepad" in user_data:
        try:
            os.system("notepad.exe")
            reply = "Opening Notepad."
        except Exception:
            reply = "Sorry, I could not open Notepad."

    elif "open calculator" in user_data or "open calc" in user_data:
        try:
            os.system("calc.exe")
            reply = "Opening Calculator."
        except Exception:
            reply = "Sorry, I could not open Calculator."

    # (keep the default reply defined at top if none matched)

    # Speak and return reply
    text_to_speech.text_to_speech(reply)
    return reply
