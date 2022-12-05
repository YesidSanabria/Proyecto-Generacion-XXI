import pyrebase
from flask import render_template, request
import modules.crud as crud
import modules.search as sr
import modules.reports as rp


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
            req = crud.getRequests()
             #arreglo con los campos de imagenes de cada persona
            links = crud.getImagesURL(emails)
            return render_template(putos, usuario=user, l=links, req=req, keys=keys, cantidadDatos=cantidad, cuent=cuenta)

        elif ruta == "infopract":
            putos = 'infopract.html'
            yave = request.form["yave"]
            user = crud.getStudentInfo(yave)            
            foto = crud.getImagesURL([request.form["foto"]])
            ev = crud.getEvaluationResults(request.form['yave'], 'lider')
            if ev == None:
                ev = {'': ''}
            return render_template(putos, usuario=user, l=foto, ev=ev, y=yave)
        
        elif ruta == "infopract1":
            yave = request.form["yavee"]
            putos = 'infopract.html'
            user = crud.getStudentInfo(yave)            
            foto = request.form["foto"]
            ev = crud.getEvaluationResults(yave, 'lider')
            message = ''
            file_plan = request.files['file_plan']
            plandesa = request.form['plandesa']         
            
            if (file_plan.filename != ''):
                crud.uploadDevelopmentPlan(plandesa, file_plan)
                message = 'Plan de desarrollo subido satisfactoriamente.'

            if ev == None:
                ev = {'': ''}
            return render_template(putos, usuario=user, l=foto, ev=ev, y=yave, smessage=message)

        elif ruta == "elim":
            putos = 'homeadmin.html'         
            
            [keys, emails, cantidad] = crud.getStudentsData([])
            user = crud.deleteStudent(request.form["eliminar"])
            foto = crud.getImagesURL([request.form["eliminar"]])
            ev = crud.getEvaluationResults(request.form['eliminar'], 'lider')
            if ev == None:
                ev = {'': ''}         
            emails = [x.lower() for x in emails]
            req = crud.getRequests()
            links = crud.getImagesURL(emails)
                         
            return render_template(putos, usuario=user, l=foto, req=req, keys=keys, cantidadDatos=cantidad, ev=ev) 

        elif ruta =="edit":
            putos = 'admformulario.html'
            editt = request.form['editar']
            yave = request.form['yavee']
            # foto = crud.getImagesURL([request.form["foto"]])

            return render_template(putos, usuario=crud.getStudentInfo(editt),y=yave)

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
            req = crud.getRequests()
             #arreglo con los campos de imagenes de cada persona
            links = crud.getImagesURL(emails)
            if len(links[0]) == 1:
                links = [links]
            return render_template(putos, usuario=user, l=links, req=req, keys=keys, cantidadDatos=cantidad)

        elif ruta == 'searchCareer':
            putos = 'admin.html'
            user = crud.getAllStudents()
            buscar = request.form['buscar']
            studentsList = sr.searchCareer(buscar)            
            if buscar == '':
                [keys, emails, cantidad] = crud.getStudentsData([])
            else:
                [keys, emails, cantidad] = crud.getStudentsData(studentsList)
            emails = [x.lower() for x in emails]
            req = crud.getRequests()
             #arreglo con los campos de imagenes de cada persona
            links = crud.getImagesURL(emails)
            if len(links[0]) == 1:
                links = [links]
            return render_template(putos, usuario=user, l=links, req=req, keys=keys, cantidadDatos=cantidad)
        
        elif ruta == 'reportes':
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
            return render_template(putos, keys=keys, carreras=carreras,cont_carreras=cont_carreras,uni=uni,cont_uni=cont_uni, email=email, canEdadK=canEdadK, canEdadV=canEdadV, canGeneroK=canGeneroK, canGeneroV=canGeneroV, canDirK=canDirK, canDirV=canDirV , canPrac=canPrac)

        elif ruta == 'reportes_ev':
            putos = 'dashboard_ev.html'
            [keys, email, canEdad, canGenero, canPrac] = rp.getInfoGraphs([])
            [carreras, cont_carreras] = rp.getCareerData()
            [uni, cont_uni] = rp.getUniversityData()
            canGenero['Otros'] = 0
            canEdadK = list(canEdad.keys())
            canEdadV = list(canEdad.values())
            canGeneroK = list(canGenero.keys())
            canGeneroV = list(canGenero.values())
            return render_template(putos, keys=keys, carreras=carreras,cont_carreras=cont_carreras,uni=uni,cont_uni=cont_uni, email=email, canEdadK=canEdadK, canEdadV=canEdadV, canGeneroK=canGeneroK, canGeneroV=canGeneroV, canPrac=canPrac)

    return render_template('admin.html')   

    


def confirm():
    if (request.method == 'POST'):               
        putos = 'admin.html'
        user = crud.getAllStudents()
        [keys, emails, cantidad] = crud.getStudentsData([])
        cuenta = crud.amountCards()
        emails = [x.lower() for x in emails]
        req = crud.getRequests()
             #arreglo con los campos de imagenes de cada persona
        links = crud.getImagesURL(emails)

        if True:
            return render_template(putos, usuario=user, l=links, req=req, keys=keys, cantidadDatos=cantidad, cuent=cuenta)
        
    return render_template('homeadmin.html')
