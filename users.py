from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import userdb
bp = Blueprint('users', __name__, url_prefix='/users')
@bp.route('/register', methods=['GET','POST'])
def register_user():
        if request.method=='GET':
                return render_template("user_registration.html")
        else:
                result=userdb.register(request.form['fname'],request.form['lname'],request.form['email'],request.form['username'],request.form['password'])
                if result:
                        return "User successfully registered!, <a href='login'>Login</a>"
                else:
                        return 'Error registering user'
@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login_form.html")
    else:
        uname=request.form['username']
        pwd=request.form['password']
        return uname+", "+pwd

