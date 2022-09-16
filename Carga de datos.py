import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd 
import numpy as np

cred = credentials.Certificate("generacion-xxi-firebase-adminsdk-iwq0c-bc2e550415.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://generacion-xxi-default-rtdb.firebaseio.com/'})

# Importar datos de Excel.
baseDatos = pd.read_excel('data\DATOS PRACTICANTES (1) (1).xlsx')
dic = baseDatos.to_dict()
# Convertir los datos a lista de listas.
columns = []
for clave in dic.keys():
    column = []
    for i in dic[clave].keys():
        column.append(dic[clave][i])
    columns.append(column)
data = np.array(columns)
data = data.transpose()
rows = data.tolist()


# ref = db.reference('Estudiantes')
# ref.set({
#     'id1': {
#         # 'nombre' : 'David',
#         'apellido' : 'Cely',
#         # 'telefono' : '3214157461'
#     }
# })