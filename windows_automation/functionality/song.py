'''
Created on Oct 6, 2015

@author: dipkumar.patel
'''
def open_song(string):
    a=""
#write your song collection here
    song_list=["we own it"]
    for word in song_list:
        if word in string:
             a=get_song_directory()+word+".mp3"
             temp="opening "+word+"song"
             text_speech(temp)
    continuos_loop()  