# inicio ventanaEntradaUsuario

from ventanas.ventanaConexionMysql import VentanaConexionMysql
from ventanas.ventanaEntrada import Ui_VentanaEntrada
from PyQt5 import QtWidgets
from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.prepararInputs import PrepararInputs


class VentanaEntradaUsuario(VentanaConexionMysql, Ui_VentanaEntrada):
    '''
    Clase para permitir la entrada a un usuario.
    '''

    def __init__(self):
        try:
            super(VentanaEntradaUsuario, self).__init__()
        except ConnectionError:
            raise ConnectionError
        else:
            self.setupUi(self)
            self._correcto = False
            self.botonAceptar.clicked.connect(self._aceptar)
        # fin try
    # fin __init__

    def resetear(self):
        '''
        Resetea los campos.
        '''
        self.inputUsuario.setText("")
        self.inputPassword.setText("")
    # fin resetear

    def verCorrecto(self) -> bool:
        return self._correcto
    # fin verCorrecto

    def _crearConsulta(self, usuario: str, password: str) -> str:
        '''
        Consulta para comprobar la existencia del usuario
        '''
        consulta = f"SELECT * \
            FROM usuarios \
            WHERE usuario = '{usuario}' AND password = '{password}'"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta

    def _existeUsuario(self, usuario: str, password: str) -> bool:
        '''
        Comprueba si son correctos los datos.
        '''
        self._conexion.reconnect()
        consulta = self._crearConsulta(usuario, password)
        cursor = self._conexion.cursor()
        cursor.execute(consulta)
        lista = cursor.fetchall()
        cursor.close()
        self._conexion.close()

        return len(lista) > 0
    # fin _existeUsuario

    def _validarCampos(self, usuario: str, password: str) -> bool:
        '''
        Comprueba la validez de los campos.
        '''
        if len(usuario) == 0:
            ErrorCampoModal.errorCampoVacio("Usuario")
            return False
        elif len(password) == 0:
            ErrorCampoModal.errorCampoVacio("Password")
            return False
        else:
            return True
        # fin if
    # fin _validarCampos

    def _obtenerCampos(self) -> tuple:
        '''
        Obtiene los valores de los campos
        '''
        return self.inputUsuario.text(), self.inputPassword.text()
    # fin _obtenerCampos

    def _aceptar(self):
        '''
        Confirma la veracidad de los datos del Usuario
        '''
        usuario, password = self._obtenerCampos()
        correcto = self._validarCampos(usuario, password)
        if correcto:
            self._correcto = self._existeUsuario(usuario, password)
            self.close()
        # fin if
    # fin _aceptar
# fin VentanaEntradaUsuario


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ventana = VentanaEntradaUsuario()
        ventana.show()
        app.exec_()
        salida = ventana.verCorrecto()
        print(salida)
    except ConnectionError:
        ErrorCampoModal.errorConexion()
    # fin try
# fin if test

# fin ventanaEntradaUsuario
