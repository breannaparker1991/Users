from flask_app import app
from flask import Flask, redirect, request, render_template 
from flask_app.models.user import User

@app.route('/')
def index():
  return redirect('/user')

@app.route('/user')
def user():
  all = User.get_all()
  return render_template("index.html", all = all)

@app.route('/user/new')
def new():
  return render_template ("new.html")
  
@app.route('/user/create', methods=["POST"]) 
def create():
  data = {
    "first_name": request.form["first_name"],
    "last_name": request.form["last_name"],
    "email": request.form["email"]
  }
  User.create(data)
  return redirect('/user')

@app.route('/user/edit/<int:id>')
def edit(id):
  data = {
    "id" : id
  }
  return render_template("edit.html", user = User.get_one(data))

@app.route('/user/update', methods=["POST"])
def update():
  User.update(request.form)
  return redirect('/user')
  
@app.route('/user/delete/<int:id>')
def delete(id):
  data = { 
      'id': id
      }
  User.delete(data)
  return redirect ('/user')

@app.route('/user/show/<int:id>')
def show(id):
  data = {
    "id" : id
  }
  return render_template("show.html", user = User.get_one(data))