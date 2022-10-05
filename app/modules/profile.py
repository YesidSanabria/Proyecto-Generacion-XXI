from flask import render_template, request
import modules.crud as crud

def view_personal_data():
    if (request.method == 'POST'):
        email = request.form['email']
        print(email)
        return render_template('formulario.html', usuario=crud.getStudentInfo(email))
    return render_template('view_personal_data.html')