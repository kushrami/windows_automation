'''
Created on Oct 6, 2015

@author: dipkumar.patel
'''

import pyttsx

def text_speech(text):
    engine = pyttsx.init()
    engine.setProperty('rate', 150)
    voice=pyttsx.voice.Voice
    voice.id= 0x0000000002CC9550
    engine.setProperty('voice', voice.id)
    s=text
    engine.say(s)
    engine.runAndWait()