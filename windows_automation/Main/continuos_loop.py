'''
Created on Oct 6, 2015

@author: dipkumar.patel
'''
from Main.main import main
from Speech2text.speech_to_text import speech_text


def continuos_loop():
    try:
        result=speech_text()
        #To track program status i am printing it.
	#you can delete this print line,no problem.
        print("looping..",result)
        if result.lower()=="jarvis":
            main()
        else:
            continuos_loop()
           
    except LookupError:
        continuos_loop()