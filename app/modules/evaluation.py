from flask import render_template, request
import random
import modules.send_email as mail
import modules.crud as crud
from datetime import date

# Funciones

def checkInDataBase(role, email):
    users = crud.getAllStudents()
    if role == 'docente':
        field = 'Correo tutor'
    else:
        field = 'Correo gerente'
    students = []
    for user,data in users.items():
        try:
            if data[field] == email:
                students.append({'user': user, 'name': data['Nombres'] + ' ' + data['Apellidos']})
        except:
            x = 'Aquí no pasa nada :v'
    return students

# Módulos

def evaluation():
    if request.method == 'POST':
        role = request.form['role']
        email = request.form['email']
        students = checkInDataBase(role, email)
        # No existe el correo registrado en la base de datos.
        if len(students) < 1:
            message = 'El correo ingresado no corresponde con el del ' + role + ' registrado por algún practicante'
            return render_template('evaluation.html', umessage=message)
        # El correo registrado se encontró en la base de datos.
        else:
            code = ''
            for d in range(6):
                code += str(random.randint(0,9))
            mail.send_mail(email,code)
            # EL correo está una sol vez en la base de datos.
            if len(students) < 2:
                repetido = False
            # El correo está más de una vez en la base de datos.
            else:
                repetido = True
            print(students)
            return render_template('confirm.html', ev=True, code=code, email=email, role=role, students=students, repetido=repetido)
    return render_template('evaluation.html')

def boss_ev():
    if request.method == 'POST':
        evaluation = {}
        for i in range(1, 11):
            evaluation['Pregunta' + str(i)] = request.form['p' + str(i)]
        evaluation['Observaciones'] = request.form['obs']
        evaluation['Fecha'] = str(date.today())
        email = request.form['user']
        crud.saveNewEvaluation(email, 'lider', evaluation)
        message = 'Estudiante evaluado con éxito'
        return render_template('evaluation.html', smessage=message)
    return render_template('boss_ev.html')

def tutor_ev():
    if request.method == 'POST':
        evaluation = {}
        for i in range(1, 6):
            evaluation['Pregunta' + str(i)] = request.form['p' + str(i)]
        evaluation['Observaciones'] = request.form['obs']
        evaluation['Fecha'] = str(date.today())
        email = request.form['user']
        crud.saveNewEvaluation(email, 'tutor', evaluation)
        message = 'Estudiante evaluado con éxito'
        return render_template('evaluation.html', smessage=message)
    return render_template('boss_ev.html')

def teacher_ev():
    if request.method == 'POST':
        user = request.form['user']
        return render_template('tutor_ev.html', user=user)
    return render_template('teacher_ev.html')