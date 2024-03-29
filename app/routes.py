from flask import render_template
from flask import Flask
from flask_mail import Mail

# ------ Importar archivos propios -------
import modules.register as reg
import modules.login as lg
import modules.passw as pw
import modules.admin as ad
import modules.form as fm
import modules.profile as pf
import modules.evaluation as ev
import modules.confirm as cf
import modules.notif as nt
import modules.reports as rp
import modules.faq as fq

app = Flask(__name__)
app.secret_key = 'esto-es-una-clave-muy-secreta'
mail = Mail()

# --------------------------------------REGISTRO E INICIO DE SESION-------------------------------------

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/index', methods=['GET', 'POST'])
def index():     
    return lg.index()

# ----------------------REGISTRARSE-----------------------------

@app.route('/register', methods=['GET', 'POST'])
def register():
    return reg.register()

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    return reg.create_account()

# ----------------------REINICIAR CONTRASEÑA----------------------

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    return pw.forgot_password()

# --------------------------------------EVALUACION A PRACTICANTES-------------------------------------

@app.route('/evaluation', methods=['GET', 'POST'])
def evaluation():
    return ev.evaluation()

@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    return cf.confirm()

@app.route('/boss_ev', methods=['GET', 'POST'])
def boss_ev():
    return ev.boss_ev()

@app.route('/teacher_ev', methods=['GET', 'POST'])
def teacher_ev():
    return ev.teacher_ev()

@app.route('/tutor_ev', methods=['GET', 'POST'])
def tutor_ev():
    return ev.tutor_ev()

# --------------------------------------REGISTRO E INICIO DE SESION-------------------------------------

@app.route('/admin_view', methods=['GET', 'POST'])
def admin_view():
    return ad.admin()

@app.route('/homeadmin', methods=['GET', 'POST'])
def hadmin():
    return ad.confirm()

# --------------------------------------FORMULARIO-------------------------------------

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    return fm.form()

# --------------------------------------PERFIL-------------------------------------

@app.route('/view_personal_data', methods=['GET', 'POST'])
def view_personal_data():
    return pf.view_personal_data()

# ---------------------------------Propuesta Notificaciones YS -------------------------------------

@app.route('/notif', methods=['GET', 'POST'])
def notif():
    return nt.notif()

# ---------------------------------FAQ -------------------------------------

@app.route('/faq', methods=['GET', 'POST'])
def faq():
    question= fq.question
    length = len(question)
    return render_template('faq.html', question=question, length=length)

#------------------------- DESCARGAR EL PLAN DE DESARROLLO- -------------------
@app.route('/download', methods=['GET', 'POST'])
def download_file():
    return pf.download_file()

#------------------------ DASHBOARD ------------------------------------------
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return rp.dashboard()

@app.route('/dashboard_ev', methods=['GET', 'POST'])
def dashboard_ev():
    return rp.dashboard_ev()
    
# ---------------------------------PROGRAMAR ARRIBA DEL IF DE ABAJO----------------------------------
# if __name__ == '__main__':
#     mail.init_app(app)
#     app.run(debug=True)

if __name__ == '__main__':
    server_name = app.config['SERVER_NAME']
    if server_name and ':' in server_name:
        host, port = server_name.split(":")
        port = int(port)
    else:
        port = 80
        host = "localhost"
    mail.init_app(app)
    app.run(host=host, port=port, debug=True)