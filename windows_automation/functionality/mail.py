'''
Created on Oct 6, 2015

@author: dipkumar.patel
'''

#====================================================================================
import os,urllib,feedparser
import email.utils,smtplib
from email.mime.text import MIMEText


from Speech2text.speech_to_text import speech_text
from Text2speech.text_to_speech import text_speech
from Main.continuos_loop import continuos_loop
from credential.email_credentials import get_password,get_userid, get_username, get_name
#=====================================================================================
#here write all your email ids..
email_directory={"dip":"dippatel1994@gmail.com","engineering":"engineeringkfunde@gmail.com","shivang":"shivaang13@gmail.com"}

def readmail():
    opener = urllib.FancyURLopener()
    _URL = "https://mail.google.com/gmail/feed/atom"
    f = opener.open(_URL)
    feed = f.read() 
    atom = feedparser.parse(feed)
    text_speech(atom.entries[2].title)
    continuos_loop()
    
def send_mail():
        text_speech("Tell the name of person to whom you want to send E-mail")
        temp=speech_text().split(" ")
        flag=True
        count=0 
        for word in temp:
            try:
                if flag==True:
                    mail_id=email_directory[word]
                    count+=1
                    flag=False
            except:
                pass
        if count==1:        
            print("mail id =",mail_id)
            to_email = mail_id          #raw_input('Recipient: ')
            servername = "smtp.gmail.com"
            username = get_userid()   
            password = get_password() 
            msg = MIMEText('checking mail')
            msg.set_unixfrom(get_username())
            msg['To'] = email.utils.formataddr(('Recipient', to_email))
            msg['From'] = email.utils.formataddr((get_name(), get_userid()))
            text_speech("Sir What I Write In Mail")
            msg['Subject'] = speech_text()
            server = smtplib.SMTP(servername)
            try:
                server.set_debuglevel(True)
                server.ehlo()
                if server.has_extn('STARTTLS'):
                    server.starttls()
                    server.ehlo() 

                server.login(username, password)
                server.sendmail('author@example.com', [to_email], msg.as_string())
            except:
                text_speech("Server Problem to send email")
            finally:
                server.quit()
                continuos_loop()
        else:
            text_speech("sorry sir no record found for this name") 
                
                
                