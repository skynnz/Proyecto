from flask import Flask

app = Flask(__name__)

# referenciales
from app.rutas.referencial.ciudad.ciudad_ruta import ciumod

modulo0 = '/referencial'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')