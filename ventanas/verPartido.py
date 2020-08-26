# inicio verPartido

from editarPartido import VentanaEditarPartido as VEP
from PyQt5 import QtCore, QtGui, QtWidgets

class VentanaVerPartido(VEP):
    '''
    Ventana para ver un Partido
    '''

    def __init__(self, identificador: int):
        try:
            VEP.__init__(self, identificador)
        except:
            raise Exception
        else:
            self.setWindowTitle("Ver un partido")
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
        app.exec_()
    except:
        pass
# fin if test
# fin verPartido
