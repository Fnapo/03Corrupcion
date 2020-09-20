# inicio ventanaInsertarPartido

from PyQt5 import QtWidgets, QtGui
from ventanas.prepararInputs import PrepararInputs
from ventanas.ventanaAccionMysql import VentanaAccionMysql
from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.partido.insertarPartido import Ui_introducirPartido


class VentanaInsertarPartido(VentanaAccionMysql, Ui_introducirPartido):
    '''
    Ventana para insertar un Partido
    '''

    def __init__(self):
        try:
            super(VentanaInsertarPartido, self).__init__()
        except ConnectionError:
            raise ConnectionError
        else:
            self.setupUi(self)
            self.botonLogo.clicked.connect(self._buscarLogo)
            self.botonAceptar.clicked.connect(self._accion)
            self.botonCancelar.clicked.connect(self.close)
            self.botonResetear.clicked.connect(self._resetear)
        # fin try
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
        if len(nombre) == 0:
            ErrorCampoModal.errorCampoVacio("Nombre")
            return False
        elif len(siglas) == 0:
            ErrorCampoModal.errorCampoVacio("Siglas")
            return False
        elif len(logo) == 0:
            ErrorCampoModal.errorCampoVacio("Logo")
            return False
        else:
            return True
        # fin if len
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
# fin VentanaIntroducirPartido


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = VentanaInsertarPartido()
        ui.show()
        app.exec_()
    except:
        ErrorCampoModal.errorConexion()
# fin if test

# fin ventanaInsertarPartido
