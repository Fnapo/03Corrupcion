# inicio ventanaVerImputadoCasos

from ventanas.imputado.ventanaInsertarImputadoCasos import VentanaInsertarImputadoCasos
from PyQt5 import QtWidgets
from ventanas.clases.conectarMysql import ConectarMysql
from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.imputado.seleccionarImputados import SeleccionarImputados
from ventanas.prepararInputs import PrepararInputs
from ventanas.imputado.ventanaListarImputados import VentanaListarImputados


class VentanaVerImputadoCasos(VentanaInsertarImputadoCasos):
    '''
    Relaciona unos Casos con un Imputado dado.
    '''

    def __init__(self, identificador: int):
        try:
            super(VentanaVerImputadoCasos, self).__init__(identificador)
        except ConnectionError:
            raise ConnectionError
        except ValueError:
            raise ValueError
        else:
            self.setWindowTitle("Mirar relación Imputado Casos")
            self.botonAceptar.setText("Aceptar")
            self.botonCancelar.setEnabled(False)
            self.botonResetear.setEnabled(False)
        # fin try
    # fin __init__

    def _realizarAccion(self):
        '''
        Realiza la acción CRUD pertinente.
        '''
        self.close()
    # fin _realizarAccion

    def _cambiarLabels(self, campoCadena: str):
        '''
        Cambia el texto de las primeras labels de la Ventana.
        '''
        super(VentanaVerImputadoCasos, self)._cambiarLabels(campoCadena)
        texto = self.labelSeleciona.text()
        texto = texto.replace("Selecciona", "Mira")
        self.labelSeleciona.setText(texto)
    # fin _cambiarLabels

    def _inicializarCheckBox(self) -> bool:
        return True
    # fin _inicializarCheckBox

    def _crearCheckBox(self, fila: int) -> QtWidgets.QWidget:
        '''
        Crea una CheckBox en una celda de una TableWidget.
        '''
        nuevoWidget = super(VentanaVerImputadoCasos, self)._crearCheckBox(fila)
        hijos = nuevoWidget.children()
        hijos[1].setEnabled(False)

        return nuevoWidget
    # fin _crearCheckBox

    def _obtenerRegitros(self):
        '''
        Obtiene los Casos relacionados con el Imputado.
        '''
        cursor = VentanaVerImputadoCasos._conexion.cursor()
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
# fin VentanaVerImputadoCasos


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        id = 1
        ventana = VentanaVerImputadoCasos(id)
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
    except IndexError:
        ErrorCampoModal.errorSinRegistros("Casos adecuados")
# fin if test

# fin ventanaVerImputadoCasos
