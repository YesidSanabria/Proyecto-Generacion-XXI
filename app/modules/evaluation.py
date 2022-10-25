from flask import render_template, request
import random
import modules.send_email as mail

def evaluation():
    if request.method == 'POST':
        role = request.form['role']
        email = request.form['email']
        code = ''
        for d in range(6):
            code += str(random.randint(0,9))
        mail.send_mail(email,code)
        return render_template('confirm.html', code=code, email=email, role=role)
    return render_template('evaluation.html')