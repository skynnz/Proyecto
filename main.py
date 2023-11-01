from flask import Flask, render_template, request, session, url_for, redirect, flash
from werkzeug.security import check_password_hash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)


app.secret_key = 'your secret key'
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sistema'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'proyecto'
 
mysql = MySQL(app)
 
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'usuario' in request.form and 'contra' in request.form:
        usuario = request.form['usuario']
        contra = request.form['contra']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND pass = % s', (usuario, contra, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('auth/index.html', msg = msg)
        else:
            msg = 'Incorrect usuario / contra !'
    return render_template('auth/login.html', msg = msg)
 
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    flash('Goodbye!')
    return redirect(url_for('login'))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
