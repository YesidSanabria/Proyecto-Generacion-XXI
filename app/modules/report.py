import modules.crud as crud

careers = {
    'SISTEMAS': 'Ingeniería de Sistemas',
    'ELECTRICA': 'Ingeniería Eléctrica',
    'ELECTRONICA': 'Ingeniería Electrónica',
    'TELECO': 'Ingeniería en Telecomunicaciones',
    'ELECTRO Y TELECO': 'Ingeniería Electrónica y en Telecomunicaciones',
    'MERCADEO': 'Mercadeo',
    'EMPRESA': 'Administración de Empresas',
    'BIOINGENIE': 'Bioingeniería',
    'MECATRO': 'Ingeniería Mecatrónica',
    'MARKETING': 'Marketing',
    'MARKET Y INTER': 'Marketing y Negocios Internacionales',
    'INTERNAC': 'Negocios Internacionales',
    'PSI': 'Psicología',
    'PUBLIC': 'Publicidad',
    'PUBLICIDAD INETRN': 'Publicidad Internacional',
    'IA INDUSTRI': 'Ingeniería Industrial',
    'N INDUSTRI': 'Administración Industrial',
    'MATEMAT': 'Matemáticas Aplicadas',
    'COMUNICA': 'Comunicación Social',
    'ARQUI': 'Arquitectura'
}

def getCareerData():
    data = crud.getAllStudents()
