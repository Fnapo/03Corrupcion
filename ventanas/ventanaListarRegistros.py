# inicio ventanaListarRegistros

from ventanas.ventanaLista import Ui_ventanaLista
from ventanas.ventanaConexionMysql import VentanaConexionMysql
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaListarRegistros(VentanaConexionMysql, Ui_ventanaLista):
    '''
    Ventana abstracta que lista unos Registros para elegir uno de ellos.
    '''

    # atributo static
    _anchura = 50

    def __init__(self):
        try:
            super(VentanaListarRegistros, self).__init__()
        except ConnectionError:
            self._salida = -2
            raise ConnectionError
        else:
            self._salida = -1
            self.setupUi(self)
            self._listaOrdenada = []
            VentanaConexionMysql._conexion.reconnect()
            self._llenarListaOrdenada()
            VentanaConexionMysql._conexion.close()
            if len(self._listaOrdenada) > 0:
                for item in self._listaOrdenada:
                    self.comboLista.addItem(item[0])
                self.botonAceptar.clicked.connect(self._registroSeleccionado)
                self.botonCancelar.clicked.connect(self._cerrar)
            else:
                raise ValueError
            # fin if len
        # fin try conexion
    # fin __init__

    def verIDRegistro(self):
        '''
        Muestra el 'id' del registro seleccionado
        '''
        return self._salida
    # fin verIDRegistro
    
    def _cerrar(self)->int:
        '''
        Acción al cerrar la ventana actual
        '''
        self.close()
        self._salida = -3
    # fin _cerrar

    def _registroSeleccionado(self):
        '''
        Devuelve el 'id' del registro seleccionado
        '''
        entero = self.comboLista.currentIndex()
        self.close()
        self._salida = self._listaOrdenada[entero][1]
    # fin _registroSeleccionado

    @staticmethod
    def _prepararItem(item: tuple) -> tuple:
        '''
        Prepara el item para insertarlo en el QComboBox.

        La Tupla tiene el siguientge aspecto: tuple = str, int
        '''
        raise NotImplementedError
    # fin

    @staticmethod
    def _obtenerTodosRegistros() -> list:
        '''
        Obtiene todos los registros asociados
        '''
        raise NotImplementedError
    # fin obtenerTodosRegistros

    def _llenarListaOrdenada(self):
        '''
        Llena una lista y la ordenada con todos los registros.
        '''
        lista = self._obtenerTodosRegistros()
        while len(lista) > 0:
            item = lista.pop()
            cadena, identificador = self._prepararItem(item)
            self._listaOrdenada.append((cadena, identificador))
        self._listaOrdenada.sort()
    # fin _llenarListaOrdenada
# fin VentanaListarRegistros

# fin ventanaListarRegistros
