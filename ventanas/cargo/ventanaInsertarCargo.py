# inicio ventanaInsertarCargo

from PyQt5 import QtWidgets
from ventanas.prepararInputs import PrepararInputs
from ventanas.accionMysql import AccionMysql
from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.cargo.insertarCargo import Ui_Dialog


class VentanaInsertarCargo(QtWidgets.QDialog, Ui_Dialog, AccionMysql):
    '''
    Ventana para insertar un Cargo
    '''

    def __init__(self):
        super(VentanaInsertarCargo, self).__init__()
        AccionMysql.__init__(self)
        self.setupUi(self)
        self.botonAceptar.clicked.connect(self._accion)
        self.botonResetear.clicked.connect(self._resetear)
    # fin __init__

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto
        '''
        cargo = self._obtenerCampos()
        consulta = f"INSERT INTO cargos \
            (cargo) \
            VALUES ('{cargo}')"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta

    def _resetear(self):
        self.inputCargo.setText("")

    def _validarCampos(self) -> bool:
        '''
        Devuelve True si los campos son válidos
        '''
        cargo = self._obtenerCampos()
        minimo = 4
        mensaje = "Campo vacío o muy corto: '{}'.\nMínimo {} Caracteres."
        errorCM = ErrorCampoModal()
        if len(cargo) < minimo:
            errorCM.mostrar(mensaje.format("Cargo", minimo))
            return False

        return True
    # fin _validarCampos

    def _prepararCampos(self):
        '''
        Prepara el formato de los campos Inputs
        '''
        cargo = self._obtenerCampos()
        self.inputCargo.setText(PrepararInputs.prepararCadenaCap(cargo))
    # fin _prepararCampos

    def _obtenerCampos(self):
        '''
        Obtiene los valores de los campos Inputs
        '''
        return self.inputCargo.text()
    # fin _obtenerCampos
# fin VentanaInsertarCargo


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication([])
        ventana = VentanaInsertarCargo()
        ventana.show()
        app.exec_()
    except BaseException:
        ErrorCampoModal.errorConexion()
    # fin try
# fin if test

# fin ventanaInsertarCargo
