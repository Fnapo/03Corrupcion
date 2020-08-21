# inicio introducirPartido.py

# from introducirPartido_ui import Ui_introducirPartido
import introducirPartido_ui as uiVip
from PyQt5 import QtCore, QtGui, QtWidgets
import clases.conMysql as cConMysql

class Basura(cConMysql.ConectarMysql):
    pass

class VentanaIntroducirPartido(QtWidgets.QDialog, uiVip.Ui_introducirPartido):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.botonLogo.clicked.connect(self.buscarLogo)
        self.botonAdd.clicked.connect(self.addPartido)
        
    # fin __init__

    def addPartido(self):
        pass

    # fin addPartido
    
    def buscarLogo(self):
        fNombre = QtWidgets.QFileDialog.getOpenFileName(
            self, "Buscando un Logo", ".\\imagenes", "Ficheros de imágenes (*.jpg *.gif *.jpeg)")
        if len(fNombre[0]) > 0:
            self.inputLogo.setText(fNombre[0])
            miQpixmax = QtGui.QPixmap(fNombre[0])
            self.labelLogo.setPixmap(miQpixmax.scaled(100, 100))

    # fin buscarLogo

# fin clase VentanaIntroducirPartido

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = VentanaIntroducirPartido()
    ui.show()
    sys.exit(app.exec_())

# fin introducirPartido.py
