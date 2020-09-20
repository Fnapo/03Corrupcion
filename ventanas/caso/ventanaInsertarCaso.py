# inicio ventanaInsertarCaso

from PyQt5 import QtWidgets, QtGui
from ventanas.caso.insertarCaso import Ui_VentanaCaso
from ventanas.ventanaAccionMysql import VentanaAccionMysql
from ventanas.prepararInputs import PrepararInputs
from ventanas.errorCampoModal import ErrorCampoModal
import locale


class VentanaInsertarCaso(VentanaAccionMysql, Ui_VentanaCaso):
    '''
    Ventana para insertar un Caso.
    '''

    # static attibutos
    _min = 50000.0
    _max = 1000000.0

    def __init__(self):
        try:
            super(VentanaInsertarCaso, self).__init__()
        except ConnectionError:
            raise ConnectionError
        else:
            self.setupUi(self)
            self.botonAceptar.clicked.connect(self._accion)
            self.botonCancelar.clicked.connect(self.close)
            self.botonResetear.clicked.connect(self._resetear)
            validadorDoble = QtGui.QDoubleValidator(
                self._min, self._max, 2)
            validadorDoble.setNotation(validadorDoble.StandardNotation)
            self.inputMontante.setValidator(validadorDoble)
        # fin try
    # fin __init__

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto.
        '''
        credencial, montante = self._obtenerCampos()
        valor = PrepararInputs.pasarMonedaFloat(montante)
        consulta = f"INSERT INTO casos \
            (credencial, montante) \
            VALUES ('{credencial}', {valor})"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta

    def _validarCampos(self) -> bool:
        '''
        Devuelve True si los campos son válidos.
        '''
        credencial, montante = self._obtenerCampos()
        minimo = 4
        if len(credencial) < minimo:
            ErrorCampoModal.errorCampoCorto("Credencial", minimo)
            return False
        elif len(montante) == 0:
            ErrorCampoModal.errorCampoVacio("Montante")
            return False
        else:
            valor = PrepararInputs.pasarMonedaFloat(montante)
            if PrepararInputs.estaValorEntre(valor, self._min, self._max):
                return True
            else:
                cadenaMin = PrepararInputs.pasarFloatMoneda(self._min)
                cadenaMax = PrepararInputs.pasarFloatMoneda(self._max)
                ErrorCampoModal.errorFueraRango(
                    "Montante", cadenaMin, cadenaMax)
                return False
            # fin if in
        # fin if len
    # fin _validarCampos

    def _prepararCampos(self):
        '''
        Prepara el formato de los campos Inputs.
        '''
        credencial, montante = self._obtenerCampos()
        self.inputCredencial.setText(
            PrepararInputs.prepararCadenaMay(credencial))
        if len(montante) > 0:
            self.inputMontante.setText(
                PrepararInputs.prepararComoMoneda(montante, False))
    # fin _prepararCampos

    def _obtenerCampos(self):
        return self.inputCredencial.text(), self.inputMontante.text()
    # fin _obtenerCampos

    def _resetear(self):
        self.inputCredencial.setText("")
        self.inputMontante.setText("")
    # fin _resetear
# fin VentanaInsertarCaso


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = VentanaInsertarCaso()
    except ConnectionError:
        ErrorCampoModal.errorConexion()
    else:
        ui.show()
        app.exec_()
    # fin try
# fin if test

# fin ventanaInsertarCaso
