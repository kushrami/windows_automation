'''
Created on Oct 6, 2015

@author: dipkumar.patel
'''

def readnews(key):
    url=["http://news.google.com/?output=rss","http://indianexpress.com/rss/721/india.xml"]
    feed = feedparser.parse(url)
    entries = feed.entries
    collect=[]
    a=0
    for entry in entries:
        if a<6:
           text_speech(entry.title)
           a=a+1
    if a==0:
       text_speech("there is no new news")
    continuos_loop() 