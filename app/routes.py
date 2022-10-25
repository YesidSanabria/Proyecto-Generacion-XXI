# Este se quita cuando se arregle la sección "Pendientes de cambio"
from flask import render_template
####################################################################
from flask import Flask

# ------ Importar archivos propios -------
import modules.register as reg
import modules.login as lg
import modules.passw as pw
import modules.admin as ad
import modules.form as fm
import modules.profile as pf
import modules.demand as dm
import modules.evaluation as ev
import modules.confirm as cf
import modules.notif as nt


from flask_mail import Mail


app = Flask(__name__)
mail = Mail()

# --------------------------------------REGISTRO E INICIO DE SESION-------------------------------------

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():     
    return lg.index()

# ----------------------REGISTRARSE-----------------------------

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    return reg.create_account()

# ----------------------REINICIAR CONTRASEÑA----------------------

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    return pw.forgot_password()

############################ Pendientes de cambio ################################
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

# --------------------------------------EVALUACION A PRACTICANTES-------------------------------------

@app.route('/evaluation', methods=['GET', 'POST'])
def evaluation():
    return ev.evaluation()

@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    return cf.confirm()

@app.route('/boss_ev', methods=['GET', 'POST'])
def boss_ev():
    return render_template('boss_ev.html')

@app.route('/teacher_ev', methods=['GET', 'POST'])
def teacher_ev():
    return render_template('teacher_ev.html')
    
# --------------------------------------SOLICITUD DE PRACTICANTES-------------------------------------

@app.route('/solicitudes', methods=['GET', 'POST'])
def solicitudes():
    return dm.demand()

# --------------------------------------REGISTRO E INICIO DE SESION-------------------------------------

@app.route('/admin_view', methods=['GET', 'POST'])
def admin_view():
    return ad.admin()

# --------------------------------------FORMULARIO-------------------------------------

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    return fm.form()

# --------------------------------------PERFIL-------------------------------------
@app.route('/view_personal_data', methods=['GET', 'POST'])
def view_personal_data():
    return pf.view_personal_data()

# ---------------------------------Propuesta Notificaciones YS -------------------------------------

# @app.route('/notif', methods=['GET', 'POST'])
# def admin_view():
#     return nt.notif()

# ---------------------------------PROGRAMAR ARRIBA DEL IF DE ABAJO----------------------------------
if __name__ == '__main__':
    mail.init_app(app)
    app.run(debug=True)

