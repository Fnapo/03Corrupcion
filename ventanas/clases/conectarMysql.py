# inicio conMysql.py

import mysql.connector as conMysql
from mysql.connector import errorcode
from ventanas.errorCampoModal import ErrorCampoModal
from PyQt5 import QtWidgets


class ConectarMysql:
    '''
    Clase estática para crear una conexión, propia o global, con una BBDD tipo Mysql o para ejecutar una consulta con dicha BBDD.
    '''

    # atributos static
    _configuracion = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'politica'
    }
    _conexion: conMysql.MySQLConnection = None

    def __init__(self):
        try:
            if self._conexion is None:
                self._conexion = self.conectar()
        except:
            raise ConnectionError
        else:
            if self._conexion.is_connected():
                self._conexion.close()
    # fin __init__

    @staticmethod
    def conectar():
        '''
        Crea y retorna una conexión a una BBDD tipo MySQL
        '''
        try:
            conexion = conMysql.connect(**ConectarMysql._configuracion)
        except:
            raise ConnectionError
        else:
            return conexion
    # fin _conectar

    @staticmethod
    def ejecutar(conexion: conMysql.MySQLConnection, consulta: str):
        '''
        Dada una conexion Mysql activa, ejecuta una consulta tipo CRUD (SIUD) sin retornar nada
        '''
        cursor = conexion.cursor()
        cursor.execute(consulta)
        conexion.commit()
        cursor.close()
    # fin ejecutar
# fin class ConectarMysql


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication([])
        conexion = ConectarMysql.conectar()
    except ConnectionError:
        ErrorCampoModal.errorConexion()
    else:
        print("Salida exitosa...")
        conexion.close()
        sys.exit()
# fin if test

# fin conMysql.py
