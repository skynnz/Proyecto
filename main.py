from common import *
from src.auth import login, logout

app = Flask(__name__)
app.secret_key = 'holaholahola'  # Clave secreta para la sesión


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login_route():
   return login()

@app.route('/logout')
def logout_route():
    return logout()


if __name__ == '__main__':
  app.run(debug=True, port=81)
