# inicio conMysql.py

import mysql.connector as conMysql
from ventanas.errorCampoModal import ErrorCampoModal
from PyQt5 import QtWidgets
import os
from dotenv import load_dotenv


class ConectarMysql:
    '''
    Clase estática para crear una conexión con una BBDD tipo Mysql.
    O para ejecutar una consulta a una BBDD.
    '''

    # atributos static
    _configuracion =  {
        'user': '',
        'password': '',
        'host': '',
        'database': ''
    }

    @staticmethod
    def conectar():
        '''
        Crea y retorna una conexión a una BBDD tipo MySQL
        '''
        try:
            if ConectarMysql._configuracion['host'] == '':
                load_dotenv()
                ConectarMysql._configuracion['user'] = os.getenv('user')
                ConectarMysql._configuracion['password'] = os.getenv('password')
                ConectarMysql._configuracion['host'] = os.getenv('host')
                ConectarMysql._configuracion['database'] = os.getenv('database')
            # fin if
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
