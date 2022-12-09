import pyrebase
from flask import render_template, request, Flask, session
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
storage = firebase.storage() #linea del storage
auth = firebase.auth()


#storage.child("profile_pictures/new.jpeg").put(r"C:\Users\ic5705b\Documents\GitHub\Proyecto-Generacion-XXI\app\descarga.jpeg") #cargar imagenes al storage
# storage.child("profile_pictures/new.jpeg").download(r"C:\Users\ic5705b\Documents\GitHub\Proyecto-Generacion-XXI\app","example.jpeg") #descargar las imagenes obtenidas del storage 
# print(storage.child("profile_pictures/new.jpeg").get_url(None)) #Obtener la url de la ruta de las imagenes

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
            rut = 'admin.html'
            user = crud.getAllStudents()
            [keys, emails, cantidad] = crud.getStudentsData([])
            cuenta = crud.amountCards()
            emails = [x.lower() for x in emails]
            req = crud.getRequests()
             #arreglo con los campos de imagenes de cada persona
            links = crud.getImagesURL(emails)
            
        elif(user['Nombres'] == ''):
            rut = 'formulario.html'
            links = crud.getImagesURL([email])
        else:
            rut = 'view_personal_data.html'
            file = crud.urlDevelopmentPlan(user['Cedula'])
            links = crud.getImagesURL([email])
        try:
#--------------------INICIAR SESION---------------------------------                
            auth.sign_in_with_email_and_password(email, password)            
            #user_id = auth.get_account_info(user['idToken'])
            session['username'] = email
            #return render_template('formulario.html', user=user)
            return render_template(rut, usuario=user, opcion=options, l=links, req=req, keys=keys, cantidadDatos=cantidad, cuent=cuenta, file=file)
            
        except:
            unsuccessful = 'Su correo electrónico o contraseña estan mal digitados, vuelva a intentarlo.'
            return render_template('index.html', umessage=unsuccessful)
    session.pop('username', None)
    return render_template('index.html')
