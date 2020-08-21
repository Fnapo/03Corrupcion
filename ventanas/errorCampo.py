# inicio errorCampo.py

import errorCampo_ui as uiVec
from PyQt5 import QtCore, QtGui, QtWidgets

class ErrorCampo(QtWidgets.QDialog, uiVec.Ui_errorCampo):
    def __init__(self, campo: str):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.botonAceptar.clicked.connect(self.close)
        self.label01.setText(self.label01.text() + f" {campo}")
    
    # fin __init__

# fin class ErrorCampo
app = QtWidgets.QApplication([])
ventana = ErrorCampo("Hola")
ventana.show()
app.exec_()
# fin errorCampo.py
