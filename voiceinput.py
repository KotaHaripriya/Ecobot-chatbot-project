import speech_recognition as sr

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = r.listen(source)
    try: return r.recognize_google(audio)
    except sr.UnknownValueError: return "Could not understand audio"
    except sr.RequestError: return "Voice recognition problem"

