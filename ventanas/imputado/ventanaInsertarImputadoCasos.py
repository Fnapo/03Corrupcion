# inicio ventanaInsertarImputadoCasos

from ventanas.ventanaInsertarCampoResgistros import VentanaInsertarCampoRegistros
from PyQt5 import QtWidgets
from ventanas.clases.conectarMysql import ConectarMysql
from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.imputado.seleccionarImputados import SeleccionarImputados
from ventanas.prepararInputs import PrepararInputs
from ventanas.imputado.ventanaListarImputados import VentanaListarImputados


class VentanaInsertarImputadoCasos(VentanaInsertarCampoRegistros):
    '''
    Relaciona unos Casos con un Imputado dado.
    '''

    def __init__(self, identificador: int):
        super(VentanaInsertarImputadoCasos, self).__init__(identificador)
        self.setWindowTitle("Insertar relación Imputado Casos")
    # fin __init__

    def _crearConsulta(self, fila: int) -> str:
        '''
        Crea la consulta SQL correspondiente.
        '''
        fkcaso = self._registros[fila][0]
        consulta = f"INSERT INTO acusacion \
            (fk_caso, fk_imputado) \
            VALUES ({fkcaso}, {self._identificador})"

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
        texto = texto.replace("Registros", "Casos")
        self.labelSeleciona.setText(texto)
        texto = self.labelCampo.setText(campoCadena)
    # fin _cambiarLabels

    def _tratarRegistro(self, fila: int) -> str:
        '''
        Trata el Caso dado.
        '''
        return self._registros[fila][1]
    # fin _tratarRegistro

    def _inicializarCheckBox(self) -> bool:
        return False
    # fin _inicializarCheckBox

    def _cadenaCheckBox(self) -> str:
        return "Relacionado"
    # fin _cadenaCheckBox

    def _obtenerRegitros(self):
        '''
        Obtiene los Casos no relacionados con el Imputado.
        '''
        cursor = VentanaInsertarImputadoCasos._conexion.cursor()
        consulta = f"SELECT * \
            FROM casos \
            WHERE id_caso NOT IN \
            (SELECT fk_caso \
            FROM acusacion \
            WHERE fk_imputado = {self._identificador}) \
            ORDER BY credencial"            
        cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
        self._registros = cursor.fetchall()
        cursor.close()
    # fin _obtenerRegitros

    def _prepararCampo(self, campo: list) -> str:
        '''
        Prepara el Imputado como una cadena.
        '''
        cadena, numero = VentanaListarImputados.prepararImputado(campo[0])

        return cadena.strip()
    # fin _prepararCampo

    def _obtenerCampo(self) -> list:
        '''
        Obtiene el Imputado dado.
        '''
        imputado = SeleccionarImputados.obtenerImputado(VentanaInsertarImputadoCasos._conexion, self._identificador)

        return imputado
    # fin _obtenerCampo
# fin VentanaInsertarImputadoCasos


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        id = 1
        ventana = VentanaInsertarImputadoCasos(id)
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

# fin ventanaInsertarImputadoCasos
