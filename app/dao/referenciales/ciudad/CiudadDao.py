from app.conexion.db import Conexion
class CiudadDao:
    
    def getCiudades(self):
        
        ciudadSQL = """
            SELECT idciudad, nom_city, abr_city
            FROM ciudades
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(ciudadSQL)
            lista_ciudades = cur.fetchall()
            return lista_ciudades
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()
            
    def getCiudadById(self, idciudad):
        
        ciudadSQL = """
            SELECT idciudad, nom_city, abr_city
            FROM ciudades WHERE idciudad = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(ciudadSQL, (idciudad,))
            ciudad = cur.fetchone()
            if ciudad:
                return { 'idciudad': ciudad[0], 'nom_city': ciudad[1], 'abr_city': ciudad[2]}
            return None
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()
            
    def insertCiudad(self, nom_city, abr_city):
        
        insertSQL = """
            INSERT INTO ciudades(nom_city, abr_city) VALUES(%s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(insertSQL, (nom_city, abr_city))
            con.commit()
            return True
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()
        return False
    
    def updateCiudad(self, id, nom_city, abr_city):
        
        updateSQL = """
            UPDATE ciudades SET nom_city = %s and abr_city = %s WHERE idciudad = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(updateSQL, (nom_city, abr_city, id,))
            con.commit()
            return True
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()
        return False
    
    def deleteCiudad(self, idciudad):
        
        deleteSQL = """
            DELETE FROM ciudades WHERE idciudad = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(deleteSQL, (idciudad,))
            con.commit()
            return True
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()
        return False