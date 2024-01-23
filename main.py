# from common import *
# from src.auth import login, logout
# from src.ciudades import Ciudad

# app = Flask(__name__)
# app.secret_key = 'holaholahola'  # Clave secreta para la sesión


# @app.route('/')
# @app.route('/login', methods=['GET', 'POST'])
# def login_route():
#    return login()

# @app.route('/logout')
# def logout_route():
#     return logout()

# @app.route('/ciudades')
# def ciudades_route():
#    ci = Ciudad()

#    return render_template('html/ciudades.html', ciudades=ci.ciudades())
from app import app


if __name__ == '__main__':
  app.run(debug=True)
