# inicio verPartido

from ventanas.partido.editarPartido import VentanaEditarPartido
from PyQt5 import QtGui, QtWidgets
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaVerPartido(VentanaEditarPartido):
    '''
    Ventana para ver un Partido
    '''

    def __init__(self, identificador: int):
        VentanaEditarPartido.__init__(self, identificador)
        self.setWindowTitle("Ver un Partido")
        self.botonAdd.setText("Aceptar")
        self.botonRes.setEnabled(False)
        self.inputNombre.setReadOnly(True)
        self.inputSiglas.setReadOnly(True)
        self.botonLogo.setEnabled(False)
    # fin __init__

    def _accion(self):
        self.close()
# fin VentanaVerPartido


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication([])
        id = 1
        ui = VentanaVerPartido(id)
        ui.show()
        app.exec_()
    except ConnectionError:
        ErrorCampoModal.errorConexion()
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
# fin if test

# fin verPartido
