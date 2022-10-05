from flask import render_template, request
import modules.crud as crud

def profile():
    if (request.method == 'POST'):
        a = 0 # Esta tochada se cambia