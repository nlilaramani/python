from flask import Flask, request, render_template,jsonify,abort
import userdb

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

import users
app.register_blueprint(users.bp)
import errors
app.register_blueprint(errors.bp)
