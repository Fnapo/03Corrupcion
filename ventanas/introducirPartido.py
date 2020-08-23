# inicio introducirPartido.py

import introducirPartido_ui as uiVip
from PyQt5 import QtCore, QtGui, QtWidgets
import clases.conMysql as cConMysql
import prepararInputs as cPi
import errorCampoModal as cEcm
from mysql.connector import errorcode


class VentanaIntroducirPartido(QtWidgets.QDialog, uiVip.Ui_introducirPartido):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.botonLogo.clicked.connect(self.__buscarLogo)
        self.botonAdd.clicked.connect(self.__addPartido)
    # fin __init__

    def __addPartido(self):
        self.__prepararCampos()
        if self.__validarCampos():
            nombre, siglas, logo = self.__obtenerCampos()
            conexion = cConMysql.ConectarMysql.conectar()
            errorNumero = 0
            consulta = f"INSERT INTO partidos (nombre, siglas, logo) VALUES ('{nombre}', '{siglas}', '{logo}')"
            try:
                cConMysql.ConectarMysql.insertar(conexion, consulta)
            except Exception as error:
                errorNumero = error.errno
                errorNumero == errorcode.ER_DUP_ENTRY
                cEcm.ErrorCampoModal.mostrar(error.msg)
            else:
                cEcm.ErrorCampoModal.mostrar("Inserción correcta ...")
            finally:
                if conexion.is_connected():
                    conexion.close()

            if errorNumero == 0:
                self.close()
        # fin if validar
    # fin __addPartido

    def __validarCampos(self) -> bool:
        '''
        Devuelve True si los campos son válidos
        '''
        nombre, siglas, logo = self.__obtenerCampos()
        mensaje = "Campo vacío '{}'"
        if len(nombre) == 0:
            cEcm.ErrorCampoModal.mostrar(mensaje.format("Nombre"))
            return False
        elif len(siglas) == 0:
            cEcm.ErrorCampoModal.mostrar(mensaje.format("Siglas"))
            return False
        elif len(logo) == 0:
            cEcm.ErrorCampoModal.mostrar(mensaje.format("Logo"))
            return False

        return True
    # fin __validarCampos

    def __prepararCampos(self):
        nombre = self.inputNombre.text()
        siglas = self.inputSiglas.text()
        self.inputNombre.setText(cPi.PrepararInputs.prepararCadenaCap(nombre))
        self.inputSiglas.setText(cPi.PrepararInputs.prepararCadenaMay(siglas))
    # fin __prepararCampos

    def __obtenerCampos(self):
        return self.inputNombre.text(), self.inputSiglas.text(), \
            self.inputLogo.text()
    # fin __obtenerCampos

    def __buscarLogo(self):
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
# fin if test

# fin introducirPartido.py
