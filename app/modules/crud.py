#######################################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
from flask import render_template
import pyrebase
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
    'sexo': ['Hombre', 'Mujer'], 
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

def getStudentInfo(email):
    ref = db.reference('Estudiantes')
    user = ref.child(email.replace('.', '')).get()
    return user

def getAllStudents():
    ref = db.reference('Estudiantes')
    all = ref.get()
    return all

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
    
def getStudentsData():
    data = getAllStudents()
    keys = list(data.keys())
    email = [data[i]['Correo corporativo'] for i in keys]
    cantidad = len(keys)    
    return keys, email, cantidad

def addRequest(req):
    ref = db.reference('Solicitudes')
    ref.push(req)

def getRequests():
    ref = db.reference('Solicitudes')
    return ref.get()

def getStudenKeys():
    ref = db.reference('Estudiantes')
    data = ref.get()
    list = []
    for key in data.keys():
        list.append(key)
    return list

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