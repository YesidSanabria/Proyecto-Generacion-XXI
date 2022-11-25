#######################################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
from flask import render_template, send_file
import pyrebase
import os
from collections import Counter
##########################################
cred = credentials.Certificate("app/config/generacion-xxi-firebase-adminsdk-iwq0c-bc2e550415.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://generacion-xxi-default-rtdb.firebaseio.com/'})
##########################################

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
storage = firebase.storage()

# VARIABLES

options = {
    'sexo': ['Hombre', 'Mujer', 'Otros'], 
    'regional': ['Bogotá', 'Bucaramanga', 'Medellín', 'Barranquilla', 'Cali', 'Manizales']    
    }

# FUNCIONES

def amountCards():
    for n in range(0,2):
        if n ==0:
            for i in range(0,2):
                for j in range(0,4):
                    cuenta=j+(4*i)
                    if j == 7:
                        pasar = j                     
        elif n ==1:
            for i in range(0,2):
                for pasar in range(0,4):
                    cuenta=pasar+(4*i)                   
    return cuenta

# DATOS DE LOS ESTUDIANTES

def getStudentInfo(email):
    ref = db.reference('Estudiantes')
    user = ref.child(email.replace('.', '')).get()
    return user

def getAllStudents():
    ref = db.reference('Estudiantes')
    all = ref.get()
    return all

def getSomeStudents(students):
    lista = []
    for student in students:
        lista.append(getStudentInfo(student))
    someStudents = {}
    for i in range(len(lista)):
        someStudents[students[i]] = lista[i]
    return someStudents

def updateStudentData(email, data):
    ref = db.reference('Estudiantes')
    ref.child(email.replace('.', '')).update(data)
    # Sintaxis:
    # updateStudentData('julian.cely@claro.com.co', {'Celular personal': '3214157461'})

def deleteStudent(email):
    ref = db.reference('Estudiantes')
    ref.child(email.replace('.', '')).delete()   

def createNewStudent(email):
    ref = db.reference('Estudiantes')
    initData = {
            'Correo corporativo': email,
            'Nombres': ''
        }
    ref.child(email.replace('.','')).set(initData)
    
def getStudentsData(students):
    if len(students) >= 1:
        data = getSomeStudents(students)
    else:
        data = getAllStudents()
    keys = list(data.keys())
    email = [data[i]['Correo corporativo'] for i in keys]
    cantidad = len(keys)    
    return keys, email, cantidad

# SOLICITUDES DE PRACTICANTES

def addRequest(req):
    ref = db.reference('Solicitudes')
    ref.push(req)

def getRequests():
    ref = db.reference('Solicitudes')
    return ref.get()

# FOTOS DE PERFIL

def getImagesURL(emails):
    foto=[]
    for i in range(len(emails)):
        foto.append(storage.child("profile_pictures/"+str(emails[i])).get_url(None))
    if len(foto) == 1:
        return foto[0]
    else:
        return foto

def uploadProfileImage(path, image):
    storage.child("profile_pictures/" + path).put(image)

def deleteProfileImage(path):
    storage.child("profile_pictures/" + path, None)

# EVALUACIONES

def saveNewEvaluation(email, role, data):
    table = db.reference('Evaluaciones')
    id = table.child(email.replace('.', ''))
    role = id.child(role)
    role.push(data)

def getEvaluationResults(email, role):
    table = db.reference('Evaluaciones')
    id = table.child(email.replace('.', ''))
    role = id.child(role)
    return role.get()

#PDF plan de desarrollo
def uploadDevelopmentPlan(path, pdf):
    storage.child("development_plan/" + "plan_desarrollo_" + path + ".pdf").put(pdf)
    
#eliminar archivos pland de desarrollo
def deleteDevelopmentPlan(path):
    storage.delete("development_plan/" + "plan_desarrollo_" + path + ".pdf", None)

#descargar archivos del storage plan de desarrollo
def downloadDevelopmentPlan(cedula):
    storage.child("development_plan/" + "plan_desarrollo_" + cedula + ".pdf").download("/","app/pdfs/plan_desarrollo_" + cedula + ".pdf")
    return send_file("pdfs/plan_desarrollo_" + cedula + ".pdf",as_attachment=True)

def urlDevelopmentPlan(cedula):
    archivo = storage.child("development_plan/" + "plan_desarrollo_" + cedula + ".pdf").get_url(None)
    return archivo

#importar datos de graficas (edad)
def getInfoGraphs(students):
    if len(students) >= 1:
        data = getSomeStudents(students)
    else:
        data = getAllStudents()
    keys = list(data.keys())
    email = [data[i]['Correo corporativo'] for i in keys]
    edad = [data[i]['Edad'] for i in keys]
    genero = [data[i]['Sexo'] for i in keys]
    canEdad = dict(Counter(edad))
    canGenero = dict(Counter(genero))
    canPrac = len(keys)
    return keys, email, canEdad, canGenero, canPrac
