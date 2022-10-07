import pyrebase
from flask import render_template, request
import modules.crud as crud

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

admin = "sspg.xxi@gmail.com"

def index():
    if (request.method == 'POST'):
        email = request.form['name']
        password = request.form['password']
        #######################################
        user = crud.getStudentInfo(email)
        options = crud.options
        #######################################
        if (admin == email):
            putos = 'admin.html'
            user = crud.getAllStudents()
        elif(user['Nombres'] == ''):
            putos = 'formulario.html'
        else:
            putos = 'view_personal_data.html'
        try:
#--------------------INICIAR SESION---------------------------------                
            auth.sign_in_with_email_and_password(email, password)
            #user_id = auth.get_account_info(user['idToken'])
            #session['usr'] = user_id
            #return render_template('formulario.html', user=user)

            return render_template(putos, usuario=user, opcion=options)
            
        except:
            unsuccessful = 'Su correo electrónico o contraseña estan mal digitados, vuelva a intentarlo.'
            return render_template('index.html', umessage=unsuccessful)
    return render_template('index.html')