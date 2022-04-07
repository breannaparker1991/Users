from flask import Flask, render_template 
from env import KEY
from user import User

app = Flask(__name__)
app.secret_key = KEY

@app.route('/')
def index():
  all = User.get_all()
  return render_template("index.html", users = all)

@app.route('/user/create')
def user_create():
  return render_template ("user.html")
  

if __name__ == "__main__":
  app.run(debug=True)