from flask import render_template, request
import modules.crud as crud

def orderOptions(email):
    options = crud.options
    data = crud.getStudentInfo(email)
    genre = data['Sexo']
    city = data['Regional']
    out = {
        'sexo': [genre],
        'regional': [city]
    }
    for i in options['sexo']:
        if i != genre:
            out['sexo'].append(i)
    for i in options['regional']:
        if i != city:
            out['regional'].append(i)
    return out

def view_personal_data():
    if (request.method == 'POST'):
        email = request.form['email']
        user = crud.getStudentInfo(email)
        try:
            opciones = orderOptions(email)
        except:
            opciones = crud.options
        return render_template('formulario.html', usuario=user, opcion=opciones)
    return render_template('view_personal_data.html')