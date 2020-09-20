# inicio ventanaEditarPartido

from ventanas.partido.ventanaInsertarPartido import VentanaInsertarPartido
from PyQt5 import QtGui, QtWidgets
from ventanas.prepararInputs import PrepararInputs
from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.clases.conectarMysql import ConectarMysql
from ventanas.partido.seleccionarPartidos import SeleccionarPartidos


class VentanaEditarPartido(VentanaInsertarPartido):
    '''
    Ventana para editar un Partido
    '''

    def __init__(self, identificador: int):
        try:
            super(VentanaEditarPartido, self).__init__()
        except ConnectionError:
            raise ConnectionError
        else:
            self.identificador = identificador
            self.setWindowTitle("Editar un Partido")
            self.botonAceptar.setText("Editar Partido")
            self._conexion.reconnect()
            lista = SeleccionarPartidos.obtenerPartido(self._conexion, self.identificador)
            self._conexion.close()        
            if len(lista) == 0:
                raise ValueError
            else:
                self._resetear()
        # fin try
    # fin __init__

    def _resetear(self):
        self._conexion.reconnect()
        lista = SeleccionarPartidos.obtenerPartido(self._conexion, self.identificador)
        self._conexion.close()
        self.inputNombre.setText(lista[0][1])
        self.inputSiglas.setText(lista[0][2])
        self.inputLogo.setText(lista[0][3])
        miQpixmax = QtGui.QPixmap(lista[0][3])
        self.labelLogo.setPixmap(miQpixmax.scaled(100, 100))
    # fin _resetear

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto
        '''
        nombre, siglas, logo = self._obtenerCampos()
        consulta = f"UPDATE partidos \
            SET nombre = '{nombre}', siglas = '{siglas}', logo = '{logo}' \
            WHERE id_partido = {self.identificador}"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta
# fin VentanaEditarPartido


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication([])
        id = 1
        ui = VentanaEditarPartido(id)
        ui.show()
        app.exec_()
        try:
            id = 1
            conexion = ConectarMysql.conectar()
            lista = SeleccionarPartidos.obtenerPartido(conexion, id)
            if len(lista) == 0:
                raise ValueError
            conexion.close()
            print(lista)
            print(lista[0][1])         
        except ConnectionError:
            ErrorCampoModal.errorConexion()
        except ValueError:
            ErrorCampoModal.errorNoRegistro(id)
    except ConnectionError:
        ErrorCampoModal.errorConexion()
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
# fin if test

# fin ventanaEditarPartido
