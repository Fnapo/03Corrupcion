# inicio ventanaConexionMysql

from ventanas.conexionMysql import ConexionMysql
from PyQt5 import QtWidgets


class VentanaConexionMysql(QtWidgets.QDialog, ConexionMysql):
    '''
    Ventana con una conexión a una BBDD Mysql.
    '''

    def __init__(self):
        super(VentanaConexionMysql, self).__init__()
        # ConexionMysql.__init__(self)
    # fin __init__
# fin VentanaConexionMysql

# fin ventanaConexionMysql
