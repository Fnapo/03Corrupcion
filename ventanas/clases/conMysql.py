# inicio conMysql.py

import mysql.connector as conMysql
from mysql.connector import Error, errorcode

# inicio class ConectarMysql


class ConectarMysql(object):
    @staticmethod
    def conectar():
        '''
        Crea una conexión a una BBDD de MySQL
        '''
        configuracion = {
            'user': 'root',
            'password': '',
            'host': '127.0.0.1',
            'database': 'politica'
        }
        try:
            conex = conMysql.connect(**configuracion)
        except Error as error:
            print(f"Error en la conexión: {error.errno}")
            return None
        else:
            print(f"Conexión correcta ... {conex}")
            return conex

    # fin conectar()

    @staticmethod
    def insertar(conexion, consulta):
        '''
        Hace una inserción retornando el id del registro insertado
        '''
        cursor = conexion.cursor()
        cursor.execute(consulta)
        conexion.commit()
        salida = cursor.lastrowid
        cursor.close()

        return salida

    # fin insertar

# fin class ConectarMysql


if __name__ == "__main__":
    conexion = ConectarMysql.conectar()

# fin conMysql.py
