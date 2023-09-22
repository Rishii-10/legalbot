from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")  

if __name__ == "__main__":
    text = input()
    text_to_speech(text)

import threading
import playsound

class AudioPlayer(threading.Thread):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.stop_event = threading.Event()

    def run(self):
        playsound.playsound(self.filename)
        AudioPlayer.stop(self)
        
    def stop(self):
        self.stop_event.set()

if __name__ == "__main__":
    player = AudioPlayer("output.mp3")
    player.start()
    