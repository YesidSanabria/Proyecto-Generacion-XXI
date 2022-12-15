from flask import render_template, request, session
import modules.crud as crud
import modules.faq as fq
from urllib.request import urlopen

def orderOptions(email):
    options = crud.options
    data = crud.getStudentInfo(email)
    genre = data['Sexo']
    city = data['Regional']
    dirCorp = data['Area de gerencia']
    out = {
        'sexo': [genre],
        'regional': [city],
        'direccion': [dirCorp]
    }
    for i in options['sexo']:
        if i != genre:
            out['sexo'].append(i)
    for i in options['regional']:
        if i != city:
            out['regional'].append(i)
    for i in options['direccion']:
        if i != dirCorp:
            out['direccion'].append(i)
    return out

def view_personal_data():
    if (request.method == 'POST'):
        ruta = request.form ["ruta"]
        if ruta == "pract":
            user = crud.getStudentInfo(request.form["email"])
            links = crud.getImagesURL([request.form["email"]])
            file = crud.urlDevelopmentPlan(user['Cedula'])
            # Verificar si hay un plan de desarrollo
            try:
                urlopen(file)
            except:
                file = False
            try:
                if request.form['email'] in session["username"]:
                    return render_template('view_personal_data.html', nav_activo=1, usuario=user, l=links, file=file)
                else: 
                    return render_template('index.html')
            except:
                return render_template('index.html')
        elif ruta == "actu":
            putos = 'formulario.html'
            user = crud.getStudentInfo(request.form['actuali'])
            links = crud.getImagesURL([request.form["actuali"]])
            # print(request.form['actuali'])
            # print(session["username"])
            try:
                opciones = orderOptions(user['Correo corporativo'])
            except:
                opciones = crud.options  
            try:                      
                if request.form['actuali'] in session["username"]:
                    return render_template(putos, nav_activo=2, usuario= user, opcion=opciones, l=links)
                else:
                    return render_template('index.html')
            except:
                return render_template('index.html')
        elif ruta == "faq":
             user = crud.getStudentInfo(request.form['faq2'])
             links = crud.getImagesURL([request.form["faq2"]])
             question= fq.question
             length = len(question)
             return render_template('faq.html', nav_active=3, usuario=user, question=question, length=length)


    return render_template('view_personal_data.html')

def download_file():
    if (request.method == 'POST'):
        cedula = request.form ["cedula"]
        return crud.downloadDevelopmentPlan(cedula)
    