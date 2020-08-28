# inicio verPartido

from editarPartido import VentanaEditarPartido
from PyQt5 import QtCore, QtGui, QtWidgets

class VentanaVerPartido(VentanaEditarPartido):
    '''
    Ventana para ver un Partido
    '''

    def __init__(self, identificador: int):
        try:
            VentanaEditarPartido.__init__(self, identificador)
        except:
            raise Exception
        else:
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
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = VentanaVerPartido(1)
        ui.show()
        sys.exit(app.exec_())
    except:
        pass
# fin if test

# fin verPartido
