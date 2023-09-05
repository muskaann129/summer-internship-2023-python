from flask import Flask, request, render_template

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
  }
}

app = Flask(__name__)
@app.route('/')
def index():
        return render_template("login.html", data={"success": None})

@app.route("/login", methods=['POST'])
def login():
        username = request.form.get("uname")
        password = request.form.get("pass")
        print(password)
        for i in users:
                if username == users[i]["username"] and password == users[i]["password"]:
                        print(True)
                        return render_template("login.html", data={"success": True, "username":username})
        return render_template("login.html", data={"success": False})

app.run(debug = True)