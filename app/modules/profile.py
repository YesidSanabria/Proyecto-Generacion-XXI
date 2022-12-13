import pyrebase
from flask import render_template, request, session
import modules.crud as crud
import modules.login as lg



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

def orderOptions(email):
    options = crud.options
    data = crud.getStudentInfo(email)
    genre = data['Sexo']
    city = data['Regional']
    dirCorp = data['Area de gerencia']
    out = {
        'sexo': [genre],
        'regional': [city],
        'direccion': [dirCorp]
    }
    for i in options['sexo']:
        if i != genre:
            out['sexo'].append(i)
    for i in options['regional']:
        if i != city:
            out['regional'].append(i)
    for i in options['direccion']:
        if i != dirCorp:
            out['direccion'].append(i)
    return out


def view_personal_data():
    if (request.method == 'POST'):
        ruta = request.form ["ruta"]
        if ruta == "pract":
            user = crud.getStudentInfo(request.form["email"])
            links = crud.getImagesURL([request.form["email"]])
            file = crud.urlDevelopmentPlan(user['Cedula'])
            try:
                if request.form['email'] in session["username"]:
                    return render_template('view_personal_data.html', usuario=user, opcion=opciones,l=links,file=file)
                else: 
                    return render_template('index.html')
            except:
                return render_template('index.html')
        elif ruta == "actu":
            putos = 'formulario.html'
            user = crud.getStudentInfo(request.form['actuali'])
            links = crud.getImagesURL([request.form["actuali"]])
            # print(request.form['actuali'])
            # print(session["username"])
            try:
                opciones = orderOptions(user['Correo corporativo'])
            except:
                opciones = crud.options  
            try:                      
                if request.form['actuali'] in session["username"]:
                    return render_template(putos, usuario= user, opcion=opciones, l=links)
                else:
                    return render_template('index.html')
            except:
                return render_template('index.html')
    return render_template('view_personal_data.html')

def download_file():
    if (request.method == 'POST'):
        cedula = request.form ["cedula"]
        return crud.downloadDevelopmentPlan(cedula)
    