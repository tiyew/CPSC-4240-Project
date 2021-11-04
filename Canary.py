#!/usr/bin/env python
import smtplib
from email.message import EmailMessage
import subprocess

# Parse the list of accessed files for the name of the file or files 
#Files holds the list of files we are checking for 
files = ['x.txt']
user_email = "anemail@email.com"

#Command 1: Getting the List of recently opened files piped into a file 
#"find . -type f -amin -30"
print("Getting list of files opened in the last 30 minutes with the find command")
file = open("recent_files.txt","w+")
subprocess.call(["find",".","-type","f","-amin","-30"], stdout=file)

# Parsing the file for matches of the text file
file.seek(0)
lines = file.readlines()

#If there were no files opened recently 
if not lines:
    email = EmailMessage()
    email.set_content("Good Day, The Canary token script ran and there were no files opened on your system in the last 30 minutes your files are safe")
    email['Subject'] = "Your Token Report"
    email['From'] = "ouremail@user.com" #The example Email will go here 
    email['To'] = user_email #The users Email will go here
    #This will send the email
    s = smtplib.SMTP('localhost')
    s.send_message(email)
    s.quit()
else:
    found = []
    for line in lines: 
        if line in files:
            found.append(line)
    
    email = EmailMessage()
    email.set_content("Hello user \n unfourtnaetly these files: %s were opened on your system, if this wasn't you please take the proper steps to secure your system",found)
    email['Subject'] = "Your Token Report"
    email['From'] = "ouremail@user.com" #The example Email will go here 
    email['To'] = user_email #The users Email will go here
    #This will send the email
    s = smtplib.SMTP('localhost')
    s.send_message(email)
    s.quit()
    file.close()

print("Script ran successfully email sent to %s",email['from'])









