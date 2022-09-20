import pyrebase
from flask import render_template, request, redirect, session
#from app import app
from flask import Flask
import os

app = Flask(__name__)

config = {

  "apiKey": "AIzaSyDBP7Is2dfzsIzLA-o222p2K2VxoSsFw0c",

  "authDomain": "generacion-xxi.firebaseapp.com",

  "databaseURL": "https://generacion-xxi-default-rtdb.firebaseio.com",

  "projectId": "generacion-xxi",

  "storageBucket": "generacion-xxi.appspot.com",

  "messagingSenderId": "347199104837",

  "appId": "1:347199104837:web:e859d53b27b23d1024c02c",

  "measurementId": "G-YNKS2S6VJT"

}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
            email = request.form['name']
            password = request.form['password']
            try:
                auth.sign_in_with_email_and_password(email, password)
                #user_id = auth.get_account_info(user['idToken'])
                #session['usr'] = user_id
                return render_template('home.html')
            except:
                unsuccessful = 'Please check your credentials'
                return render_template('index.html', umessage=unsuccessful)
    return render_template('index.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if (request.method == 'POST'):
            email = request.form['name']
            password = request.form['password']
            auth.create_user_with_email_and_password(email, password)
            return render_template('index.html')
    return render_template('create_account.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if (request.method == 'POST'):
            email = request.form['name']
            auth.send_password_reset_email(email)
            return render_template('index.html')
    return render_template('forgot_password.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
