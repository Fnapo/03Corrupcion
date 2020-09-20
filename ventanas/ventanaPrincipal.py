# inicio ventanaPrincipal

from ventanas.ventanaInicial import Ui_ventanaInicial
from ventanas.ventanaConexionMysql import VentanaConexionMysql
from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.cargo.ventanaCrudCargo import VentanaCrudCargo
from ventanas.caso.ventanaCrud2Caso import VentanaCrud2Caso
from ventanas.imputado.ventanaCrud2Imputado import VentanaCrud2Imputado
from ventanas.partido.ventanaCrudPartido import VentanaCrudPartido


class VentanaPrincipal(VentanaConexionMysql, Ui_ventanaInicial):
    '''
    Ventana Principal Inicial.
    '''

    def __init__(self):
        try:
            super(VentanaPrincipal, self).__init__()
        except ConnectionError:
            ErrorCampoModal.errorConexion()
        else:
            self.setupUi(self)
            self.botonCargos.clicked.connect(self._accionCrudCargo)
            self.botonCasos.clicked.connect(self._accionCrudCaso)
            self.botonImputados.clicked.connect(self._accionCrudImputado)
            self.botonPartidos.clicked.connect(self._accionCrudPartido)
            self.botonCancelar.clicked.connect(self.close)
        # fin try
    # fin __init__

    def _accionCrudPartido(self):
        '''
        Función para trabajar con los Partidos.
        '''
        self.hide()
        ventanaCargo = VentanaCrudPartido()
        ventanaCargo.exec_()
        self.show()
    # fin _accionCrudPartido

    def _accionCrudImputado(self):
        '''
        Función para trabajar con los Imputados.
        '''
        self.hide()
        ventanaCaso = VentanaCrud2Imputado()
        ventanaCaso.exec_()
        self.show()
    # fin _accionCrudImputado

    def _accionCrudCaso(self):
        '''
        Función para trabajar con los Cargos.
        '''
        self.hide()
        ventanaCaso = VentanaCrud2Caso()
        ventanaCaso.exec_()
        self.show()
    # fin _accionCrudCaso

    def _accionCrudCargo(self):
        '''
        Función para trabajar con los Cargos.
        '''
        self.hide()
        ventanaCargo = VentanaCrudCargo()
        ventanaCargo.exec_()
        self.show()
    # fin _accionCrudCargo
# fin VentanaPrincipal

# fin ventanaPrincipal
