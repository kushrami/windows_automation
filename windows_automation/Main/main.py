'''
Created on Oct 6, 2015

@author: dipkumar.patel
'''
from functionality import jokes,mail,movie,news,software,song
from Text2speech.text_to_speech import *
from Speech2text.speech_to_text import * 
from Main import time_check,continuos_loop

def main():
    try:
        text_speech("sir")
        result=speech_text()
        temp=result.split(" ")
        software.open_software(temp)
        if "movie" in temp:
            movie.open_movie(temp)
        elif "mail" in temp:    
            mail.readmail()
        elif "news" in temp:
            key=temp[-1]
            news.readnews(key);
        elif "time" in temp:
            time_check()
        elif "song" in result:
            song.open_song(result)
        elif "send" in result:
            mail.send_mail()
        elif "jokes" in result:
            jokes()
        else:
            continuos_loop.continuos_loop() 
             
    except LookupError:
        print("Could not understand audio")
        text_speech("sorry sir will you please repeat again")
        continuos_loop.continuos_loop()


      

if __name__=="__main__":
    text="Good evening.."
    text_speech(text)
    main()
