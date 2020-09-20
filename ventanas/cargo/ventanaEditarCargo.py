# inicio ventanaEditarCargo

from ventanas.cargo.ventanaInsertarCargo import VentanaInsertarCargo
from PyQt5 import QtWidgets
from ventanas.prepararInputs import PrepararInputs
from ventanas.cargo.seleccionarCargos import SeleccionarCargos
from ventanas.clases.conectarMysql import ConectarMysql
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaEditarCargo(VentanaInsertarCargo):
    '''
    Ventana para editar un Cargo
    '''

    def __init__(self, identificador: int):
        try:
            super(VentanaEditarCargo, self).__init__()
        except ConnectionError:
            raise ConnectionError
        else:
            self.identificador = identificador
            self.setWindowTitle("Editar un Cargo")
            self.botonAceptar.setText("Editar Cargo")
            self._conexion.reconnect()
            lista = SeleccionarCargos.obtenerCargo(
                self._conexion, self.identificador)
            self._conexion.close()
            if len(lista) == 0:
                raise ValueError
            else:
                self._resetear()
        # fin try
    # fin __init__

    def _resetear(self):
        self._conexion.reconnect()
        lista = SeleccionarCargos.obtenerCargo(
            self._conexion, self.identificador)
        self._conexion.close()
        self.inputCargo.setText(lista[0][1])
    # fin _resetear

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto
        '''
        cargo = self._obtenerCampos()
        consulta = f"UPDATE cargos \
            SET cargo = '{cargo}' \
            WHERE id_cargo = {self.identificador}"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta
# fin VentanaEditarCargo


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication([])
        id = 1
        ventana = VentanaEditarCargo(id)
        ventana.show()
        app.exec_()
        try:
            conexion = ConectarMysql.conectar()
            id = 11
            lista = SeleccionarCargos.obtenerCargo(conexion, id)
            conexion.close()
            if len(lista) == 0:
                raise ValueError
            print(lista)
            print(lista[0][0])
        except ValueError:
            ErrorCampoModal.errorNoRegistro(id)
        except ConnectionError:
            ErrorCampoModal.errorConexion()
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
    except ConnectionError:
        ErrorCampoModal.errorConexion()
# fin if test

# fin ventanaEditarCargo
