import modules.crud as crud
import modules.search as sr
from collections import Counter
from flask import render_template

careers = {
    'SISTEMAS': 'Ingeniería de Sistemas',
    'TRICA': 'Ingeniería Eléctrica',
    'ELECTRON': 'Ingeniería Electrónica',
    'TELECO': 'Ingeniería en Telecomunicaciones',
    'ELECTRO Y TELECO': 'Ingeniería Electrónica y en Telecomunicaciones',
    'MERCADEO': 'Mercadeo',
    'EMPRESA': 'Administración de Empresas',
    'BIOINGENIE': 'Bioingeniería',
    'MECATRO': 'Ingeniería Mecatrónica',
    'MARKET': 'Marketing',
    'MARKET Y INTER': 'Marketing y Negocios Internacionales',
    'OS INTERN': 'Negocios Internacionales',
    'PSI': 'Psicología',
    'PUBLIC': 'Publicidad',
    'PUBLICIDAD INETRN': 'Publicidad Internacional',
    'IA INDUSTRI': 'Ingeniería Industrial',
    'N INDUSTRI': 'Administración Industrial',
    'MATEMAT': 'Matemáticas Aplicadas',
    'COMUNICA': 'Comunicación Social',
    'ARQUI': 'Arquitectura'
}

universities = {
    'PILOTO': 'Universidad Piloto de Colombia',
    'AL DE SAN': 'Universidad Industrial de Santander',
    'DIST': 'Universidad Nacional Abierta y a Distancia',
    'DAD NACION': 'Universidad Nacional de Colombia',
    'EAFIT': 'Universidad EAFIT',
    'MINUTO': 'Corporación Universitaria Minuto de Dios',
    'POLI': 'Politécnico Grancolombiano',
    'BOSQUE': 'Universidad El Bosque',
    'MILITAR': 'Universidad Militar Nueva Granada',
    'MA DE MAN': 'Universidad Autónoma de Manizales',
    'ECCI': 'Universidad ECCI',
    'SERGI': 'Universidad Sergio Arboleda',
    'DISTRI': 'Universidad Distrital',
    'OMA LATI': 'Universidad Autónoma Latinoamericana',
    'DEL NORT': 'Universidad del Norte',
    'OMA DEL CAR': 'Universidad Autónoma del Caribe',
    'CATOLI': 'Universidad Católica de Colombia',
    'ICA Y TEC': 'Universidad Pedagógica y Tecnológica de Colombia',
    'JAVE': 'Pontifica Universidad Javeriana',
    'ROSA': 'Universidad del Rosario',
    'AGUSTIN': 'Universidad Agustiniana',
    'CADA NACIO': 'Corporación Unificada Nacional',
    'SANTO TO': 'Universidad Santo Tomás'
}

def matchCareer(text):
    career = sr.limpiar_acentos(text).upper()
    for key in careers.keys():
        if key in career:
            if (key == 'ELECTRON') & ('TELECO' in career):
                return careers['ELECTRO Y TELECO']
            if (key == 'MARKET') & ('OS INTERN' in career):
                return careers['MARKET Y INTER']
            return careers[key]
    return text

def getCareerData():
    data = crud.getAllStudents()
    careersList = []
    for user in data.keys():
        career = data[user]['Carrera']
        career = matchCareer(career)
        careersList.append(career)
    uniqueCareers = list(set(careersList))
    uniqueCareers.sort()
    count = []
    for item in uniqueCareers:
        count.append(careersList.count(item))
    return uniqueCareers, count

def matchUniversity(text):
    university = sr.limpiar_acentos(text).upper()
    for key in universities.keys():
        if key in university:
            return universities[key]
    return text

def getUniversityData():
    data = crud.getAllStudents()
    universitiesList = []
    for user in data.keys():
        university = data[user]['Universidad']
        university = matchUniversity(university)
        universitiesList.append(university)
    uniqueUniversities = list(set(universitiesList))
    uniqueUniversities.sort()
    count = []
    for item in uniqueUniversities:
        count.append(universitiesList.count(item))
    return uniqueUniversities, count

#importar datos de graficas (edad)
def getInfoGraphs(students):
    if len(students) >= 1:
        data = crud.getSomeStudents(students)
    else:
        data = crud.getAllStudents()
    keys = list(data.keys())
    email = [data[i]['Correo corporativo'] for i in keys]
    edad = [data[i]['Edad'] for i in keys]
    genero = [data[i]['Sexo'] for i in keys]
    dirCorp = [data[i]['Area de gerencia'] for i in keys]
    edad.sort()
    genero.sort()
    dirCorp.sort()
    canEdad = dict(Counter(edad))
    canGenero = dict(Counter(genero))
    canDir = dict(Counter(dirCorp))
    canPrac = len(keys)
    return keys, email, canEdad, canGenero, canPrac, canDir

def dashboard():
    return render_template('dashboard.html')

def dashboard_ev():
    return render_template('dashboard_ev.html')