from email import message
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
    nombre = request.form['nombre']
    cedula = request.form['cedula']
    edad = request.form['edad']
    genero = request.form['genero']
    email = 'jorge.medina@claro.com'
    gerencia = request.form['gerencia']
    direccion = request.form['direccion']
    nombre_gerente = request.form['nombre_gerente']
    celular_corporativo = request.form['celular_corporativo']
    correo_corporativo = request.form['correo_corporativo']
    universidad = request.form['universidad']
    carrera = request.form['carrera']
    tutor = request.form['tutor']
    correo_tutor = request.form['correo_tutor']
    celular_tutor = request.form['celular_tutor']
    eps = request.form['eps']
    contacto_emergencia = request.form['contacto_emergencia']
    numero_emergencia = request.form['numero_emergencia']

    data = {"Nombres": nombre
    }

    try:
        crud.updateStudentData(email, data)
        message = 'Usuario guardado satisfactoriamente'
    except:
        message = 'Error en el registro del usuario'

    return jsonify({"message": message})