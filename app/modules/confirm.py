from flask import render_template, request

def confirm():
    if request.method == 'POST':
        role = request.form['role']
        email = request.form['email']
        code = request.form['code']
        code_input = request.form['code_input']
        if code == code_input:
            if role == 'docente':
                return render_template('teacher_ev.html', email=email)
            else:
                return render_template('boss_ev.html', email=email)
        else:
            message = 'El código de verificación no corresponde'
            return render_template('confirm.html', umessage=message, code=code, email=email, role=role)
    return render_template('confirm.html')