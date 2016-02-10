'''
Created on Oct 6, 2015

@author: dipkumar.patel
'''

def open_software(string):
     software_list=["chrome","excel","word","notepad","wordpad","powerpoint","processing","putty","mspaint"]
     for software_name in string:
          if software_name in software_list:
              s="sir, i am opening "+software_name+" for you"
              text_speech(s)
              arg="start "+software_name+".exe"
              os.system(arg)
              continuos_loop()