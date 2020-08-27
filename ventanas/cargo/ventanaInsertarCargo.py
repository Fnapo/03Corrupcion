# inicio ventanaInsertarCargo

from PyQt5 import QtCore, QtGui, QtWidgets
from prepararInputs import PrepararInputs
from clases.conectarMysql import ConectarMysql
from errorCampoModal import ErrorCampoModal
from cargo.insertarCargo import Ui_Dialog


class VentanaInsertarCargo(QtWidgets.QDialog, Ui_Dialog, ConectarMysql):
    '''
    Ventana para insertar un Cargo
    '''
    
    def __init__(self):
        try:
            QtWidgets.QDialog.__init__(self)
            self.setupUi(self)
            ConectarMysql.__init__(self)
        except:
            raise Exception
        else:
            self.botonAceptar.clicked.connect(self._accion)
            self.botonResetear.clicked.connect(self._resetear)
        # fin try
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
    except:
        pass
    else:
        sys.exit(app.exec_())
    # fin try
# fin if test

# fin ventanaInsertarCargo
