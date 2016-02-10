'''
Created on Oct 6, 2015

@author: dipkumar.patel
'''

import speech_recognition as sr

def speech_text():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        audio = r.listen(source)
        print("You said " + r.recognize(audio))
        return r.recognize(audio)