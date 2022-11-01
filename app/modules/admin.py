import pyrebase
from flask import render_template, request
from firebase_admin import db
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

def admin():
    if (request.method == 'POST'):
        ruta = request.form ["ruta"]
        if ruta == "admin":
            putos = 'admin.html'
            user = crud.getAllStudents()
            [keys, emails, cantidad] = crud.getStudentsData()
            cuenta = crud.amountCards()
            emails = [x.lower() for x in emails]
            req = crud.getRequests()
             #arreglo con los campos de imagenes de cada persona
            links = crud.getImagesURL(emails)

            if True:
                return render_template(putos, usuario=user, l=links, req=req, keys=keys, cantidadDatos=cantidad, cuent=cuenta)

        elif ruta == "infopract":
            putos = 'infopract.html'
            user = crud.getStudentInfo(request.form["yave"])
            foto = crud.getImagesURL([request.form["foto"]])
            [keys, emails, cantidad] = crud.getStudentsData()
            cuenta = crud.amountCards()
            emails = [x.lower() for x in emails]
            req = crud.getRequests()
             #arreglo con los campos de imagenes de cada persona
            links = crud.getImagesURL(emails)

            if True:
                
                return render_template(putos, usuario=user, l=foto)

    return render_template('admin.html')    









