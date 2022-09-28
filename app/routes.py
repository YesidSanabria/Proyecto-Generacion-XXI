from distutils.log import error
import pyrebase
from flask import render_template, request, redirect, session
#from app import app
from flask import Flask
#######################################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
########################################

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

##########################################
cred = credentials.Certificate("app/config/generacion-xxi-firebase-adminsdk-iwq0c-bc2e550415.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://generacion-xxi-default-rtdb.firebaseio.com/'})
##########################################
admin = "sspg.xxi@gmail.com"


#--------------------------------FUNCIONES--------------------------------------------
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

#--------------------------------------REGISTRO E INICIO DE SESION-------------------------------------
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        email = request.form['name']
        password = request.form['password']
        #######################################
        ref = db.reference('Estudiantes')
        user = ref.child(email.replace('.', '')).get()
        print(user)
        putos = 'view_personal_data.html'
        #######################################
        if (admin == email):
            putos = 'admin_view.html'
        try:
#--------------------INICIAR SESION---------------------------------                
            auth.sign_in_with_email_and_password(email, password)
            #user_id = auth.get_account_info(user['idToken'])
            #session['usr'] = user_id
            #return render_template('formulario.html', user=user)
            return render_template(putos, usuario=user)
            
        except:
            unsuccessful = 'Su correo electrónico o contraseña estan mal digitados, vuelva a intentarlo.'
            return render_template('index.html', umessage=unsuccessful)
    return render_template('index.html')

#----------------------REGISTRARSE-----------------------------
@app.route('/create_account', methods=['GET', 'POST'])
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
        try:
            auth.create_user_with_email_and_password(email, password)
            return render_template('index.html')
        except:
            return render_template('create_account.html', umessage=unsuccessful)
    return render_template('create_account.html')

#----------------------REINICIAR CONTRASEÑA----------------------
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
#--------------------------------------REGISTRO E INICIO DE SESION-------------------------------------
@app.route('/admin_view', methods=['GET', 'POST'])
def admin_view():
    return render_template('admin_view.html')

#--------------------------------------FORMULARIO-------------------------------------
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    return render_template('formulario.html')


#---------------------------------PROGRAMAR ARRIBA DEL IF DE ABAJO----------------------------------
if __name__ == '__main__':
    app.run(debug = True)
