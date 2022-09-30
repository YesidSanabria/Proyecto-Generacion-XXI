#######################################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
########################################

##########################################
cred = credentials.Certificate("app/config/generacion-xxi-firebase-adminsdk-iwq0c-bc2e550415.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://generacion-xxi-default-rtdb.firebaseio.com/'})
##########################################

def getStudentInfo(email):
    ref = db.reference('Estudiantes')
    user = ref.child(email.replace('.', '')).get()
<<<<<<< HEAD
    return user

def getAllStudents():
    ref = db.reference('Estudiantes')
    all = ref.get()
    print(all)
    return all

def updateStudentData(email, data):
    ref = db.reference('Estudiantes')
    ref.child(email.replace('.', '')).update(data)
    # Sintaxis:
    # updateStudentData('julian.cely@claro.com.co', {'Celular personal': '3214157461'})

def deleteStudent(email):
    ref = db.reference('Estudiantes')
    ref.child(email.replace('.', '')).delete()
=======
    return user
>>>>>>> a85ba8aa3ebac70be4e48acae28a22a611cf878f
