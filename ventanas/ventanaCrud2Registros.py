# inicio ventanaCrud2Registros

from PyQt5 import QtWidgets
from ventanas.ventanaCRUD2 import Ui_ventanaCrud2
from ventanas.ventanaConexionMysql import VentanaConexionMysql


class VentanaCrud2Registros(VentanaConexionMysql, Ui_ventanaCrud2):
    '''
    Ventana abstracta para elegir la acción CRUD ampliada.
    '''

    def __init__(self):
        try:
            super(VentanaCrud2Registros, self).__init__()
        except:
            raise ConnectionError
        else:
            self.setupUi(self)
            self.crearRegistro.clicked.connect(self._crear)
            self.verRegistro.clicked.connect(self._ver)
            self.editarRegistro.clicked.connect(self._editar)
            self.borrarRegistro.clicked.connect(self._borrar)
            self.cancelar.clicked.connect(self.close)
            self._llenarCombos()
            self.botonCrearMul.clicked.connect(self._crearMultiple)
            self.botonBorrarMul.clicked.connect(self._borrarMultiple)
        # fin try
    # fin __init__

    def _llenarCombos(self):
        '''
        Rellena los combos de la ventana.
        '''
        raise NotImplementedError
    # fin _llenarCombos
    
    def _borrarMultiple(self):
        '''
        Función para borrar una relación múltiple.
        '''
        raise NotImplementedError
    # fin _borrarMultiple
    
    def _crearMultiple(self):
        '''
        Función para crear una relación múltiple.
        '''
        raise NotImplementedError
    # fin _crearMultiple

    def _borrar(self):
        '''
        Función para borrar un registro.
        '''
        raise NotImplementedError
    # fin _borrar

    def _editar(self):
        '''
        Función para editar un registro.
        '''
        raise NotImplementedError
    # fin _editar

    def _ver(self):
        '''
        Función para ver un registro.
        '''
        raise NotImplementedError
    # fin _ver

    def _crear(self):
        '''
        Función para insertar un registro.
        '''
        raise NotImplementedError
    # fin _insertar
# fin VentanaCrud2Registros

# fin ventanaCrud2Registros
