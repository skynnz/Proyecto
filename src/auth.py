from common import *


def login():
    msg = ''
    if request.method == 'POST' and 'usuario' in request.form and 'contra' in request.form:
        usuario = request.form['usuario']
        contra = request.form['contra']
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        cur.execute("SELECT * FROM usuarios WHERE usu_nick = %s AND usu_clave = %s", (usuario, contra))
        users = cur.fetchone()
        if users:
            session['iduser'] = users[0]
            session['usu_nick'] = users[0]  # Almacena el ID del usuario en la sesión
            session['nombres'] = users[1]
            return render_template('auth/index.html')
        else:
            msg = "Credenciales incorrectas. Inténtalo de nuevo."

    return render_template('auth/login.html', msg = msg)  # Debes crear una plantilla HTML para el formulario de inicio de sesión

def logout():
    session.pop('iduser', None) 
    session.pop('usu_nick', None)  # Elimina la información de sesión del usuario
    return redirect(url_for('login_route'))