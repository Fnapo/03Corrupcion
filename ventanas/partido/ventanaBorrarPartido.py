# inicio ventanaBorrarPartido

from ventanas.partido.ventanaEditarPartido import VentanaEditarPartido
from PyQt5 import QtWidgets
from ventanas.prepararInputs import PrepararInputs
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaBorrarPartido(VentanaEditarPartido):
    '''
    Ventana para Borrar un Partido.
    '''

    def __init__(self, identificador: int):
        try:
            super(VentanaBorrarPartido, self).__init__(identificador)
            self._revisar = False            
        except ConnectionError:
            raise ConnectionError
        except ValueError:
            raise ValueError
        else:
            self.setWindowTitle("Borrar un Partido")
            self.botonAceptar.setText("Borrar")
            self.botonResetear.setEnabled(False)
            self.inputNombre.setReadOnly(True)
            self.inputSiglas.setReadOnly(True)
            self.inputLogo.setReadOnly(True)
            self.botonLogo.setEnabled(False)
        # fin try
    # fin __init__

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto.
        '''
        consulta = f"DELETE FROM partidos \
            WHERE id_partido = {self.identificador}"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta
# fin VentanaBorrarPartido


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        id = 1
        ui = VentanaBorrarPartido(id)
        ui.show()
        app.exec_()
    except Exception:
        ErrorCampoModal.errorNoRegistro(id)
    except BaseException:
        ErrorCampoModal.errorConexion()
# fin if test

# fin ventanaBorrarPartido
