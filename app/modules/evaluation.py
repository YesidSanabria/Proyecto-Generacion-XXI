from flask import render_template, request
import random
import modules.send_email as mail
import modules.crud as crud

# Funciones

def check_in_database(role,email):
    users = crud.getAllStudents()
    if role == 'docente':
        field = 'Correo tutor'
    else:
        field = 'Correo gerente'
    for user,data in users.items():
        try:
            if data[field] == email:
                return user, data['Nombres'] + ' ' + data['Apellidos']
        except:
            x = 'Aquí no pasa nada :v'
    return False, False

# Módulos

def evaluation():
    if request.method == 'POST':
        role = request.form['role']
        email = request.form['email']
        [user, name] = check_in_database(role,email)
        if name:
            code = ''
            for d in range(6):
                code += str(random.randint(0,9))
            mail.send_mail(email,code)
            return render_template('confirm.html', code=code, email=email, role=role, name=name, user=user)
        else:
            message = 'El correo ingresado no corresponde con el del '+ role + ' registrado por el practicante'
            return render_template('evaluation.html', umessage=message)
    return render_template('evaluation.html')