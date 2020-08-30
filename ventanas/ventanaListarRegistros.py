# inicio ventanaListarRegistros

from ventanaLista import Ui_ventanaLista
from PyQt5 import QtWidgets
from clases.conectarMysql import ConectarMysql
from errorCampoModal import ErrorCampoModal
from padreVentanaLista import PadreVentanaLista


class VentanaListarRegistros(QtWidgets.QDialog, Ui_ventanaLista):
    '''
    Ventana que lista unos registros para elegir uno de ellos
    '''

    def __init__(self, padre: PadreVentanaLista):
        super(VentanaListarRegistros, self).__init__()
        self.padre = padre
        self.setupUi(self)
        try:
            conexion = ConectarMysql.conectar()
        except:
            raise Exception
        else:
            conexion.close()
            listaOrdenada = self._obtenerListaOrdenada()
            if len(listaOrdenada) > 0:
                for cadena in listaOrdenada:
                    self.comboLista.addItem(cadena)
                self.botonAceptar.clicked.connect(self._registroSeleccionado)
                self.botonCancelar.clicked.connect(self.close)
            else:
                vacia = ErrorCampoModal("Sin registros")
                vacia.mostrar("Tabla sin registros")
                raise Exception
            # fin if
        # fin try
    # fin __init__

    def _registroSeleccionado(self):
        cadena = self.comboLista.currentText()
        entero = self._obtenerID(cadena)
        self.close()
        self.padre._tratarRegistro(entero)
    # fin _registroSeleccionado

    @staticmethod
    def _obtenerID(cadena: str) -> int:
        '''
        Dado un ítem preparado (cadena) obtiene el 'id' del registro asociado
        '''
        inicio = 0
        posible = 0
        while posible != -1:
            posible = cadena.find("(", inicio)
            if posible != -1:
                inicio = posible + 1
        # fin while
        fin = cadena.find(")", inicio)

        return int(cadena[inicio:fin])
    # fin _obtenerID

    @staticmethod
    def _prepararItem(item: tuple) -> str:
        '''
        Prepara el item para insertarlo en el QComboBox
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

    def _obtenerListaOrdenada(self) -> list:
        '''
        Obtiene una lista ordenada con todos los registros
        '''
        lista = self._obtenerTodosRegistros()
        listaOrdenada = []
        while len(lista) > 0:
            item = lista.pop()
            cadena = self._prepararItem(item)
            listaOrdenada.append(cadena)
        listaOrdenada.sort()

        return listaOrdenada
    # fin obtenerListaOrdenada

# fin ventanaListarRegistros
