# inicio ventanaEditarImputado

from ventanas.imputado.ventanaInsertarImputado import VentanaInsertarImputado
from PyQt5 import QtWidgets
from ventanas.prepararInputs import PrepararInputs
from ventanas.imputado.seleccionarImputados import SeleccionarImputados
from ventanas.clases.conectarMysql import ConectarMysql
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaEditarImputado(VentanaInsertarImputado):
    '''
    Ventana para editar un Imputado
    '''

    def __init__(self, identificador: int):
        super(VentanaEditarImputado, self).__init__()
        self.identificador = identificador
        self.setWindowTitle("Editar un Imputado")
        self.botonAceptar.setText("Editar Imputado")
        self._conexion.reconnect()
        lista = SeleccionarImputados.obtenerImputado(
            self._conexion, self.identificador)
        self._conexion.close()
        if len(lista) == 0:
            raise ValueError
        else:
            self._resetear()
    # fin __init__

    def _resetear(self):
        self._conexion.reconnect()
        lista = SeleccionarImputados.obtenerImputado(
            self._conexion, self.identificador)
        self._conexion.close()
        self.inputNombre.setText(lista[0][1])
        self.inputApellidos.setText(lista[0][2])
        self.inputPartido.setCurrentIndex(lista[0][3])
        self.inputCargo.setCurrentIndex(lista[0][4])
        try:
            indiceRH = self._listaRH.index(lista[0][5])
        except ValueError:
            indiceRH = 0
        finally:
            self.inputGrupoRH.setCurrentIndex(indiceRH)
            self.inputFecha.setDate(lista[0][6])
    # fin _resetear

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto
        '''
        nombre, apellidos, id_partido, id_cargo, grupoRH, fecha = \
            self._obtenerCampos()
        consulta = f"UPDATE imputados \
            SET nombre = '{nombre}', apellidos = '{apellidos}', fk_partido = {id_partido}, fk_cargo = {id_cargo}, grupoRH = '{grupoRH}', nacimiento = {fecha} \
            WHERE id_imputado = {self.identificador}"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta
# fin VentanaEditarImputado


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication([])
        id = 1
        ventana = VentanaEditarImputado(id)
        ventana.show()
        app.exec_()
        try:
            conexion = ConectarMysql.conectar()
            id = 11
            lista = SeleccionarImputados.obtenerImputado(conexion, id)
            conexion.close()
            if len(lista) == 0:
                raise ValueError
            print(lista)
            print(lista[0][1])
        except ValueError:
            ErrorCampoModal.errorNoRegistro(id)
        except ConnectionError:
            ErrorCampoModal.errorConexion()
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
    except ConnectionError:
        ErrorCampoModal.errorConexion()
# fin if test

# fin ventanaEditarImputado
