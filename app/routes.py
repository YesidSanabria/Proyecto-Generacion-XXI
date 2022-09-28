import pyrebase
from flask import render_template
from flask import Flask
#######################################
import firebase_admin
from firebase_admin import credentials
#------ Importar archivos propios -------
import register.register as reg
import login.login as lg
import passw.passw as pw

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

#--------------------------------------REGISTRO E INICIO DE SESION-------------------------------------
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return lg.index()

#----------------------REGISTRARSE-----------------------------
@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    return reg.create_account()

#----------------------REINICIAR CONTRASEÑA----------------------
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    return pw.forgot_password()


############################ Pendientes de cambio ################################
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
