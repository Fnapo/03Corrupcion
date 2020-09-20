# inicio ventanaVerCaso

from ventanas.caso.ventanaEditarCaso import VentanaEditarCaso
from ventanas.errorCampoModal import ErrorCampoModal
from PyQt5 import QtWidgets


class VentanaVerCaso(VentanaEditarCaso):
    '''
    Ventana para ver un Caso
    '''

    def __init__(self, identificador: int):
        try:
            super(VentanaVerCaso, self).__init__(identificador)
        except ConnectionError:
            raise ConnectionError
        except ValueError:
            raise ValueError
        else:
            self.setWindowTitle("Ver un Caso")
            self.botonAceptar.setText("Aceptar")
            self.botonCancelar.setEnabled(False)  
            self.botonResetear.setEnabled(False)
            self.inputCredencial.setReadOnly(True)
            self.inputMontante.setReadOnly(True)
        # fin try
    # fin __init__

    def _accion(self):
        self.close()
# fin VentanaVerCaso


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication([])
        id = 1
        ui = VentanaVerCaso(id)
        ui.show()
        app.exec_()
    except ConnectionError:
        ErrorCampoModal.errorConexion()        
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
# fin if test

# fin ventanaVerCaso
