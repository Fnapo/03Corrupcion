# inicio errorCampoModal.py

import errorCampo_ui as uiVec
from PyQt5 import QtCore, QtGui, QtWidgets


class ErrorCampoModal(QtWidgets.QDialog, uiVec.Ui_errorCampo):
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
    ventana.show()
    sys.exit(app.exec_())
# fin if test

# fin errorCampoModal.py
