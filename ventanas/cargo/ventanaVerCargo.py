# inicio ventanaVerCargo

from ventanas.cargo.ventanaEditarCargo import VentanaEditarCargo
from PyQt5 import QtWidgets
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaVerCargo(VentanaEditarCargo):
    '''
    Ventana para ver un Cargo
    '''

    def __init__(self, identificador: int):
        super(VentanaVerCargo, self).__init__(identificador)
        self.setWindowTitle("Ver un Cargo")
        self.botonAceptar.setText("Aceptar")
        self.botonCancelar.setEnabled(False)  
        self.botonResetear.setEnabled(False)      
        self.inputCargo.setEnabled(False)
    # fin __init__

    def _accion(self):
        self.close()
# fin VentanaVerCargo


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ventana = VentanaVerCargo(1)
        ventana.show()
        app.exec_()
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
    except ConnectionError:
        ErrorCampoModal.errorConexion()
# fin if test

# fin ventanaVerCargo
