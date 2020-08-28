# inicio ventanaEditarCargo

from cargo.ventanaInsertarCargo import VentanaInsertarCargo
from PyQt5 import QtCore, QtGui, QtWidgets
from errorCampoModal import ErrorCampoModal
from prepararInputs import PrepararInputs
import mysql.connector as conMysql


class VentanaEditarCargo(VentanaInsertarCargo):
    '''
    Ventana para editar un Cargo
    '''

    def __init__(self, identificador: int):
        try:
            VentanaInsertarCargo.__init__(self)
            self.identificador = identificador
            self.setWindowTitle("Editar un Cargo")
            self.botonAceptar.setText("Editar Cargo")
            lista = self.obtenerCargo(self.identificador)
            if len(lista) == 0:
                self.errorNoRegistro(self.identificador)
                raise Exception
            else:
                self._resetear()
        except:
            raise Exception
    # fin __init__

    def _resetear(self):
        lista = self.obtenerCargo(self.identificador)
        self.inputCargo.setText(lista[0][0])

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

    @staticmethod
    def obtenerCargo(identificador: int):
        try:
            conexion = conMysql.connect(**VentanaInsertarCargo._configuracion)
            cursor = conexion.cursor()
            consulta = f"SELECT cargo \
                FROM cargos \
                WHERE id_cargo = {identificador}"
            cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
            lista = cursor.fetchall()
            cursor.close()
            conexion.close()

            return lista
        except:
            raise Exception
        # fin try conectar
    # fin obtenerPartido

    @staticmethod
    def obtenerTodosCargos():
        try:
            conexion = conMysql.connect(**VentanaInsertarCargo._configuracion)
            cursor = conexion.cursor()
            consulta = f"SELECT cargo \
                FROM cargos"
            cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
            lista = cursor.fetchall()
            cursor.close()
            conexion.close()

            return lista
        except:
            raise Exception
        # fin try conectar
    # fin obtenerTodosPartidos
# fin VentanaEditarCargo


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication([])
        ui = VentanaEditarCargo(1)
        ui.show()
        app.exec_()
        try:
            lista = VentanaEditarCargo.obtenerCargo(1)
            print(lista)
            print(lista[0][0])
        except:
            ventanaError = ErrorCampoModal("Error en una Lista")
            ventanaError.mostrar("La Lista está vacía")
    except:
        pass
# fin if test
# fin ventanaEditarCargo
