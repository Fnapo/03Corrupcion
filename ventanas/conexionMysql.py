# inicio conexionMysql

from ventanas.clases.conectarMysql import ConectarMysql
from mysql.connector import errorcode, MySQLConnection


class ConexionMysql:
    '''
    Clase static con una conexion Mysql
    '''
    
    # atributos static
    _conexion: MySQLConnection = None

    def __init__(self):
        try:
            if ConexionMysql._conexion is None:
                # con ConexionMysql._conexion queda claro que es el atributo static
                ConexionMysql._conexion = ConectarMysql.conectar()
                # con 'self._conexion =' crea el atributo de la instancia
        except:
            raise ConnectionError
        else:
            if ConexionMysql._conexion.is_connected():
                ConexionMysql._conexion.close()
    # fin __init__
# fin ConexionMysql

# fin conexionMysql
