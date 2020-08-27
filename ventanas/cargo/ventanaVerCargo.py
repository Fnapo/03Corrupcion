# inicio ventanaVerCargo

from cargo.ventanaEditarCargo import VentanaEditarCargo
from PyQt5 import QtCore, QtGui, QtWidgets

class VentanaVerCargo(VentanaEditarCargo):
    '''
    Ventana para ver un Cargo
    '''

    def __init__(self, identificador: int):
        try:
            VentanaEditarCargo.__init__(self, identificador)
        except:
            raise Exception
        else:
            self.setWindowTitle("Ver un Cargo")
            self.botonAceptar.setText("Aceptar")
            self.botonResetear.setEnabled(False)
            self.inputCargo.setReadOnly(True)
    # fin __init__

    def _accion(self):
        self.close()
# fin VentanaVerCargo

if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = VentanaVerCargo(1)
        ui.show()
        sys.exit(app.exec_())
    except:
        pass
# fin if test
# fin ventanaVerCargo
