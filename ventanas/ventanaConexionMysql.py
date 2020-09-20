# inicio ventanaConexionMysql

from ventanas.conexionMysql import ConexionMysql
from PyQt5 import QtWidgets


class VentanaConexionMysql(QtWidgets.QDialog, ConexionMysql):
    '''
    Ventana con una conexión a una BBDD Mysql.
    '''

    def __init__(self):
        try:
            super(VentanaConexionMysql, self).__init__()
        except:
            raise ConnectionError
    # fin __init__
# fin VentanaConexionMysql

# fin ventanaConexionMysql
