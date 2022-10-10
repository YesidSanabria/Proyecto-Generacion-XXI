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

app = Flask(__name__)

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

# ---------------------------------PROGRAMAR ARRIBA DEL IF DE ABAJO----------------------------------
if __name__ == '__main__':
    app.run(debug=True)

# ---------------------------------Propuesta ADMIN JM -------------------------------------


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')
