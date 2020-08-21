# inicio conMysql.py

import mysql.connector as conMysql
from mysql.connector import Error, errorcode

# inicio class ConectarMysql


class ConectarMysql(object):
    @staticmethod
    def conectar():
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
        else:
            print(f"Conexión correcta ... {conex}")
            conex.close()

    # fin conectar()

# fin class ConectarMysql


if __name__ == "__main__":
    conexion = ConectarMysql.conectar()

# fin conMysql.py
