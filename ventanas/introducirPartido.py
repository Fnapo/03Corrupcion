# inicio introducirPartido.py

from introducirPartido_ui import *


class VentanaIntroducirPartido(QtWidgets.QDialog, Ui_introducirPartido):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.botonLogo.clicked.connect(self.buscarLogo)

    def buscarLogo(self):
        fNombre = QtWidgets.QFileDialog.getOpenFileName(self, "Open Files", ".\\imagenes", "Image files (*.jpg *.gif *.png)")
        if len(fNombre[0]) > 0:
            self.inputLogo.setText(fNombre[0])
            miQpixmax = QtGui.QPixmap(fNombre[0])
            self.labelLogo.setPixmap(miQpixmax.scaled(100, 100))
      
#fin clase VentanaIntroducirPartido

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = VentanaIntroducirPartido()
    ui.show()
    sys.exit(app.exec_())
