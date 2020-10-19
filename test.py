# with open("passwords.txt","r") as file:
#     passwords=file.read()

# list1=passwords.strip('\n').split('\n')
# # strip is used not to get the empty string at the last while spliting it with new line character
# print(list1)
import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login('godofthunderthor583@gmail.com', 'Test@1234')
