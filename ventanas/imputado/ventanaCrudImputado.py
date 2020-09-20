# inicio ventanaCrudImputado

from PyQt5 import QtWidgets
from ventanas.ventanaCrudRegistros import VentanaCrudRegistros
from ventanas.imputado.ventanaListarImputados import VentanaListarImputados


class VentanaCrudImputado(VentanaCrudRegistros):
    '''
    Ventana para realizar una acción CRUD relacionada con un Imputado.
    '''

    def __init__(self):
        try:
            super(VentanaCrudImputado, self).__init__()
        except:
            raise ConnectionError
        else:
            self.crearRegistro.setText("Insertar un Imputado")
            self.editarRegistro.setText("Editar un Imputado")
            self.verRegistro.setText("Ver un Imputado")
            self.borrarRegistro.setText("Borrar un Imputado")
        # fin try
    # fin __init__

    def _borrar(self):
        '''
        Función para borrar un Imputado.
        '''
        ventana = VentanaListarImputados()
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        print(identificador)
        self.close()
    # fin _borrar

    def _ver(self):
        '''
        Función para ver un Imputado.
        '''
        ventana = VentanaListarImputados()
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        print(identificador)
        self.close()
    # fin _ver

    def _editar(self):
        '''
        Función para editar un Imputado.
        '''
        ventana = VentanaListarImputados()
        cadena = ventana.label.text()
        cadena = cadena.replace("...", "para editarlo")
        ventana.label.setText(cadena)
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        print(identificador)
        self.close()
    # fin _editar

    def _crear(self):
        '''
        Función para crear un Imputado.
        '''
        ventana = VentanaListarImputados()
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        print(identificador)
        self.close()
    # fin _crear
# fin VentanaCrudImputado


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ventana = VentanaCrudImputado()
    except:
        sys.exit("Error en el programa ...")
    else:
        ventana.exec_()
        print("Correcto ...")
    # fin try
# fin if test

# fin ventanaCrudImputado
