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
storage = firebase.storage() #linea del storage
auth = firebase.auth()
def orderOptions(email):
    options = crud.options
    data = crud.getStudentInfo(email)
    genre = data['Sexo']
    city = data['Regional']
    out = {
        'sexo': [genre],
        'regional': [city]
    }
    for i in options['sexo']:
        if i != genre:
            out['sexo'].append(i)
    for i in options['regional']:
        if i != city:
            out['regional'].append(i)
    return out


def view_personal_data():
    if (request.method == 'POST'):
        ruta = request.form ["ruta"]
        if ruta == "pract":
            user = crud.getStudentInfo(request.form["email"])
            links = crud.getImagesURL([request.form["email"]])
            cedula = str(request.form ["cedula"])
            storage.child("development_plan/" + "plan_desarrollo_" + cedula + ".pdf").download(r"/","plan_desarrollo_" + cedula + ".pdf")
            try:
                opciones = orderOptions(user)
            except:
                opciones = crud.options
            return render_template('view_personal_data.html', usuario=user, opcion=opciones,l=links)
        elif ruta == "actu":
            putos = 'formulario.html'
            options = crud.options          
            user = crud.getStudentInfo(request.form['actuali'])
            links = crud.getImagesURL([request.form["actuali"]])
            return render_template(putos, usuario= user, opcion=options, l=links)

    
    return render_template('view_personal_data.html')