# inicio ventanaBorrarCaso

from ventanas.caso.ventanaEditarCaso import VentanaEditarCaso
from PyQt5 import QtWidgets
from ventanas.prepararInputs import PrepararInputs
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaBorrarCaso(VentanaEditarCaso):
    '''
    Ventana para Borrar un Caso.
    '''

    def __init__(self, identificador: int):
        super(VentanaBorrarCaso, self).__init__(identificador)
        self.setWindowTitle("Borrar un Caso")
        self.botonAceptar.setText("Borrar")
        self.botonResetear.setEnabled(False)
        self.inputCredencial.setReadOnly(True)        
    # fin __init__

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto.
        '''
        consulta = f"DELETE FROM casos \
            WHERE id_caso = {self.identificador}"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta
# fin VentanaBorrarCaso


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        id = 1
        ui = VentanaBorrarCaso(id)
        ui.show()
        app.exec_()
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
    except BaseException:
        ErrorCampoModal.errorConexion()
# fin if test

# fin ventanaBorrarCaso
