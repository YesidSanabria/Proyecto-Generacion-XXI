from flask import render_template, request
import modules.crud as crud

def form ():
    if (request.method == 'POST'):
        
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        # cedula = request.form['cedula']
        edad = request.form['edad']
        genero = request.form['genero']
        email = 'jorge.medina@claro.com.co'
        gerencia = request.form['gerencia']
        direccion = request.form['direccion']
        nombre_gerente = request.form['nombre_gerente']
        celular_gerente = request.form['celular_gerente']
        universidad = request.form['universidad']
        carrera = request.form['carrera']
        tutor = request.form['nombre_tutor']
        correo_tutor = request.form['correo_tutor']
        # celular_tutor = request.form['celular_tutor']
        eps = request.form['eps']
        contacto_emergencia = request.form['nombre_emergencia']
        numero_emergencia = request.form['numero_emergencia']
        correo_gerente = request.form['correo_gerente']

        data = {"Nombres": nombre,
            "Apellidos": apellidos,
            # "Cedula": cedula,
            "Edad": edad,
            "Sexo": genero,
            "Correo corporativo": email,
            "Gerencia": gerencia,
            "Area de gerencia": direccion,
            "Nombre gerente": nombre_gerente,
            "Celular corporativo": celular_gerente,
            "Universidad": universidad,
            "Carrera": carrera,
            "Nombre tutor": tutor,
            "Correo tutor": correo_tutor,
            # "Celular tutor": celular_tutor,
            "EPS": eps,
            "Nombre emergencia": contacto_emergencia,
            "Numero emergencia": numero_emergencia,
            "Correo gerente": correo_gerente
        }
        crud.updateStudentData(email, data)
        return render_template('view_personal_data.html', usuario=crud.getStudentInfo(email))

    return render_template('formulario.html')