import pyrebase
from flask import render_template, request
import modules.crud as crud



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
            [keys, emails, cantidad] = crud.getStudentsData()
            cuenta = crud.amountCards()
            emails = [x.lower() for x in emails]
            req = crud.getRequests()
             #arreglo con los campos de imagenes de cada persona
            links = crud.getImagesURL(emails)

            if True:
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
                                      
            file_plan = request.files['file_plan']
            plandesa = request.form['plandesa']         
            
            if (file_plan.filename != ''):
                crud.uploadDevelopmentPlan(plandesa, file_plan)                

            if ev == None:
                ev = {'': ''}
            return render_template(putos, usuario=user, l=foto, ev=ev, y=yave)

        elif ruta == "elim":
            putos = 'homeadmin.html'         
            
            [keys, emails, cantidad] = crud.getStudentsData()
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
    return render_template('admin.html')   

    


def confirm():
    if (request.method == 'POST'):               
        putos = 'admin.html'
        user = crud.getAllStudents()
        [keys, emails, cantidad] = crud.getStudentsData()
        cuenta = crud.amountCards()
        emails = [x.lower() for x in emails]
        req = crud.getRequests()
             #arreglo con los campos de imagenes de cada persona
        links = crud.getImagesURL(emails)

        if True:
            return render_template(putos, usuario=user, l=links, req=req, keys=keys, cantidadDatos=cantidad, cuent=cuenta)
        
    return render_template('homeadmin.html')
