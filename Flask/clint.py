from flask import Flask
import requests
import jwt

def login(username,password):
  resp = requests.post("https://flask-internship.iamkunal9.repl.co/login", json={'username':username, 'password': password}).json()
  return resp

jwt = None
while True:
  username = input("Enter Username: ")
  password = input("Enter Password: ")      
  rsp = login(username, password)
  if rsp['success']:
        jwt = rsp['jwt']
        break
        
check = None
while check!=3 :
    print("1. Enter 1 to fetch data")
    print("2. Enter 2 to send message")
    print("3. Enter 3 to exit")
    check = int(input("Enter our choise (1,2,3): "))
    
    if check==1:
        d=[]
        message = requests.get(f"https://flask-internship.iamkunal9.repl.co/getdata/{jwt}")
        reply = message.json()
        for i in reply:
            if i['to']==username:
                d.append(i)
        if len(d)>0:
            for i in d:
                print(f"from {i['from']}\nmessage: {i['message']}")
        else:
            print("No message found")
    
    elif check==2:
        to = input("Enter the username to which you want to send message: ")
        message = input(f"Enter your message to username {to}: ")
        data = {'from': jwt, 'to': to, 'message': message}
        resp = requests.post("https://flask-internship.iamkunal9.repl.co/postdata",json=data).json()
        if resp['success'] == "ok":
          print("Data sent successfully")
        else:
          print("Error while sending")
    
    elif check==3:
        break
        
    elif check>4:
        print("Invalid Input! Please try again")
        continue
print("Thank you!!")