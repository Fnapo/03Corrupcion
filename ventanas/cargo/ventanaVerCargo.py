# inicio ventanaVerCargo

from ventanas.cargo.ventanaEditarCargo import VentanaEditarCargo
from PyQt5 import QtWidgets
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaVerCargo(VentanaEditarCargo):
    '''
    Ventana para ver un Cargo
    '''

    def __init__(self, identificador: int):
        VentanaEditarCargo.__init__(self, identificador)
        self.setWindowTitle("Ver un Cargo")
        self.botonAceptar.setText("Aceptar")
        self.botonCancelar.setEnabled(False)  
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
        app.exec_()
    except Exception:
        ErrorCampoModal.errorNoRegistro(id)
    except BaseException:
        ErrorCampoModal.errorConexion()
# fin if test

# fin ventanaVerCargo
