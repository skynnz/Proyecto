import psycopg2

# conn = psycopg2.connect(
#     database="proyecto",
#     user="sistema",
#     password="admin",
#     host="localhost",
#     port="5432"
# )

class Conexion:
    
    def __init__(self):
        """Metodo constructor de la conexion
        
        Se retorna una instancia de la base de datos
        """
        self.__con = psycopg2.connect("dbname=proyecto user=sistema host=localhost password=admin port='5432'")
        
    def getConexion(self):
        return self.__con    