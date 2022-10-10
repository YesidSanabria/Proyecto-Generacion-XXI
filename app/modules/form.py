from doctest import register_optionflag
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


def form ():
    if (request.method == 'POST'):
        
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        cedula = request.form['cedula']
        edad = request.form['edad']
        genero = request.form['genero']
        email = request.form['correo_corporativo']
        gerencia = request.form['gerencia']
        direccion = request.form['direccion']
        nombre_gerente = request.form['nombre_gerente']
        celular_gerente = request.form['celular_gerente']
        universidad = request.form['universidad']
        carrera = request.form['carrera']
        tutor = request.form['nombre_tutor']
        correo_tutor = request.form['correo_tutor']
        celular_tutor = request.form['celular_tutor']
        eps = request.form['eps']
        contacto_emergencia = request.form['nombre_emergencia']
        numero_emergencia = request.form['numero_emergencia']
        correo_gerente = request.form['correo_gerente']
        regional = request.form['ciudad']

        data = {"Nombres": nombre,
            "Apellidos": apellidos,
            "Cedula": cedula,
            "Edad": edad,
            "Sexo": genero,
            "Correo corporativo": email,
            "Gerencia": gerencia,
            "Area de gerencia": direccion,
            "Nombre gerente": nombre_gerente,
            "Celular gerente": celular_gerente,
            "Universidad": universidad,
            "Carrera": carrera,
            "Nombre tutor": tutor,
            "Correo tutor": correo_tutor,
            "Celular tutor": celular_tutor,
            "EPS": eps,
            "Nombre emergencia": contacto_emergencia,
            "Numero emergencia": numero_emergencia,
            "Correo gerente": correo_gerente,
            "Regional": regional
        }
        crud.updateStudentData(email, data)
        mensaje = 'Los datos han sido guardados satisfactoriamente.'
        links = storage.child("profile_pictures/"+email).get_url(None)
        upload = request.files['upload']
        userr= request.form['userr']
        #print(upload.filename)
        if (upload.filename != ''):
            storage.child("profile_pictures/" + userr).put(upload)
            links = storage.child("profile_pictures/"+userr).get_url(None)
            #print("1")
        return render_template('view_personal_data.html', usuario=crud.getStudentInfo(email), smessage=mensaje,l=links)

    return render_template('formulario.html')