# inicio ventanaEditarCaso

from caso.ventanaInsertarCaso import VentanaInsertarCaso
from PyQt5 import QtWidgets
from clases.conectarMysql import ConectarMysql
from prepararInputs import PrepararInputs
import mysql.connector as conMysql
from errorCampoModal import ErrorCampoModal


class VentanaEditarCaso(VentanaInsertarCaso):
    '''
    Ventana para editar un Caso
    '''

    def __init__(self, identificador: int):
        try:
            super(VentanaEditarCaso, self).__init__()
        except:
            raise Exception
        else:
            self.identificador = identificador
            self.setWindowTitle("Editar un Caso")
            self.botonAceptar.setText("Editar Caso")
            lista = self.obtenerCaso(self.identificador)
            if len(lista) == 0:
                self.errorNoRegistro(self.identificador)
                raise Exception
            else:
                self._resetear()
    # fin __init__

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto
        '''
        credencial, montante = self._obtenerCampos()
        consulta = f"UPDATE casos \
            SET credencial = '{credencial}', montante = '{montante}' \
            WHERE id_caso = {self.identificador}"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta

    def _resetear(self):
        lista = self.obtenerCaso(self.identificador)
        self.inputCredencial.setText(lista[0][0])
        self.inputMontante.setText(lista[0][1])
    # fin _resetear

    @staticmethod
    def obtenerCaso(identificador: int):
        try:
            conexion = conMysql.connect(
                **ConectarMysql._configuracion)
            cursor = conexion.cursor()
            consulta = f"SELECT credencial, montante \
                FROM casos \
                WHERE id_caso = {identificador}"
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
    def obtenerTodosCasos():
        try:
            conexion = conMysql.connect(
                **ConectarMysql._configuracion)
            cursor = conexion.cursor()
            consulta = f"SELECT credencial, montante \
                FROM casos"
            cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
            lista = cursor.fetchall()
            cursor.close()
            conexion.close()

            return lista
        except:
            raise Exception
        # fin try conectar
    # fin obtenerTodosCasos
# fin VentanaEditarCaso


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication([])
        ui = VentanaEditarCaso(1)
        ui.show()
        app.exec_()
        try:
            lista = VentanaEditarCaso.obtenerCaso(2)
            print(lista)
            print(lista[0][0])
        except:
            ventanaError = ErrorCampoModal("Error en una Lista")
            ventanaError.mostrar("La Lista está vacía")
    except:
        pass
# fin if test

# fin ventanaEditarCaso
