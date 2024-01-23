from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.dao.referenciales.ciudad.CiudadDao import CiudadDao

ciumod = Blueprint('ciudad', __name__, template_folder='templates')

@ciumod.route('/index-ciudad')
def index_ciudad():
    cdao = CiudadDao()
    lista = cdao.get_ciudades()
    diccionario = []
    if len(lista) > 0:
        for item in lista:
            diccionario.append(
                {
                    'id': item[0],
                    'descripcion': item[1]
                }
            )
    return render_template('index-ciudades.html', ciudades = diccionario)