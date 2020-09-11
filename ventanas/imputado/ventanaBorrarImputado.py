# inicio ventanaBorrarImputado

from ventanas.imputado.ventanaEditarImputado import VentanaEditarImputado
from PyQt5 import QtWidgets
from ventanas.prepararInputs import PrepararInputs
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaBorrarImputado(VentanaEditarImputado):
    '''
    Ventana para Borrar un Imputado
    '''

    def __init__(self, identificador: int):
        super(VentanaBorrarImputado, self).__init__(identificador)
        self.setWindowTitle("Borrar un Imputado")
        self.botonAceptar.setText("Borrar")
        self.botonResetear.setEnabled(False)
        self.inputNombre.setEnabled(False)
        self.inputApellidos.setEnabled(False)
        self.inputPartido.setEnabled(False)
        self.inputCargo.setEnabled(False)
        self.inputGrupoRH.setEnabled(False)
        self.inputFecha.setEnabled(False)
    # fin __init__

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto.
        '''
        consulta = f"DELETE FROM imputados \
            WHERE id_imputado = {self.identificador}"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta
# fin VentanaBorrarImputado


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication([])
        id = 1
        ventana = VentanaBorrarImputado(id)
        ventana.show()
        app.exec_()
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
    except ConnectionError:
        ErrorCampoModal.errorConexion()
# fin if test

# fin ventanaBorrarImputado
