from app.conexion.db import Conexion

class CiudadDao:
    
    def get_ciudades(self):
        ciudadessql = """ select idciudad, nom_city, abr_city from ciudades """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(ciudadessql)
            listar_ciudades = cur.fetchall()
            return listar_ciudades
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")


        finally:
            cur.close()
            con.close()


    def ciudades(self):
        lista = self.get_ciudades()
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
        return diccionario