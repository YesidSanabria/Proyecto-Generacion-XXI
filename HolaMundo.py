import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("generacion-xxi-firebase-adminsdk-iwq0c-bc2e550415.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://generacion-xxi-default-rtdb.firebaseio.com/'})

ref = db.reference('\Estudiantes')
ref.set({
    'id1': {
        'nombre' : 'David',
        'apellido' : 'Cely',
        'telefono' : '3214157461'
    }
})