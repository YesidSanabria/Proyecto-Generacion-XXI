import pyrebase
from flask import render_template, request
import modules.crud as crud
import modules.evaluation as ev

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
        celular_personal = request.form['celular_personal']
        correo_corporativo = request.form['correo_corporativo']
        celular_corporativo = request.form['celular_corporativo']
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
        correo_personal = request.form['correo_personal']
        registro = request.form['registro']

        data = {"Nombres": nombre,
            "Apellidos": apellidos,
            "Cedula": cedula,
            "Edad": edad,
            "Sexo": genero,
            "Correo corporativo": correo_corporativo,
            "Gerencia": gerencia,
            "Area de gerencia": direccion,
            "Nombre gerente": nombre_gerente,
            "Celular personal" : celular_personal,
            "Celular gerente": celular_gerente,
            "Celular corporativo": celular_corporativo,
            "Universidad": universidad,
            "Carrera": carrera,
            "Nombre tutor": tutor,
            "Correo tutor": correo_tutor,
            "Celular tutor": celular_tutor,
            "EPS": eps,
            "Nombre emergencia": contacto_emergencia,
            "Numero emergencia": numero_emergencia,
            "Correo gerente": correo_gerente,
            "Regional": regional,
            "Correo personal": correo_personal
        }
        crud.updateStudentData(correo_corporativo, data)
        mensaje = 'Los datos han sido guardados satisfactoriamente.'
        links = crud.getImagesURL([correo_corporativo])
        userr= request.form['userr']
        try:
            upload = request.files['upload']
            if (upload.filename != ''):
                crud.uploadProfileImage(userr, upload)
                links = crud.getImagesURL([userr])
                #print("1")
        except:
            upload = 3
        
        #print(upload.filename)
        

            
        if (registro == 'estudiante'):
            return render_template('view_personal_data.html', nav_activo=1, usuario=crud.getStudentInfo(correo_corporativo), smessage=mensaje,l=links)
        else:
            user = crud.getStudentInfo(request.form["userr"])
            links = crud.getImagesURL([correo_corporativo])
            ev = {}
            ev['lider'] = crud.getEvaluationResults(correo_corporativo, 'lider')
            ev['tutor'] = crud.getEvaluationResults(correo_corporativo, 'tutor')
            if ev == None:
                ev['lider'] = {'': ''}
                ev['tutor'] = {'': ''}
            return render_template('infopract.html', usuario=user, l=links, ev=ev)
    return render_template('formulario.html')