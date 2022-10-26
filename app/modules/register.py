import pyrebase
from flask import render_template, request
import modules.crud as crud

from flask_mail import Mail, Message

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

def accCreationExc(email1, email2, pass1, pass2):
    acc = {'email': email1, 'password': pass1}
    acc['error'] = 'Este correo ya está asociado a una cuenta.'
    if (email1 == '') | (email2 == '') | (pass1 == '') | (pass2 == ''):
        acc['error'] = 'Rellene todos los campos.'
    elif email1 != email2:
        acc['error'] = 'Los correos no coinciden.'
        acc['email'] = ''
    elif pass1 != pass2:
        acc['error'] = 'Las contraseñas no coinciden.'
        acc['password'] = ''
    return acc

def create_account():
    if (request.method == 'POST'):
        email = request.form['name']
        password = request.form['password']
        conf_email = request.form['conf_name']
        conf_password = request.form['conf_password']
        # Confirmación de correo y contraseña
        acc = accCreationExc(email, conf_email, password, conf_password)
        unsuccessful = acc['error']
        email = acc['email']
        password = acc['password']
        if True:
            auth.create_user_with_email_and_password(email, password)
            crud.createNewStudent(email)                                                          
            return render_template('index.html')
        else:
        # except:
            return render_template('create_account.html', umessage=unsuccessful)
    return render_template('create_account.html')
