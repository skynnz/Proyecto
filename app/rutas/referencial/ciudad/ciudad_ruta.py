from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.dao.referenciales.ciudad.CiudadDao import CiudadDao

ciumod = Blueprint('ciudad', __name__, template_folder='templates')

@ciumod.route('/index-ciudad')
def index_ciudad():
    cdao = CiudadDao()
    lista = cdao.getCiudades()
    diccionario = []
    if len(lista) > 0:
        for item in lista:
            diccionario.append(
                {
                    'idciudad': item[0],
                    'nom_city': item[1],
                    'abr_city': item[2]
                }
            )
    return render_template('index-ciudades.html', ciudades=diccionario)

@ciumod.route('/agregar-ciudad')
def agregar_ciudad():
    return render_template('vistas_ciudades/agregar-ciudad.html')

@ciumod.route('/save-ciudad', methods=['POST'])
def save_ciudad():
    cdao = CiudadDao()
    txtciudad = request.form['txtciudad']
    isSaved = False
    if txtciudad != None and len(txtciudad.strip()) > 0:
        isSaved = cdao.insertCiudad(txtciudad.strip().upper())
    if isSaved:
        return redirect(url_for('index_ciudad'))
    else:
        return redirect(url_for('agregar_ciudad'))

@ciumod.route('/editar-ciudad/<id>')
def editar_ciudad(id):
    cdao = CiudadDao()
    ciudadFound = cdao.getCiudadById(id)
    if ciudadFound:
        return render_template('vistas_ciudades/editar-ciudad.html', ciudad=ciudadFound)
    return redirect(url_for('index_ciudad'))

@ciumod.route('/update-ciudad', methods=['POST'])
def update_ciudad():
    cdao = CiudadDao()
    idtxtciudad = request.form['idtxtciudad']
    txtciudad = request.form['txtciudad']
    isUpdated = False
    if idtxtciudad == None or len(idtxtciudad.strip()) == 0:
        return redirect(url_for('index_ciudad'))
    
    if txtciudad != None and len(txtciudad.strip()) > 0:
        isUpdated = cdao.updateCiudad(idtxtciudad.strip(), txtciudad.strip().upper())
    if isUpdated:
        return redirect(url_for('index_ciudad'))
    else:
        return redirect(url_for('editar_ciudad', id=idtxtciudad))

@ciumod.route('/delete-ciudad/<id>')
def delete_ciudad(id):
    cdao = CiudadDao()
    cdao.deleteCiudad(id)
    return redirect(url_for('ciudad.index_ciudad'))

# REST
@ciumod.route('/get-ciudad')
def getCiudad():
    cdao = CiudadDao()
    lista = cdao.getCiudades()
    diccionario = []
    if len(lista) > 0:
        for item in lista:
            diccionario.append(
                {
                    'id': item[0],
                    'descripcion': item[1]
                }
            )
        return jsonify(diccionario)
    else:
        return 'no hay ciudades'
