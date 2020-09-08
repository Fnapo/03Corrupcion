# inicio ventanaAccionMysql3Botones

from ventanas.ventanaAccionMysql import VentanaAccionMysql
from PyQt5 import QtWidgets


class VentanaAccionMysql3Botones(VentanaAccionMysql):
    '''
    Ventana Mysql con 3 Botones.
    '''

    def __init__(self):
        super(VentanaAccionMysql3Botones, self).__init__()
        self.botonAceptar = QtWidgets.QPushButton()
        self.botonCancelar = QtWidgets.QPushButton()
        self.botonResetear = QtWidgets.QPushButton()
        self.botonAceptar.clicked.connect(self._accion)
        self.botonCancelar.clicked.connect(self.close)
        self.botonResetear.clicked.connect(self._resetear)
    # fin __init__

    def _resetar(self):
        '''
        Resetea los campos de la ventana.
        '''
        raise NotImplementedError
    # fin _resetar
# fin VentanaAccionMysql3Botones

# fin ventanaAccionMysql3Botones
