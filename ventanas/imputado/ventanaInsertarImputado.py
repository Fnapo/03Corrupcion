# inicio ventanaInsertarImputado

from PyQt5 import QtWidgets, QtCore
from datetime import date, timedelta
from ventanas.prepararInputs import PrepararInputs
from ventanas.ventanaAccionMysql import VentanaAccionMysql
from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.imputado.insertarImputado import Ui_insertarImputado
from ventanas.partido.seleccionarPartidos import SeleccionarPartidos
from ventanas.partido.ventanaListarPartidos import VentanaListarPartidos
from ventanas.cargo.seleccionarCargos import SeleccionarCargos
from ventanas.cargo.ventanaListarCargos import VentanaListarCargos


class VentanaInsertarImputado(VentanaAccionMysql, Ui_insertarImputado):
    '''
    Ventana para insertar un Imputado.
    '''

    # static atributos
    _listaRH = ['A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-']

    def __init__(self):
        super(VentanaInsertarImputado, self).__init__()
        self.setupUi(self)
        self.botonAceptar.clicked.connect(self._accion)
        self.botonCancelar.clicked.connect(self.close)
        self.botonResetear.clicked.connect(self._resetear)
        self._listaPartidos = []
        self._listaCargos = []
        self._llenarPartidos()
        for item in self._listaPartidos:
            self.inputPartido.addItem(item[0])
        self._llenarCargos()
        for item in self._listaCargos:
            self.inputCargo.addItem(item[0])
        for item in VentanaInsertarImputado._listaRH:
            self.inputGrupoRH.addItem(item)
        hoy = date.today()
        fechaMin = hoy - timedelta(days=100*365)
        fechaMax = hoy - timedelta(days=18*365)
        self.inputFecha.setDateRange(fechaMin, fechaMax)
        self.inputFecha.setDate(hoy-timedelta(days=20*365))
        self.inputFecha.setCalendarPopup(True)
    # fin __init__

    def _llenarCargos(self):
        '''
        Llena la lista de los Partidos.
        '''
        VentanaAccionMysql._conexion.reconnect()
        lista = SeleccionarCargos.obtenerTodosCargos(
            VentanaAccionMysql._conexion)
        self._listaCargos.append(("  Selecciona un Cargo", -1))
        while len(lista) > 0:
            cargo = lista.pop()
            self._listaCargos.append(VentanaListarCargos.prepararCargo(cargo))
        self._listaCargos.sort()
    # fin _llenarCargos

    def _llenarPartidos(self):
        '''
        Llena la lista de los Partidos.
        '''
        VentanaAccionMysql._conexion.reconnect()
        lista = SeleccionarPartidos.obtenerTodosPartidos(
            VentanaAccionMysql._conexion)
        self._listaPartidos.append(("  Selecciona un Partido", -1))
        while len(lista) > 0:
            partido = lista.pop()
            self._listaPartidos.append(
                VentanaListarPartidos.prepararPartido(partido))
        self._listaPartidos.sort()
    # fin _llenarPartidos

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto.
        '''
        nombre, apellidos, id_partido, id_cargo, grupoRH, fecha = \
            self._obtenerCampos()
        cadenaFecha = fecha.toString("yyyy-MM-dd")
        consulta = f"INSERT INTO imputados \
            (nombre, apellidos, fk_partido, fk_cargo, grupoRH, nacimiento) \
            VALUES ('{nombre}', '{apellidos}', {id_partido}, \
            {id_cargo}, '{grupoRH}', '{cadenaFecha}')"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta

    def _resetear(self):
        self.inputNombre.setText("")
        self.inputApellidos.setText("")
        self.inputPartido.setCurrentIndex(0)
        self.inputCargo.setCurrentIndex(0)
        self.inputGrupoRH.setCurrentIndex(0)
        self.inputFecha.setDate(date.today()-timedelta(days=20*365))
    # fin _resetear

    def _validarCampos(self) -> bool:
        '''
        Devuelve True si los campos son válidos.
        '''
        nombre, apellidos, id_partido, id_cargo, grupoRH, fecha = \
            self._obtenerCampos()
        minimo = 2
        if len(nombre) < minimo:
            errorCM = ErrorCampoModal.errorCampoCorto("Nombre", minimo)
            return False
        if len(apellidos) < minimo:
            errorCM = ErrorCampoModal.errorCampoCorto("Apellidos", minimo)
            return False
        if id_partido < 0:
            errorCM = ErrorCampoModal.errorFaltaCampo("un partido político")
            return False
        if id_cargo < 0:
            errorCM = ErrorCampoModal.errorFaltaCampo("un cargo político")
            return False

        return True
    # fin _validarCampos

    def _prepararCampos(self):
        '''
        Prepara el formato de los campos Inputs.
        '''
        nombre, apellidos, id_partido, id_cargo, grupoRH, fecha = \
            self._obtenerCampos()
        self.inputNombre.setText(PrepararInputs.prepararCadenaCap(nombre))
        self.inputApellidos.setText(
            PrepararInputs.prepararCadenaCap(apellidos))
    # fin _prepararCampos

    def _obtenerCampos(self):
        '''
        Obtiene los valores de los campos Inputs.
        '''
        indicePartido = self.inputPartido.currentIndex()
        indiceCargo = self.inputCargo.currentIndex()

        return self.inputNombre.text(), self.inputApellidos.text(), int(self._listaPartidos[indicePartido][1]), int(self._listaCargos[indiceCargo][1]), self.inputGrupoRH.currentText(), QtCore.QDate(self.inputFecha.date())
    # fin _obtenerCampos
# fin VentanaInsertarImputado


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication([])
        ventana = VentanaInsertarImputado()
        ventana.show()
        app.exec_()
    except ConnectionError:
        ErrorCampoModal.errorConexion()
    # fin try
# fin if test

# fin ventanaInsertarImputado
