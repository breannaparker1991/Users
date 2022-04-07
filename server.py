from flask import Flask, render_template 
from env import KEY

app = Flask(__name__)
app.secret_key = KEY

app.route('/')
def index():
  return render_template("index.html")

if __name__ == "__main":
  app.run(debug=True)