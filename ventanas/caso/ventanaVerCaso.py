# inicio ventanaVerCaso

from caso.ventanaEditarCaso import VentanaEditarCaso
from PyQt5 import QtWidgets


class VentanaVerCaso(VentanaEditarCaso):
    '''
    Ventana para ver un Caso
    '''

    def __init__(self, identificador: int):
        try:
            super(VentanaVerCaso, self).__init__(identificador)
        except:
            raise Exception
        else:
            self.setWindowTitle("Ver un Caso")
            self.botonAceptar.setText("Aceptar")
            self.botonResetear.setEnabled(False)
            self.inputCredencial.setReadOnly(True)
            self.inputMontante.setReadOnly(True)
    # fin __init__

    def _accion(self):
        self.close()
# fin VentanaVerCaso


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = VentanaVerCaso(1)
        ui.show()
        sys.exit(app.exec_())
    except:
        pass
# fin if test

# fin ventanaVerCaso
