from flask import render_template, request
import modules.crud as crud

def demand():
    if request.method == 'POST':
        solicitud = {}
        solicitud['Direccion'] = request.form['direccion']
        solicitud['Gerencia'] = request.form['gerencia']
        solicitud['Profesion'] = request.form['profesion']
        solicitud['Motivo'] = request.form['motivo']
        solicitud['Nombre'] = request.form['nombre']
        solicitud['Email'] = request.form['email']
        crud.addRequest(solicitud)
        return render_template('index.html')
    return render_template('solicitudes.html')