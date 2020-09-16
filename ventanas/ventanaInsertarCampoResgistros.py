# inicio ventanaInsertarCampoRegistros

from ventanas.ventanaConexionMysql import VentanaConexionMysql
from ventanas.clases.conectarMysql import ConectarMysql
from ventanas.insertarRelacion import Ui_insertarRelacion
from PyQt5 import QtWidgets, QtCore


class VentanaInsertarCampoRegistros(VentanaConexionMysql, Ui_insertarRelacion):
    '''
    Relaciona unos Registros con un Campo dado.
    '''

    def __init__(self, identificador: int):
        try:
            super(VentanaInsertarCampoRegistros, self).__init__()
            self.setupUi(self)
        except ConnectionError:
            raise ConnectionError
        else:
            self._identificador = identificador
            try:
                self._prepararTabla()
            except ValueError:
                raise ValueError
            except IndexError:
                raise IndexError
            else:
                self.botonAceptar.clicked.connect(self._realizarAccion)
                self.botonCancelar.clicked.connect(self.close)
                self.botonResetear.clicked.connect(self._resetear)
            # fin try _prepararTabla
        # fin try super
    # fin __init__

    def _resetear(self):
        '''
        Reinicia todos los CkeckBoxs.
        '''
        for fila in range(len(self._registros)):
            self._crearCheckBox(fila)
    # fin _resetear

    def _crearConsulta(self, fila: int) -> str:
        '''
        Crea la consulta SQL correspondiente.
        '''
        raise NotImplementedError
    # fin _crearConsulta

    def _esCorrecto(self, checkeo: bool) -> bool:
        '''
        ¿Con qué se actúa .. con True o False?
        '''
        raise NotImplementedError
    # fin _esCorrecto

    def _realizarAccion(self):
        '''
        Realiza la acción CRUD pertinente.
        '''
        for fila in range(len(self._registros)):
            hijos = self.tablaRegistros.cellWidget(fila, 0).children()
            checkeo = hijos[1].isChecked()
            if self._esCorrecto(checkeo):
                VentanaInsertarCampoRegistros._conexion.reconnect()
                cadena = self._crearConsulta(fila)
                ConectarMysql.ejecutar(VentanaInsertarCampoRegistros
                                       ._conexion, cadena)
                VentanaInsertarCampoRegistros._conexion.close()
            # fin if
        # fin for
        self.close()
    # fin _realizarAccion

    def _tratarRegistro(self, fila: int) -> str:
        '''
        Trata el Registro dado.
        '''
        raise NotImplementedError
    # fin _tratarRegistro

    def _obtenerRegitros(self):
        '''
        Obtiene los Registros no relacionados con el Campo.
        '''
        raise NotImplementedError
    # fin _obtenerRegitros

    def _obtenerCampo(self) -> list:
        '''
        Obtiene el Campo dado.
        '''
        raise NotImplementedError
    # fin _obtenerCampo

    def _inicializarCheckBox(self) -> bool:
        raise NotImplementedError
    # fin _inicializarCheckBox

    def _cadenaCheckBox(self) -> str:
        raise NotImplementedError
    # fin _cadenaCheckBox

    def _crearCheckBox(self, fila: int) -> QtWidgets.QWidget:
        '''
        Crea una CheckBox en una celda de una TableWidget.
        '''
        elementoCheckBox = QtWidgets.QCheckBox()
        elementoCheckBox.setText(self._cadenaCheckBox())
        elementoCheckBox.setChecked(self._inicializarCheckBox())
        elementoCelda = QtWidgets.QHBoxLayout()
        elementoCelda.setAlignment(QtCore.Qt.AlignCenter)
        elementoCelda.addWidget(elementoCheckBox)
        nuevoWidget = QtWidgets.QWidget()
        nuevoWidget.setLayout(elementoCelda)

        return nuevoWidget
    # fin _crearCheckBox

    def _crearLabel(self, fila: int) -> QtWidgets.QLabel:
        '''
        Crea y coloca una Label en una celda de una TableWidget.        
        '''
        elementoLabel = QtWidgets.QLabel()
        cadenaRegistro = self._tratarRegistro(fila)
        elementoLabel.setText(cadenaRegistro)
        elementoLabel.setAlignment(QtCore.Qt.AlignCenter)

        return elementoLabel
    # fin _crearLabel

    def _prepararCampo(self, campo: list) -> str:
        '''
        Prepara el Campo como una cadena.
        '''
        raise NotImplementedError
    # fin _prepararCampo

    def _cambiarLabels(self, campoCadena: str):
        '''
        Cambia el texto de las primeras labels de la Ventana.
        '''
        raise NotADirectoryError
    # fin _cambiarLabels

    def _llenarTablaVacia(self):
        '''
        Llena una tabla vacía.
        '''
        elementoLabel = QtWidgets.QLabel()
        elementoLabel.setText("")
        elementoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tablaRegistros.setCellWidget(0, 0, elementoLabel)
        elementoLabel = QtWidgets.QLabel()
        elementoLabel.setText("Sin Registros Adecuados")
        elementoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tablaRegistros.setCellWidget(0, 1, elementoLabel)
    # fin _llenarTablaVacia

    def _prepararTabla(self):
        self._conexion.reconnect()
        campo = self._obtenerCampo()
        self._conexion.close()
        if len(campo) == 0:
            raise ValueError
        campoCadena = self._prepararCampo(campo)
        self._conexion.reconnect()
        self._registros = []
        self._obtenerRegitros()
        self._conexion.close()
        if len(self._registros) == 0:
            self.tablaRegistros.setRowCount(1)
            self._llenarTablaVacia()
        else:
            cuantosRegistros = len(self._registros)
            self.tablaRegistros.setRowCount(cuantosRegistros)
            for fila in range(cuantosRegistros):
                elementoCheckbox = self._crearCheckBox(fila)
                self.tablaRegistros.setCellWidget(fila, 0, elementoCheckbox)
                elementoLabel = self._crearLabel(fila)
                self.tablaRegistros.setCellWidget(fila, 1, elementoLabel)
            # fin for
        self._cambiarLabels(campoCadena)
    # fin _prepararTabla
# fin VentanaInsertarCampoRegistros

# fin ventanaInsertarCampoRegistros
