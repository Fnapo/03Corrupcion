# inicio ventanaBorrarCargo

from ventanas.cargo.ventanaEditarCargo import VentanaEditarCargo
from PyQt5 import QtWidgets
from ventanas.prepararInputs import PrepararInputs
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaBorrarCargo(VentanaEditarCargo):
    '''
    Ventana para Borrar un Cargo.
    '''

    def __init__(self, identificador: int):
        super(VentanaBorrarCargo, self).__init__(identificador)
        self.setWindowTitle("Borrar un Cargo")
        self.botonAceptar.setText("Borrar")
        self.botonResetear.setEnabled(False)
        self.inputCargo.setEnabled(False)        
    # fin __init__

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto.
        '''
        consulta = f"DELETE FROM cargos \
            WHERE id_cargo = {self.identificador}"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta
# fin VentanaBorrarCargo


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        id = 1
        ventana = VentanaBorrarCargo(id)
        ventana.show()
        app.exec_()
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
    except ConnectionError:
        ErrorCampoModal.errorConexion()
# fin if test

# fin ventanaBorrarCargo
