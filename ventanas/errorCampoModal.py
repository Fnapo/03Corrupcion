# inicio errorCampoModal.py

from PyQt5 import QtWidgets
from errorCampo_ui import Ui_errorCampo


class ErrorCampoModal(QtWidgets.QDialog, Ui_errorCampo):
    def __init__(self, titulo="Error en un Campo"):
        '''
        Crea una ventana modal con un título dado
        '''
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.botonAceptar.clicked.connect(self.close)
        self.setWindowTitle(titulo)
    # fin __init__

    def mostrar(self, mensaje: str):
        self.label01.setText(mensaje)
        self.exec()
    # fin mostrar
# fin class ErrorCampoModal


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    ventana = ErrorCampoModal("Hola")
    ventana.mostrar("Prueba")
    ventana.show()
    sys.exit(app.exec_())
# fin if test

# fin errorCampoModal.py
