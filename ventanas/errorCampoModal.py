# inicio errorCampoModal.py

import errorCampo_ui as uiVec
from PyQt5 import QtCore, QtGui, QtWidgets


class ErrorCampoModal(QtWidgets.QDialog, uiVec.Ui_errorCampo):
    def __init__(self, mensaje: str):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.botonAceptar.clicked.connect(self.close)
        self.label01.setText(mensaje)
    # fin __init__
    
    @staticmethod
    def mostrar(mensaje: str):
        error = ErrorCampoModal(mensaje)
        error.exec()
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
