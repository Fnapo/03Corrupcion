# inicio errorCampoModal.py

from PyQt5 import QtWidgets
from ventanas.errorCampo_ui import Ui_errorCampo
from ventanas.prepararInputs import PrepararInputs


class ErrorCampoModal(QtWidgets.QDialog, Ui_errorCampo):
    '''
    Clase para crear ventanas modales para visualizar mensajes de error.
    También crea algunos ejemplos de ellas con mensajes.
    '''

    def __init__(self, titulo="Error en un Campo"):
        '''
        Crea una ventana modal con un título dado
        '''
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.botonAceptar.clicked.connect(self.close)
        self.setWindowTitle(titulo)
    # fin __init__

    def mostrar(self, mensaje: str):
        self.label01.setText(mensaje)
        self.exec()
    # fin mostrar

    @staticmethod
    def errorDesconocido(mensajeError: str):
        errorCM = ErrorCampoModal()
        errorCM.mostrar(mensajeError)
    # fin errorDesconocido

    @staticmethod
    def campoReferenciado(mensajeError: str):
        '''
        El campo está referenciado.
        '''
        errorCM = ErrorCampoModal("Error en el borrado")
        tabla = PrepararInputs.separarTablaReferenciada(mensajeError)
        cadena = f"No se puede borrar el registro\
            \nPor estar Referenciado en la tabla {tabla}"
        errorCM.mostrar(PrepararInputs.quitarEspaciosCentrales(cadena))
    # fin campoReferenciado

    @staticmethod
    def errorFaltaCampo(campo: str):
        '''
        Error tipo Campo sin seleccionar
        '''
        vacia = ErrorCampoModal(f"Falta seleccionar {campo}")
        vacia.mostrar(f"Debes seleccionar ...\n{campo}")
    # fin errorFaltaCampo

    @staticmethod
    def errorSinRegistros(campos: str):
        '''
        Error tipo tabla sin registros
        '''
        vacia = ErrorCampoModal(f"Sin {campos}")
        vacia.mostrar(f"Tabla sin {campos}")
    # fin errorSinRegistros

    @staticmethod
    def errorIndiceIncorrecto(tipo: str):
        '''
        Error en el índice de una tuple, o list, etc...
        '''
        errorCM = ErrorCampoModal("Error en un índice")
        errorCM.mostrar(f"Error en un índice\n de la {tipo}")
    # fin indiceIncorrecto

    @staticmethod
    def errorFueraRango(campo: str, minimo: str, maximo: str):
        '''
        Error del tipo valor no está entre dos valores
        '''
        errorCM = ErrorCampoModal()
        errorCM.mostrar(f"El {campo} debe estar entre\n{minimo} y\n{maximo}")
    # fin

    @staticmethod
    def errorDuplicado(mensajeError: str):
        '''
        Error que muestra la ya existencia de un valor en un campo
        '''
        errorCM = ErrorCampoModal()
        valor, campo = PrepararInputs.separarValorCampo(
            mensajeError)
        errorCM.mostrar(f"Error: el valor {valor} ya está usado en el campo {campo}")
    # fin errorDuplicado

    @staticmethod
    def errorCampoCorto(campo: str, minimo: int):
        '''
        Error del tipo campo corto
        '''
        errorCM = ErrorCampoModal()
        errorCM.mostrar(
            f"Campo vacío o muy corto: '{campo}'\nMínimo {minimo} Caracteres")
    # fin campoCorto

    @staticmethod
    def errorCampoVacio(campo: str):
        '''
        Error del tipo campo vacío
        '''
        errorCM = ErrorCampoModal()
        errorCM.mostrar(f"Campo vacío: '{campo}'")
    # fin campoVacio

    @staticmethod
    def errorNoRegistro(id: int):
        '''
        Mensaje que muestra la no existencia de un registro
        '''
        ventanaError = ErrorCampoModal("Error de registro")
        ventanaError.mostrar(f"El registro con 'id' = {id}\nNo existe.")
    # fin errorNoRegistro

    @staticmethod
    def correcto():
        errorCM = ErrorCampoModal("Éxito en la operación")
        errorCM.mostrar("Operación correcta ...")
    # fin correcto

    @staticmethod
    def errorConexion():
        '''
        Mensaje de algún error en la conexión a la BBDD
        '''
        errorCM = ErrorCampoModal("Error en la conexión")
        errorCM.mostrar(
            "Error en la conexión.\nRevisa los parámetros de la misma.")
    # fin errorConexion
# fin class ErrorCampoModal


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    ventana = ErrorCampoModal("Hola")
    ventana.mostrar("Prueba")
    ventana.show()
    app.exec_()
# fin if test

# fin errorCampoModal.py
