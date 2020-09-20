# inicio ventanaAccionMysql

from PyQt5 import QtWidgets
from ventanas.accionMysql import AccionMysql


class VentanaAccionMysql(QtWidgets.QDialog, AccionMysql):
    '''
    Ventana con una conexion Mysql para realizar una acción.
    '''

    def __init__(self):
        try:
            super(VentanaAccionMysql, self).__init__()
        except:
            raise ConnectionError
    # fin __init__
# fin VentanaAccionMysql

# fin ventanaAccionMysql
