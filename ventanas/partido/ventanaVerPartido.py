# inicio ventanaVerPartido

from ventanas.partido.ventanaEditarPartido import VentanaEditarPartido
from PyQt5 import QtGui, QtWidgets
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaVerPartido(VentanaEditarPartido):
    '''
    Ventana para ver un Partido
    '''

    def __init__(self, identificador: int):
        super(VentanaVerPartido, self).__init__(identificador)
        self.setWindowTitle("Ver un Partido")
        self.botonAceptar.setText("Aceptar")
        self.botonCancelar.setEnabled(False)  
        self.botonResetear.setEnabled(False)   
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

# fin ventanaVerPartido
