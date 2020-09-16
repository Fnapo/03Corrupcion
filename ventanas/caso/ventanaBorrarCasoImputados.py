# inicio ventanaBorrarCasoImputados

from ventanas.caso.ventanaInsertarCasoImputados import VentanaInsertarCasoImputados
from ventanas.prepararInputs import PrepararInputs
from PyQt5 import QtWidgets
from ventanas.errorCampoModal import ErrorCampoModal


class VentanaBorrarCasoImputados(VentanaInsertarCasoImputados):
    '''
    Des-relaciona unos Imputados con un Caso dado.
    '''

    def __init__(self, identificador: int):
        super(VentanaBorrarCasoImputados, self).__init__(identificador)
        self.botonAceptar.setText("Borrar Relación")
        self.setWindowTitle("Borrar relación Caso Imputados")
    # fin __init__

    def _crearConsulta(self, fila: int) -> str:
        '''
        Crea la consulta SQL correspondiente.
        '''
        fkimp = self._registros[fila][0]
        consulta = f"DELETE FROM  acusacion \
            WHERE fk_imputado = {fkimp} AND fk_caso = {self._identificador}"

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
        texto = texto.replace("Registros", "Imputados NO")      
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
        Obtiene los Imputados relacionados con el Caso.
        '''
        cursor = VentanaInsertarCasoImputados._conexion.cursor()
        consulta = f"SELECT * \
            FROM imputados \
            WHERE id_imputado IN \
            (SELECT fk_imputado \
            FROM acusacion \
            WHERE fk_caso= {self._identificador}) \
            ORDER BY apellidos"
        cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
        self._registros = cursor.fetchall()
        cursor.close()
    # fin _obtenerRegitros
# fin VentanaBorrarCasoImputados


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        id = 2
        ventana = VentanaBorrarCasoImputados(id)
        ventana.show()
        app.exec_()
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
    except ConnectionError:
        ErrorCampoModal.errorConexion()
    except IndexError:
        ErrorCampoModal.errorSinRegistros("Imputados adecuados")
# fin if test

# fin ventanaBorrarCasoImputados
