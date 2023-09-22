import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    
    # Record audio from the microphone
    with sr.Microphone() as source:
        print("Please speak something...")
        audio = recognizer.listen(source)
    
    # Use Google Web Speech API to recognize the audio
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results; check your network connection.")

if __name__ == "__main__":
    speech_to_text()
