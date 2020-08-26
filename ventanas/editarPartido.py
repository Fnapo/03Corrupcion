# inicio editarPartido

from introducirPartido import VentanaIntroducirPartido as VIP
from PyQt5 import QtCore, QtGui, QtWidgets
from prepararInputs import PrepararInputs as cPi
from errorCampoModal import ErrorCampoModal as cEcm
import mysql.connector as conMysql


class VentanaEditarPartido(VIP):
    '''
    Ventana para editar un Partido
    '''

    def __init__(self, identificador: int):
        try:
            VIP.__init__(self)
            self.identificador = identificador
            self.setWindowTitle("Editar un partido")
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

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto
        '''
        nombre, siglas, logo = self._obtenerCampos()
        consulta = f"UPDATE partidos \
            SET nombre = '{nombre}', siglas = '{siglas}', logo = '{logo}' \
            WHERE id_partido = {self.identificador}"

        return cPi.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta

    @staticmethod
    def errorNoRegistro(id: int):
        errorCecm = cEcm("Error de registro")
        errorCecm.mostrar(f"El registro con 'id' = {id} no existe")
    # fin errorNoRegistro

    @staticmethod
    def obtenerPartido(identificador: int):
        try:
            conexion = conMysql.connect(**VIP._configuracion)
            cursor = conexion.cursor()
            consulta = f"SELECT nombre, siglas, logo \
                FROM partidos \
                WHERE id_partido = {identificador}"
            cursor.execute(cPi.quitarEspaciosCentrales(consulta))
            lista = cursor.fetchall()
            cursor.close()
            conexion.close()

            return lista
        except:
            raise Exception
        # fin try conectar
    # fin obtenerPartido

# fin VentanaEditarPartido


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = VentanaEditarPartido(1)
        ui.show()
        app.exec_()
        try:
            lista = VentanaEditarPartido.obtenerPartido(2)
            print(lista)
            print(lista[0][0])
        except:
            errorCecm = cEcm("Error en una Lista")
            errorCecm.mostrar("La Lista está vacía")
    except:
        pass
# fin if test
# fin editarPartido
