from email import message
from operator import pos
import pyrebase
from flask import jsonify, render_template, request
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


def form ():
    if (request.method == 'POST'):
        
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        cedula = request.form['cedula']
        edad = request.form['edad']
        genero = request.form['genero']
        email = 'jorge.medina@claro.com.co'
        gerencia = request.form['gerencia']
        direccion = request.form['direccion']
        nombre_gerente = request.form['nombre_gerente']
        celular_gerente = request.form['celular_gerente']
        universidad = request.form['universidad']
        carrera = request.form['carrera']
        tutor = request.form['tutor']
        correo_tutor = request.form['correo_tutor']
        celular_tutor = request.form['celular_tutor']
        eps = request.form['eps']
        contacto_emergencia = request.form['contacto_emergencia']
        numero_emergencia = request.form['numero_emergencia']

        data = {"Nombres": nombre,
            "Apellidos": apellidos,
            "Cedula": cedula,
            "Edad": edad,
            "Sexo": genero,
            "Correo corporativo": email,
            "Gerencia": gerencia,
            "Area de gerencia": direccion,
            "Nombre gerente": nombre_gerente,
            "Celular corporativo": celular_gerente,
            "Universidad": universidad,
            "Carrera": carrera,
            "Nombre tutor": tutor,
            "Correo tutor": correo_tutor,
            "Celular tutor": celular_tutor,
            "EPS": eps,
            "Nombre emergencia": contacto_emergencia,
            "Numero emergencia": numero_emergencia
        }
        crud.updateStudentData(email, data)
        render_template('view_personal_data.html', usuario = crud.getStudentInfo(email))

    return render_template('formulario.html')