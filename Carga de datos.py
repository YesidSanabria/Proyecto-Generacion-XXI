from email.mime import base
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd 
import numpy as np
import os

cred = credentials.Certificate("app/config/generacion-xxi-firebase-adminsdk-iwq0c-bc2e550415.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://generacion-xxi-default-rtdb.firebaseio.com/'})

# Importar datos de Excel.
file = os.listdir('data')[0]
# Definir todos los campos numéricos como campos de texto.
col_types = {
    'Numero emergencia':str, 
    'Cedula':str, 
    'Celular corporativo':str, 
    'Celular personal':str,
    'Celular tutor':str,
    'Celular gerente':str,
    'Edad':str
    }
baseDatos = pd.read_excel(f'data\{file}',dtype=col_types)
dic = baseDatos.to_dict()
# Convertir los datos a lista de listas.
columns = []
keys = list(dic.keys())
for clave in keys:
    column = []
    for i in dic[clave].keys():
        column.append(dic[clave][i])
    columns.append(column)
data = np.array(columns)
data = data.transpose()
rows = data.tolist()

# Hasta este punto todos los registros están en una lista individual.

# Convertir cada registro en el formato JSON para subir  Firebase.
students = {}
for register in rows:
    field = {}
    ci = register[9].replace('.', '')    # Correo institucional como PK.
    for i in range(len(register)):
        field[keys[i]] = str(register[i])
    if ci != 'nan': # Exclusión de gente sin correo institucional.
        students[ci] = field
ref = db.reference('Estudiantes')
ref.set(students)
