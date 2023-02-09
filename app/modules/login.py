import pyrebase
from flask import render_template, request, session
import modules.crud as crud
from urllib.request import urlopen

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
        # Inicialización de parámetros.
        req = ''
        cantidad = ''
        emails = ''
        keys =''
        cuenta = ''
        file = ''
        #######################################
        if (admin == email):
            putos = 'admin.html'
            user = crud.getAllStudents()
            [keys, emails, cantidad] = crud.getStudentsData([])
            cuenta = crud.amountCards()
            emails = [x.lower() for x in emails]
             #arreglo con los campos de imagenes de cada persona
            links = crud.getImagesURL(emails)
            
        elif(user['Nombres'] == ''):
            putos = 'formulario.html'
            links = crud.getImagesURL([email])
        else:
            putos = 'view_personal_data.html'
            file = crud.urlDevelopmentPlan(user['Cedula'])
            links = crud.getImagesURL([email])
            # Verificar si hay un plan de desarrollo
            try:
                urlopen(file)
            except:
                file = False
        try:
#--------------------INICIAR SESION---------------------------------                
            auth.sign_in_with_email_and_password(email, password)            
            #user_id = auth.get_account_info(user['idToken'])
            session['username'] = email
            #return render_template('formulario.html', user=user)
            return render_template(putos, nav_activo=1, usuario=user, opcion=options, l=links, keys=keys, cantidadDatos=cantidad, cuent=cuenta, file=file)
            
        except:
            unsuccessful = 'Su correo electrónico o contraseña estan mal digitados, vuelva a intentarlo.'
            return render_template('index.html', umessage=unsuccessful)
    session.pop('username', None)
    return render_template('index.html')
