# inicio ventanaBorrarImputadoCasos

from ventanas.imputado.ventanaInsertarImputadoCasos import VentanaInsertarImputadoCasos
from ventanas.prepararInputs import PrepararInputs
from PyQt5 import QtWidgets
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaBorrarImputadoCasos(VentanaInsertarImputadoCasos):
    '''
    Des-relaciona unos Casos con un Imputado dado.
    '''

    def __init__(self, identificador: int):
        try:
            super(VentanaBorrarImputadoCasos, self).__init__(identificador)
        except ConnectionError:
            raise ConnectionError
        except ValueError:
            raise ValueError
        else:
            self.botonAceptar.setText("Borrar Relación")
            self.setWindowTitle("Borrar relación Imputado Casos")
    # fin __init__

    def _crearConsulta(self, fila: int) -> str:
        '''
        Crea la consulta SQL correspondiente.
        '''
        fkcaso = self._registros[fila][0]
        consulta = f"DELETE FROM  acusacion \
            WHERE fk_caso = {fkcaso} AND fk_imputado = {self._identificador}"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta

    def _esCorrecto(self, checkeo: bool) -> bool:
        '''
        ¿Con qué se actúa .. con True o False?
        '''
        return checkeo
    # fin _esCorrecto

    def _cambiarLabels(self, campoCadena: str):
        '''
        Cambia el texto de las primeras labels de la Ventana.
        '''
        texto = self.labelSeleciona.text()
        texto = texto.replace("Registros", "Casos NO")      
        self.labelSeleciona.setText(texto)
        texto = self.labelCampo.setText(campoCadena)
    # fin _cambiarLabels

    def _inicializarCheckBox(self) -> bool:
        return False
    # fin _inicializarCheckBox

    def _cadenaCheckBox(self) -> str:
        return "No Relacionado"
    # fin _cadenaCheckBox

    def _obtenerRegitros(self):
        '''
        Obtiene los Casos relacionados con el Imputado.
        '''
        cursor = VentanaInsertarImputadoCasos._conexion.cursor()
        consulta = f"SELECT * \
            FROM casos \
            WHERE id_caso IN \
            (SELECT fk_caso \
            FROM acusacion \
            WHERE fk_imputado = {self._identificador}) \
            ORDER BY credencial"
        cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
        self._registros = cursor.fetchall()
        cursor.close()
    # fin _obtenerRegitros
# fin VentanaBorrarImputadoCasos


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        id = 1
        ventana = VentanaBorrarImputadoCasos(id)
        ventana.show()
        app.exec_()
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
    except ConnectionError:
        ErrorCampoModal.errorConexion()
    except IndexError:
        ErrorCampoModal.errorSinRegistros("Casos adecuados")
# fin if test

# fin ventanaBorrarImputadoCasos
