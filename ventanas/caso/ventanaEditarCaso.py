# inicio ventanaEditarCaso

from ventanas.caso.ventanaInsertarCaso import VentanaInsertarCaso
from PyQt5 import QtWidgets
from ventanas.caso.seleccionarCasos import SeleccionarCasos
from ventanas.prepararInputs import PrepararInputs
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaEditarCaso(VentanaInsertarCaso):
    '''
    Ventana para editar un Caso
    '''

    def __init__(self, identificador: int):
        super(VentanaEditarCaso, self).__init__()
        self.identificador = identificador
        self.setWindowTitle("Editar un Caso")
        self.botonAceptar.setText("Editar Caso")
        self._conexion.reconnect()
        lista = SeleccionarCasos.obtenerCaso(
            self._conexion, self.identificador)
        self._conexion.close()
        if len(lista) == 0:
            raise ValueError
        else:
            self._resetear()
    # fin __init__

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto
        '''
        credencial, montante = self._obtenerCampos()
        valor = PrepararInputs.pasarMonedaFloat(montante)
        consulta = f"UPDATE casos \
            SET credencial = '{credencial}', montante = {valor} \
            WHERE id_caso = {self.identificador}"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta

    def _resetear(self):
        self._conexion.reconnect()
        lista = SeleccionarCasos.obtenerCaso(
            self._conexion, self.identificador)
        self._conexion.close()
        self.inputCredencial.setText(lista[0][0])
        self.inputMontante.setText(PrepararInputs.pasarFloatMoneda(lista[0][1], False))
    # fin _resetear
# fin VentanaEditarCaso


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication([])
        id = 1
        ui = VentanaEditarCaso(id)
        ui.show()
        app.exec_()
        try:
            conexion = VentanaEditarCaso.conectar()
            id = 11
            lista = SeleccionarCasos.obtenerCaso(conexion, id)
            if len(lista) == 0:
                raise ValueError
            conexion.close()
            print(lista)
            print(lista[0][1])
        except IndexError:
            ErrorCampoModal.errorIndiceIncorrecto(type(lista))
        except ValueError:
            ErrorCampoModal.errorNoRegistro(id)
    except ConnectionError:
        ErrorCampoModal.errorConexion()            
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
# fin if test

# fin ventanaEditarCaso
