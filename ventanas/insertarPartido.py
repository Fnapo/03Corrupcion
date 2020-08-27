# inicio insertarPartido

from PyQt5 import QtCore, QtGui, QtWidgets
from prepararInputs import PrepararInputs
from clases.conectarMysql import ConectarMysql
from errorCampoModal import ErrorCampoModal
from introducirPartido_ui import Ui_introducirPartido


class VentanaInsertarPartido(QtWidgets.QDialog, Ui_introducirPartido, ConectarMysql):
    '''
    Ventana para insertar un Partido
    '''

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        try:
            ConectarMysql.__init__(self)
        except:
            raise Exception
        else:
            self.setupUi(self)
            self.botonLogo.clicked.connect(self._buscarLogo)
            self.botonAdd.clicked.connect(self._accion)
            self.botonRes.clicked.connect(self._resetear)
    # fin __init__

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto
        '''
        nombre, siglas, logo = self._obtenerCampos()
        consulta = f"INSERT INTO partidos \
            (nombre, siglas, logo) \
            VALUES ('{nombre}', '{siglas}', '{logo}')"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta

    def _validarCampos(self) -> bool:
        '''
        Devuelve True si los campos son válidos
        '''
        nombre, siglas, logo = self._obtenerCampos()
        mensaje = "Campo vacío: '{}'"
        errorCM = ErrorCampoModal()
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
        self.inputNombre.setText(PrepararInputs.prepararCadenaCap(nombre))
        self.inputSiglas.setText(PrepararInputs.prepararCadenaMay(siglas))
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
        ui = VentanaInsertarPartido()
    except:
        pass
    else:
        ui.show()
        sys.exit(app.exec_())
# fin if test

# fin insertarPartido
