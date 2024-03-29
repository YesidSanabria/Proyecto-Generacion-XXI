from flask import render_template, request
import modules.crud as crud

def confirm():
    if request.method == 'POST':
        role = request.form['role']
        email = request.form['email']
        code = request.form['code']                                 
        code_input = request.form['code_input']
        try:
            user = request.form['user']
            userI = crud.getStudentInfo(user)
            foto = crud.getImagesURL([userI["Correo corporativo"]])  
        except:
            user = ''           
        if code == code_input:
            if role == 'docente':
                ev = {}
                ev['lider'] = crud.getEvaluationResults(user, 'lider')
                return render_template('teacher_ev.html', email=email, user=user, userI=userI, foto=foto, ev=ev)
            elif role == 'líder':                
                return render_template('boss_ev.html', email=email, user=user)
            else:
                return render_template('create_account.html', email=email)
        else:
            message = 'El código de verificación no corresponde'
            return render_template('confirm.html', umessage=message, code=code, email=email, role=role)
                  
    return render_template('confirm.html')