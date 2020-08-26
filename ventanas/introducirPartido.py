# inicio introducirPartido.py

import introducirPartido_ui as uiVip
from PyQt5 import QtCore, QtGui, QtWidgets
# from mysql.connector import errorcode
from prepararInputs import PrepararInputs as cPi
from clases.conMysql import ConectarMysql as cConMysql
from errorCampoModal import ErrorCampoModal as cEcm


class VentanaIntroducirPartido(
        QtWidgets.QDialog, uiVip.Ui_introducirPartido, cConMysql):
    '''
    Ventana para insertar un Partido
    '''

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        try:
            cConMysql.__init__(self)
        except:
            raise Exception
        else:
            self.setupUi(self)
            self.botonLogo.clicked.connect(self._buscarLogo)
            self.botonAdd.clicked.connect(self._accion)
            self.botonRes.clicked.connect(self._resetear)
    # fin __init__

    # def _correcto(self):
    #     cEcm.mostrar("Operación correcta ...")

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto
        '''
        nombre, siglas, logo = self._obtenerCampos()
        consulta = f"INSERT INTO partidos \
            (nombre, siglas, logo) \
            VALUES ('{nombre}', '{siglas}', '{logo}')"

        return cPi.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta

    def _validarCampos(self) -> bool:
        '''
        Devuelve True si los campos son válidos
        '''
        nombre, siglas, logo = self._obtenerCampos()
        mensaje = "Campo vacío: '{}'"
        errorCM = cEcm()
        if len(nombre) == 0:
            errorCM.mostrar(mensaje.format("Nombre"))
            return False
        elif len(siglas) == 0:
            errorCM.mostrar(mensaje.format("Siglas"))
            return False
        elif len(logo) == 0:
            errorCM.mostrar(mensaje.format("Logo"))
            return False

        return True
    # fin _validarCampos

    def _prepararCampos(self):
        '''
        Prepara el formato de los campos Inputs
        '''
        nombre = self.inputNombre.text()
        siglas = self.inputSiglas.text()
        self.inputNombre.setText(cPi.prepararCadenaCap(nombre))
        self.inputSiglas.setText(cPi.prepararCadenaMay(siglas))
    # fin _prepararCampos

    def _obtenerCampos(self):
        return self.inputNombre.text(), self.inputSiglas.text(), \
            self.inputLogo.text()
    # fin _obtenerCampos

    def _resetear(self):
        self.inputNombre.setText("")
        self.inputSiglas.setText("")
        self.inputLogo.setText("")
        miQpixmax = QtGui.QPixmap("")
        self.labelLogo.setPixmap(miQpixmax)
    # fin _resetear

    def _buscarLogo(self):
        fNombre = QtWidgets.QFileDialog.getOpenFileName(
            self, "Buscando un Logo", ".\\imagenes", "Ficheros de imágenes (*.jpg *.gif *.jpeg)")
        if len(fNombre[0]) > 0:
            self.inputLogo.setText(fNombre[0])
            miQpixmax = QtGui.QPixmap(fNombre[0])
            self.labelLogo.setPixmap(miQpixmax.scaled(100, 100))
    # fin _buscarLogo
# fin clase VentanaIntroducirPartido


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = VentanaIntroducirPartido()
    except:
        pass
    else:
        ui.show()
        sys.exit(app.exec_())
# fin if test

# fin introducirPartido.py
