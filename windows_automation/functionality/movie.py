'''
Created on Oct 6, 2015

@author: dipkumar.patel
'''
def open_movie(string):
   a=""
   #update your movie collection here...
   movie_list=["hulk","avengers","superman","spiderman"]
   for word in string:
      if word in movie_list:
         a=get_movie_directory()+"/"+word+".mkv"
         s="sir, opening"+word+"movie, it's a awesome movie , enjoy it"
         text_speech(s)
         os.startfile(a)
         continuos_loop()