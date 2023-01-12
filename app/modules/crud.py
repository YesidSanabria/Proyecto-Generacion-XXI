#######################################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import send_file
import pyrebase
from firebase_admin import auth
import pandas as pd
##########################################
# Excepción para ejecutar el proyecto desde cmd
try:
    cred = credentials.Certificate("app/config/generacion-xxi-firebase-adminsdk-iwq0c-bc2e550415.json")
except:
    cred = credentials.Certificate("config/generacion-xxi-firebase-adminsdk-iwq0c-bc2e550415.json")
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
    'regional': ['Bogotá', 'Bucaramanga', 'Medellín', 'Barranquilla', 'Cali', 'Manizales'],
    'direccion': ['Corporativo financiero',
                  'Corporativo gestión humana',
                  'Corporativo jurídico y asuntos corporativos',
                  'Corporativo marketing y medios de comunicación',
                  'Ejecutivo unidad mercado corporativo',
                  'Auditoría',
                  'Corporativo tecnología',
                  'Ejecutivo unidad mercado masivo',
                  'Corporativo asuntos regulatorios y relaciones institucionales',
                  'Corporativo planeación estratégica e innovación']
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
    student = getStudentInfo(email)
    deleteDevelopmentPlan(student['Cedula'])
    deleteProfileImage(email)
    ref = db.reference('Estudiantes')
    ref.child(email.replace('.', '')).delete()
    user = auth.get_user_by_email(email)
    auth.delete_user(user.uid)

def createNewStudent(email):
    ref = db.reference('Estudiantes')
    initData = {
            'Correo corporativo': email,
            'Nombres': '',
            'Apellidos': '',
            'Area de gerencia': '',
            'Carrera': '',
            'Cedula': '',
            'Celular corporativo': '',
            'Celular gerente': '',
            'Celular personal': '',
            'Celular tutor': '',
            'Correo gerente': '',
            'Correo personal': '',
            'Correo tutor': '',
            'EPS': '',
            'Edad': '',
            'Gerencia': '',
            'Nombre emergencia': '',
            'Nombre gerente': '',
            'Nombre tutor': '',
            'Numero emergencia': '',
            'Regional': '',
            'Sexo': '',
            'Universidad': ''
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
    storage.delete("profile_pictures/" + path, None)

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

def getSingleEvaluation(email, number):
    results = getEvaluationResults(email, 'lider')
    keys = list(results.keys())
    try:
        return results[keys[number - 1]]
    except:
        return False

def getAllEvaluations(number):
    table = db.reference('Evaluaciones')
    keys = list(table.get().keys())
    evaluations = {}
    for student in keys:
        notas = getSingleEvaluation(student, number)
        if notas:
            grades = {}
            for i in range(5, 11):
                grades[str(i - 4)] = int(notas['Pregunta' + str(i)])
            evaluations[student] = grades
    return evaluations

def getEvaluationsAvg(number):
    evaluations = {}
    for i in range(1, 7):
        evaluations[str(i)] = 0
    data = getAllEvaluations(number)
    for student, grades in data.items():
        for question in grades.keys():
            evaluations[question] += grades[question] / len(data.keys())
    return evaluations

#PDF plan de desarrollo
def uploadDevelopmentPlan(path, pdf):
    storage.child("development_plan/" + "plan_desarrollo_" + path + ".pdf").put(pdf)

# Excel con los datos de los practicantes y evaluaciones.
def uploadStudentsExcel():
    storage.child('datos_practicantes/practicantes.xlsx').put('data\Datos Practicantes.xlsx')
    file = storage.child('datos_practicantes/practicantes.xlsx').get_url(None)
    return file

def uploadEvaluationsExcel():
    storage.child('datos_practicantes/evaluaciones.xlsx').put('data\Datos Evaluación.xlsx')
    file = storage.child('datos_practicantes/evaluaciones.xlsx').get_url(None)
    return file
    
#eliminar archivos plan de desarrollo
def deleteDevelopmentPlan(path):
    storage.delete("development_plan/" + "plan_desarrollo_" + path + ".pdf", None)

#descargar archivos del storage plan de desarrollo
def downloadDevelopmentPlan(cedula):
    storage.child("development_plan/" + "plan_desarrollo_" + cedula + ".pdf").download("/","app/pdfs/plan_desarrollo_" + cedula + ".pdf")
    return send_file("pdfs/plan_desarrollo_" + cedula + ".pdf",as_attachment=True)

def urlDevelopmentPlan(cedula):
    archivo = storage.child("development_plan/" + "plan_desarrollo_" + cedula + ".pdf").get_url(None)
    return archivo

# Data frames de los datos contenidos en la base de datos.

def getEvaluationsDF(number):
    dicc = db.reference('Evaluaciones').get()
    keys = dicc.keys()
    for key in keys:
        notas = getSingleEvaluation(key, number)
        if notas:
            dicc[key] = notas
    cols = [
        'Fecha', 'Pregunta1', 'Pregunta2', 'Pregunta3', 'Pregunta4', 'Pregunta5', 'Pregunta6',
        'Pregunta7', 'Pregunta8', 'Pregunta9', 'Pregunta10', 'Observaciones'
    ]
    df = pd.DataFrame.from_dict(dicc, orient='index', columns=cols)
    col_names = {
        'Pregunta1': 'Gerencia', 
        'Pregunta2': 'Cédula', 
        'Pregunta3': 'Nombre Líder', 
        'Pregunta4': 'Nombre Practicante', 
        'Pregunta5': 'Pregunta 1', 
        'Pregunta6': 'Pregunta 2',
        'Pregunta7': 'Pregunta 3',
        'Pregunta8': 'Pregunta 4', 
        'Pregunta9': 'Pregunta 5', 
        'Pregunta10': 'Pregunta 6'
    }
    df.rename(columns=col_names, inplace=True)
    return df

def getStudentsDF():
    dicc = db.reference('Estudiantes').get()
    cols = [
        'Nombres', 'Apellidos', 'Cedula', 'Edad', 'Sexo', 'Celular personal', 'Correo personal', 'Regional', 
        'Gerencia', 'Area de gerencia', 'Correo corporativo', 'Celular corporativo', 
        'Nombre gerente', 'Correo gerente', 'Celular gerente', 
        'Universidad', 'Carrera', 'Nombre tutor', 'Correo tutor', 'Celular tutor', 
        'EPS', 'Nombre emergencia', 'Numero emergencia'        
    ]
    df = pd.DataFrame.from_dict(dicc, orient='index', columns=cols)
    col_names = {
        'Cedula': 'Cédula',
        'Sexo': 'Género',
        'Area de gerencia': 'Dirección corporativa',
        'Nombre gerente': 'Nombre líder',
        'Correo gerente': 'Correo líder',
        'Celular gerente': 'Celular líder',
        'Nombre emergencia': 'Nombre en caso de emergencia',
        'Numero emergencia': 'Numero en caso de emergencia'
    }
    df.rename(columns=col_names, inplace=True)
    return df
