# inicio ventanaAccionMysql

from PyQt5 import QtWidgets
from ventanas.accionMysql import AccionMysql


class VentanaAccionMysql(QtWidgets.QDialog, AccionMysql):
    '''
    Ventana con una conexion Mysql para realizar una acción.
    '''

    def __init__(self):
        super(VentanaAccionMysql, self).__init__()
    # fin __init__
# fin VentanaAccionMysql

# fin ventanaAccionMysql
