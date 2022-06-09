from email import message
from urllib import response
from flask import Flask, render_template, jsonify, request, redirect, url_for

from flask_cors import CORS
from chat import searching
from sqlalchemy import true
import subprocess

subprocess.call("chat.py", shell=True) 
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print(request.form['username'])
        if request.form['username'] != 'a' or request.form['password'] != '':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('connected.html', value=request.form['username'])
    return render_template('login.html', error=error)
@app.route('/')
def index():
    return render_template('index.html')
@app.post('/predict')
def predict():
    import subprocess

    subprocess.call("chat.py", shell=True)
    from function import Gsearch
    
    while True:
        login()
        text=request.get_json().get("message")
        response=searching(text)
        message ={"answer":response}
        return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
