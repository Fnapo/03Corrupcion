# inicio editarPartido

from partido.insertarPartido import VentanaInsertarPartido
from PyQt5 import QtGui, QtWidgets
from prepararInputs import PrepararInputs
from errorCampoModal import ErrorCampoModal
import mysql.connector as conMysql


class VentanaEditarPartido(VentanaInsertarPartido):
    '''
    Ventana para editar un Partido
    '''

    def __init__(self, identificador: int):
        try:
            VentanaInsertarPartido.__init__(self)
            self.identificador = identificador
            self.setWindowTitle("Editar un Partido")
            self.botonAdd.setText("Editar Partido")
            lista = self.obtenerPartido(self.identificador)
            if len(lista) == 0:
                self.errorNoRegistro(self.identificador)
                raise Exception
            else:
                self._resetear()
        except:
            raise Exception
    # fin __init__

    def _resetear(self):
        lista = self.obtenerPartido(self.identificador)
        self.inputNombre.setText(lista[0][0])
        self.inputSiglas.setText(lista[0][1])
        self.inputLogo.setText(lista[0][2])
        miQpixmax = QtGui.QPixmap(lista[0][2])
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

    @staticmethod
    def obtenerPartido(identificador: int):
        try:
            conexion = conMysql.connect(
                **VentanaInsertarPartido._configuracion)
            cursor = conexion.cursor()
            consulta = f"SELECT nombre, siglas, logo \
                FROM partidos \
                WHERE id_partido = {identificador}"
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
    def obtenerTodosPartidos():
        try:
            conexion = conMysql.connect(
                **VentanaInsertarPartido._configuracion)
            cursor = conexion.cursor()
            consulta = "SELECT id_partido, nombre, siglas, logo \
                FROM partidos"
            cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
            lista = cursor.fetchall()
            cursor.close()
            conexion.close()

            return lista
        except:
            raise Exception
        # fin try conectar
    # fin obtenerTodosPartidos
# fin VentanaEditarPartido


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication([])
        ui = VentanaEditarPartido(1)
        ui.show()
        app.exec_()
        try:
            lista = VentanaEditarPartido.obtenerPartido(2)
            print(lista)
            print(lista[0][0])
        except:
            ventanaError = ErrorCampoModal("Error en una Lista")
            ventanaError.mostrar("La Lista está vacía")
    except:
        pass
# fin if test

# fin editarPartido
