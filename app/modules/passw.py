import pyrebase
from flask import render_template, request
#import firebase_admin
from firebase_admin import auth
import modules.send_email as mail

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
#auth = firebase.auth()

def forgot_password():
    if (request.method == 'POST'):
        action_code_settings = auth.ActionCodeSettings(
            url='https://www.example.com/finishSignUp?cartId=1234',
            handle_code_in_app=True,
        )
        email = request.form['name']
        print(email)
        try:
            link = auth.generate_password_reset_link(email, action_code_settings)
            mail.send_custom_email(email,link)
            return render_template('index.html')
        except:
            unsuccessful = 'Cambios de contraseña excedidos, intentelo mas tarde'
            return render_template('index.html', umessage=unsuccessful)
        # # Construct password reset email from a template embedding the link, and send
        # # using a custom SMTP server.
        
        #auth.send_password_reset_email(email)
    return render_template('forgot_password.html')