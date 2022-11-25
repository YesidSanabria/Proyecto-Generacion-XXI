from flask import render_template
import modules.crud as crud

def dashboard():
    return render_template('dashboard.html')
