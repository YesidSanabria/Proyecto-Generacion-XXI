#######################################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
########################################

import pandas as pd

##########################################
cred = credentials.Certificate("app/config/generacion-xxi-firebase-adminsdk-iwq0c-bc2e550415.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://generacion-xxi-default-rtdb.firebaseio.com/'})
##########################################

# VARIABLES

options = {
    'sexo': ['Hombre', 'Mujer'], 
    'regional': ['Bogotá', 'Bucaramanga', 'Medellín', 'Barranquilla', 'Cali', 'Manizales']
    }

# FUNCIONES

def getStudentInfo(email):
    ref = db.reference('Estudiantes')
    user = ref.child(email.replace('.', '')).get()
    return user

def getAllStudents():
    ref = db.reference('Estudiantes')
    all = ref.get()
    return all

def getCedulas():
    ref = db.reference('Estudiantes')
    snapshot = ref.order_by_child('Cedula').get()
    for key in snapshot:
        print(key)
    

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
    
def cedulas():
    ref = db.reference('Estudiantes')
    all = ref.get()
    data = {
        "calories": '34',
        "duration": '56'
        }
    
    info = pd.DataFrame(list(all.items()))
    for i in range(len(info)):
        info1 = info[1][i]
        info2 = pd.DataFrame(list(info1.items())).transpose()
        
        if i == 0:
            info3 = info2.drop(0)

        if i>0:
            info3 = info3.append(info2.drop(0))    
        
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    #print(info3)
    
    info = info.drop(columns = 1)
    info3 = info3.reset_index()
    
    info4 = pd.concat([info,info3],axis=1)
    info4 = info4.drop(columns = 'index')
    info5 = info4[3] #este es el campo que se modifica para obtener las colunas de los datos en este caso las cedulas
    
    print(info4)
    
    return info5

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