import routes as rt
from flask import render_template
from flask_mail import Mail, Message

def send_mail(email,codVer):
    # mail = Mail().
    # https://myaccount.google.com/apppasswords
    #configuracion del obejto
    rt.app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    rt.app.config['MAIL_PORT'] = 465
    rt.app.config['MAIL_USERNAME'] = 'sspg.xxi@gmail.com'
    rt.app.config['MAIL_PASSWORD'] = 'kerjzfaqfgxbobyn'
    rt.app.config['MAIL_USE_TLS'] = False
    rt.app.config['MAIL_USE_SSL'] = True
                    
    #crea el objeto mail
    mail=Mail(rt.app)
                    
    msg = Message("Codigo de verificación de usuario",sender='sspg.xxi@gmail.com',recipients=[email])
    msg.body = 'Su codigo de verificación es: ' + codVer + "\n\n" + "Mensaje enviado de manera automática, no responder"
    mail.send(msg)

def send_custom_email(email,link,correo):
    # mail = Mail()
    # https://myaccount.google.com/apppasswords
    #configuracion del obejto
    rt.app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    rt.app.config['MAIL_PORT'] = 465
    rt.app.config['MAIL_USERNAME'] = 'sspg.xxi@gmail.com'
    rt.app.config['MAIL_PASSWORD'] = 'kerjzfaqfgxbobyn'
    rt.app.config['MAIL_USE_TLS'] = False
    rt.app.config['MAIL_USE_SSL'] = True
                    
    #crea el objeto mail
    mail=Mail(rt.app)

    
    # msg = Message("Restablecer contraseña",sender='sspg.xxi@gmail.com',recipients=[email])
    # #msg.body = 'Link de restablecimiento de contraseña: ' +  "\n\n"  + "Mensaje enviado de manera automática, no responder" 
    # msg.html = render_template('correoFP.html', link=link,mail=correo)
    # mail.send(msg)
    
    msg1 = Message("Restablecer contraseña",sender='sspg.xxi@gmail.com',recipients=[correo])
    #msg1.body = 'Link de restablecimiento de contraseña: ' + "\n\n"  + "Mensaje enviado de manera automática, no responder" 
    msg1.html = render_template('correoFP.html', link=link,mail=correo)
    mail.send(msg1)