from flask import Flask, redirect, request, render_template 
from env import KEY
from user import User

app = Flask(__name__)
app.secret_key = KEY

@app.route('/')
def index():
  all = User.get_all()
  return render_template("index.html", all = all)

@app.route('/user/new')
def new():
  return render_template ("user.html")
  
@app.route('/user/create', methods=["POST"]) 
def create_user():
  data = {
    "first_name": request.form["first_name"],
    "last_name": request.form["last_name"],
    "email": request.form["email"]
  }
  User.create(data)
  return redirect('/')




if __name__ == "__main__":
  app.run(debug=True)