# inicio ventanaInsertarCasoImputados

from ventanas.ventanaInsertarCampoResgistros import VentanaInsertarCampoRegistros
from PyQt5 import QtWidgets
from ventanas.clases.conectarMysql import ConectarMysql
from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.caso.seleccionarCasos import SeleccionarCasos
from ventanas.prepararInputs import PrepararInputs
from ventanas.imputado.ventanaListarImputados import VentanaListarImputados
from ventanas.caso.ventanaListarCasos import VentanaListarCasos


class VentanaInsertarCasoImputados(VentanaInsertarCampoRegistros):
    '''
    Relaciona unos Imputadps con un Caso dado.
    '''

    def __init__(self, identificador: int):
        super(VentanaInsertarCasoImputados, self).__init__(identificador)
        self.setWindowTitle("Insertar relación Caso Impurtados")
    # fin __init__

    def _crearConsulta(self, fila: int) -> str:
        '''
        Crea la consulta SQL correspondiente.
        '''
        fkimputado = self._registros[fila][0]
        consulta = f"INSERT INTO acusacion \
            (fk_caso, fk_imputado) \
            VALUES ({self._identificador}, {fkimputado})"

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
        texto = texto.replace("Registros", "Imputados")
        self.labelSeleciona.setText(texto)
        texto = self.labelCampo.setText(campoCadena)
    # fin _cambiarLabels

    def _tratarRegistro(self, fila: int) -> str:
        '''
        Trata el Imputado dado.
        '''
        cadena, numero = VentanaListarImputados.prepararImputado(self._registros[fila])

        return cadena.strip()        
    # fin _tratarRegistro

    def _inicializarCheckBox(self) -> bool:
        return False
    # fin _inicializarCheckBox

    def _cadenaCheckBox(self) -> str:
        return "Relacionado"
    # fin _cadenaCheckBox

    def _obtenerRegitros(self):
        '''
        Obtiene los Imputados no relacionados con el Caso.
        '''
        cursor = VentanaInsertarCasoImputados._conexion.cursor()
        consulta = f"SELECT * \
            FROM imputados \
            WHERE id_imputado NOT IN \
            (SELECT fk_imputado \
            FROM acusacion \
            WHERE fk_caso = {self._identificador}) \
            ORDER BY apellidos"            
        cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
        self._registros = cursor.fetchall()
        cursor.close()
    # fin _obtenerRegitros

    def _prepararCampo(self, campo: list) -> str:
        '''
        Prepara el Caso como una cadena.
        '''
        return campo[0][1].strip()
    # fin _prepararCampo

    def _obtenerCampo(self) -> list:
        '''
        Obtiene el Caso dado.
        '''
        caso = SeleccionarCasos.obtenerCaso(VentanaInsertarCasoImputados._conexion, self._identificador)

        return caso
    # fin _obtenerCampo
# fin VentanaInsertarCasoImputados


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        id = 1
        ventana = VentanaInsertarCasoImputados(id)
        ventana.show()
        app.exec_()
        try:
            conexion = ConectarMysql.conectar()
            id = 11
            lista = SeleccionarCasos.obtenerCaso(conexion, id)
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
        ErrorCampoModal.errorSinRegistros("Imputados adecuados")
# fin if test

# fin ventanaInsertarCasoImputados
