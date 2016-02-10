'''
Created on Oct 6, 2015

@author: dipkumar.patel
'''
import time
from Text2speech.text_to_speech import *


def time_check():
    text_speech(time.strftime("%I"+"  and  "+"%M"+" PM"))