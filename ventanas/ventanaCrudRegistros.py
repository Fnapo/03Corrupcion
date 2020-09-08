# inicio ventanaCrudRegistros

from PyQt5 import QtWidgets
from ventanas.ventanaCRUD import Ui_ventanaCrud
from ventanas.conexionMysql import ConexionMysql


class VentanaCrudRegistros(QtWidgets.QDialog, Ui_ventanaCrud, ConexionMysql):
    '''
    Ventana abstracta para elegir la acción CRUD
    '''

    def __init__(self):
        super(VentanaCrudRegistros, self).__init__()
        self.setupUi(self)
        ConexionMysql.__init__(self)
        self.crearRegistro.clicked.connect(self._crear)
        self.verRegistro.clicked.connect(self._ver)
        self.editarRegistro.clicked.connect(self._editar)
        self.borrarRegistro.clicked.connect(self._borrar)
        self.cancelar.clicked.connect(self.close)          
    # fin __init__

    def _borrar(self):
        '''
        Función para borrar un registro
        '''
        raise NotImplementedError
    # fin _borrar

    def _editar(self):
        '''
        Función para editar un registro
        '''
        raise NotImplementedError
    # fin _editar

    def _ver(self):
        '''
        Función para ver un registro
        '''
        raise NotImplementedError
    # fin _ver

    def _crear(self):
        '''
        Función para insertar un registro
        '''
        raise NotImplementedError
    # fin _insertar
# fin VentanaCrudRegistros

# fin ventanaCrudRegistros
