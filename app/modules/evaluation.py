from flask import render_template, request
import random

def evaluation():
    if request.method == 'POST':
        role = request.form['role']
        email = request.form['email']
        code = ''
        for d in range(6):
            code += str(random.randint(0,9))
        print(code)
        return render_template('confirm.html', code=code, email=email, role=role)
    return render_template('evaluation.html')