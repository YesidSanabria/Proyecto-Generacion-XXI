import routes as rt
from flask_mail import Mail, Message

def send_mail(email,codVer):
    mail = Mail()
    # https://myaccount.google.com/apppasswords
    #configuracion del obejto
    rt.app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    rt.app.config['MAIL_PORT'] = 465
    rt.app.config['MAIL_USERNAME'] = 'ingsebastianherrerau@gmail.com'
    rt.app.config['MAIL_PASSWORD'] = 'xhpqhmkyinxwdtqv'
    rt.app.config['MAIL_USE_TLS'] = False
    rt.app.config['MAIL_USE_SSL'] = True
                    
    #crea el objeto mail
    mail=Mail(rt.app)
                    
    msg = Message(codVer,sender='ingsebastianherrerau@gmail.com',recipients=[email])
    mail.send(msg)