from flask import Flask,request
import jwt
users = {
  1:{
    "username":"iamkunal9",
    "password":"whoami",
  },
  2:{
    "username":"harshyadav",
    "password":"kuchbhi",
  },
  3:{
    "username":"muskaann.29",
    "password":"Sotu@123",
  },
  4:{
    "username":"ishajain",
    "password":"isha12",
},
  5:{
    "username":"kalika123",
    "password":"kalika2",
  },
  6:{
    "username":"kritig20",
    "password":"kayy2",
  },  
  7:{
    "username":"RituRAjs12",
    "password":"kyundu",
  },
  8:{'username':'Aditya@2',
     'password':'A2',
    }
}

app = Flask(__name__)


@app.route('/')
def index():    
  return 'Hello from Flask!'


chat = []
@app.route('/getdata/<data>',methods=['GET'])
def getData(data):
  to = jwt.decode(data,"whoami",algorithms=['HS256'])['username']
  dpost = []
  for i in chat:
    if to == i["to"]:
      dpost.append(i)
  return dpost


@app.route('/postdata',methods=['POST'])
def postData():
  From = request.json['from']
  to = request.json['to']
  message = request.json['message']
  exist = True
  if From==None or to == None or message == None or to==From:
    return {"success":False}
  
  for i in users:
    if to == users[i]["username"]:
      exist = False
      break
  if exist:
    return {"success":False,"reason":"No username Found"}
  decoded_value = jwt.decode(From,"whoami",algorithms=['HS256'])
  chat.append({
    "from":decoded_value['username'],
    "to":to,
    "message":message
  })
  return {"success":"ok"}



@app.route('/login',methods=['POST'])
def login():
  username  = request.json['username']
  password = request.json['password']
  for i in users:
    if username == users[i]["username"] and password == users[i]["password"]:
      encoded_jwt = jwt.encode({"username":username},"whoami",algorithm="HS256")
      return {"success":True,"jwt":encoded_jwt}
  return {"success":False}

app.run(debug=True,host='0.0.0.0', port=8000)
