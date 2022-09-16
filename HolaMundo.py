import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd 

cred = credentials.Certificate("generacion-xxi-firebase-adminsdk-iwq0c-bc2e550415.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://generacion-xxi-default-rtdb.firebaseio.com/'})

#importar datos 
baseDatos = pd.read_excel('data\DATOS PRACTICANTES (1) (1).xlsx')
print(baseDatos)

"""
ref = db.reference('Estudiantes')
ref.set({
    'id1': {
        'nombre' : 'David',
        'apellido' : 'Cely',
        'telefono' : '3214157461'
    }
})
"""