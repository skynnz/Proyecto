from flask import Flask, flash, render_template, request, session, url_for, redirect, flash
from werkzeug.security import check_password_hash
import psycopg2


app = Flask(__name__)
app.secret_key = 'holaholahola'  # Clave secreta para la sesión


# Configura la conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    database="proyecto",
    user="sistema",
    password="admin",
    host="localhost",
    port="5432"
)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'usuario' in request.form and 'contra' in request.form:
        usuario = request.form['usuario']
        contra = request.form['contra']
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE usuario = %s AND contra = %s", (usuario, contra))
        users = cur.fetchone()
        if users:
            #session['loggedin'] = True
            session['iduser'] = users[0]
            session['usuario'] = users[0]  # Almacena el ID del usuario en la sesión
            return render_template('auth/index.html')
        else:
            msg = "Credenciales incorrectas. Inténtalo de nuevo."

    return render_template('auth/login.html', msg = msg)  # Debes crear una plantilla HTML para el formulario de inicio de sesión


@app.route('/logout')
def logout():
    session.pop('loggedin', None) 
    session.pop('iduser', None) 
    session.pop('usuario', None)  # Elimina la información de sesión del usuario
    return redirect(url_for('login'))


if __name__ == '__main__':
  app.run(debug=True, port=81)
