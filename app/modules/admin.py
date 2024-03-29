import pyrebase
from flask import render_template, request
import modules.crud as crud
import modules.search as sr
import modules.reports as rp
from urllib.request import urlopen
import modules.excel_files as exf

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
auth = firebase.auth()

def admin():
    if (request.method == 'POST'):
        ruta = request.form ["ruta"]
        if ruta == "admin":
            putos = 'admin.html'
            user = crud.getAllStudents()
            [keys, emails, cantidad] = crud.getStudentsData([])
            cuenta = crud.amountCards()
            emails = [x.lower() for x in emails]
            # arreglo con los campos de imagenes de cada persona
            links = crud.getImagesURL(emails)
            return render_template(putos, usuario=user, l=links, keys=keys, cantidadDatos=cantidad, cuent=cuenta)

        elif ruta == "infopract":
            putos = 'infopract.html'
            yave = request.form["yave"]
            user = crud.getStudentInfo(yave)            
            foto = crud.getImagesURL([request.form["foto"]])
            ev = {}
            ev['lider'] = crud.getEvaluationResults(request.form['yave'], 'lider')
            ev['tutor'] = crud.getEvaluationResults(request.form['yave'], 'tutor')
            if (ev['lider'] == None) | (ev['tutor'] == None):
                ev['lider'] = {'': ''}
                ev['tutor'] = {'': ''}
            file = crud.urlDevelopmentPlan(user['Cedula'])
            # Verificar si hay un plan de desarrollo.
            try:
                urlopen(file)
            except:
                file = False
            return render_template(putos, usuario=user, l=foto, ev=ev, y=yave, file=file)
        
        elif ruta == "infopract1":
            yave = request.form["yavee"]
            putos = 'infopract.html'
            user = crud.getStudentInfo(yave)
            foto = request.form["foto"]
            ev = {}
            ev['lider'] = crud.getEvaluationResults(request.form['yavee'], 'lider')
            ev['tutor'] = crud.getEvaluationResults(request.form['yavee'], 'tutor')
            message = ''
            file_plan = request.files['file_plan']
            plandesa = request.form['plandesa']
            
            if (file_plan.filename != ''):
                crud.uploadDevelopmentPlan(plandesa, file_plan)
                message = 'Plan de desarrollo subido satisfactoriamente.'

            if (ev['lider'] == None) | (ev['tutor'] == None):
                ev['lider'] = {'': ''}
                ev['tutor'] = {'': ''}
            file = crud.urlDevelopmentPlan(user['Cedula'])
            # Verificar si hay un plan de desarrollo.
            try:
                urlopen(file)
            except:
                file = False
            return render_template(putos, usuario=user, l=foto, ev=ev, y=yave, smessage=message, file=file)

        elif ruta == "elim":
            putos = 'homeadmin.html'         
            
            [keys, emails, cantidad] = crud.getStudentsData([])
            user = crud.deleteStudent(request.form["eliminar"])
            foto = crud.getImagesURL([request.form["eliminar"]])
            emails = [x.lower() for x in emails]
            links = crud.getImagesURL(emails)
                         
            return render_template(putos, usuario=user, l=foto, keys=keys, cantidadDatos=cantidad) 

        elif ruta =="edit":
            putos = 'admformulario.html'
            editt = request.form['editar']
            yave = request.form['yavee']
            # foto = crud.getImagesURL([request.form["foto"]])

            return render_template(putos, usuario=crud.getStudentInfo(editt), y=yave)

        elif ruta == 'search':
            putos = 'admin.html'
            user = crud.getAllStudents()
            buscar = request.form['buscar']
            studentsList = sr.searchStudent(buscar)            
            if buscar == '':
                [keys, emails, cantidad] = crud.getStudentsData([])
            else:
                [keys, emails, cantidad] = crud.getStudentsData(studentsList)
            emails = [x.lower() for x in emails]
             #arreglo con los campos de imagenes de cada persona
            links = crud.getImagesURL(emails)
            if len(links[0]) == 1:
                links = [links]
            return render_template(putos, usuario=user, l=links, keys=keys, cantidadDatos=cantidad)

        elif ruta == 'searchCareer':
            putos = 'admin.html'
            user = crud.getAllStudents()
            buscar = request.form['buscar']
            studentsList = sr.searchStudent(buscar)            
            if buscar == '':
                [keys, emails, cantidad] = crud.getStudentsData([])
            else:
                [keys, emails, cantidad] = crud.getStudentsData(studentsList)
            emails = [x.lower() for x in emails]
             #arreglo con los campos de imagenes de cada persona
            links = crud.getImagesURL(emails)
            if len(links[0]) == 1:
                links = [links]
            return render_template(putos, usuario=user, l=links, keys=keys, cantidadDatos=cantidad)
        
        elif ruta == 'reportes':
            exf.createStudentsExcel()
            link = crud.uploadStudentsExcel()
            putos = 'dashboard.html'
            [keys, email, canEdad, canGenero, canPrac, canDir] = rp.getInfoGraphs([])
            [carreras, cont_carreras] = rp.getCareerData()
            [uni, cont_uni] = rp.getUniversityData()
            #canGenero['Otros'] = 0
            canEdadK = list(canEdad.keys())
            canEdadV = list(canEdad.values())
            canGeneroK = list(canGenero.keys())
            canGeneroV = list(canGenero.values())
            canDirK = list(canDir.keys())
            canDirV = list(canDir.values())
            return render_template(putos, keys=keys, carreras=carreras,cont_carreras=cont_carreras,uni=uni,cont_uni=cont_uni, email=email, canEdadK=canEdadK, canEdadV=canEdadV, canGeneroK=canGeneroK, canGeneroV=canGeneroV, canDirK=canDirK, canDirV=canDirV , canPrac=canPrac, link=link)

        elif ruta == 'reportes_ev':
            exf.createEvlauationsExcel()
            link = crud.uploadEvaluationsExcel()
            putos = 'dashboard_ev.html'
            try:
                ev = int(request.form['ev'])
            except:
                ev = 1
            [questions, grades] = rp.getQuestionsResults(ev)
            avg = 0
            for grade in grades:
                grade = round(grade, 2)
                avg += grade / len(grades)
            return render_template(putos, questions=questions, grades=grades, avg=round(avg, 2), ev=ev, link=link)

    return render_template('admin.html')   

    


def confirm():
    if (request.method == 'POST'):               
        putos = 'admin.html'
        user = crud.getAllStudents()
        [keys, emails, cantidad] = crud.getStudentsData([])
        cuenta = crud.amountCards()
        emails = [x.lower() for x in emails]
             #arreglo con los campos de imagenes de cada persona
        links = crud.getImagesURL(emails)

        if True:
            return render_template(putos, usuario=user, l=links, keys=keys, cantidadDatos=cantidad, cuent=cuenta)
        
    return render_template('homeadmin.html')
