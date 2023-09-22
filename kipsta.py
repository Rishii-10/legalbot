from googletrans import Translator
import pygame 
from gtts import gTTS
import pyttsx3 as pyt
def text_to_speech(text, filename): #can all be implemented as one ultimate function simple 
    #instead of parameters 
    a=ord(text[0])
    if(a<128):
        tts = gTTS(text, lang='en')   
#function overloading ofcourse  cant in python apprently so yeh
    else:
        tts = gTTS(text, lang='hi')
    tts.save(filename)
def translate_to_hindi(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='hi')
    return translated_text.text
english_text = str(input())
filename = "output1.mp3"#input of your filename
file = "output2.mp3"
#problem with meaing og the name so in between if there are any capital letters
hindi_translation = translate_to_hindi(english_text)
print(f"{hindi_translation}")#now to play these basically a file is downloaded