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
storage = firebase.storage() #linea del storage
auth = firebase.auth()

def view_personal_data():
    if (request.method == 'POST'):

        upload = request.files['upload']
        userr= request.form['userr']
        storage.child("profile_pictures/" + userr).put(upload)
        
        # return render_template('formulario.html', usuario=crud.getStudentInfo(email))
        
        #if True:
        links = storage.child("profile_pictures/"+userr).get_url(None)
        print(links)
        email = request.form['email']
        return render_template('view_personal_data.html',l=links,usuario=crud.getStudentInfo(email))
                                      
    return render_template('view_personal_data.html')