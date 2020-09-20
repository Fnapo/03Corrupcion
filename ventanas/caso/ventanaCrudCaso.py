# inicio ventanaCrudCaso

from PyQt5 import QtWidgets
from ventanas.ventanaCrudRegistros import VentanaCrudRegistros
from ventanas.caso.seleccionarCasos import SeleccionarCasos
from ventanas.caso.ventanaListarCasos import VentanaListarCasos


class VentanaCrudCaso(VentanaCrudRegistros):
    '''
    Ventana para realizar una acción CRUD relacionada con un Caso.
    '''

    def __init__(self):
        try:
            super(VentanaCrudCaso, self).__init__()
        except ConnectionError:
            raise ConnectionError
        else:
            self.crearRegistro.setText("Insertar un Caso")
            self.editarRegistro.setText("Editar un Caso")
            self.verRegistro.setText("Ver un Caso")
            self.borrarRegistro.setText("Borrar un Caso")
        # fin try
    # fin __init__

    def _borrar(self):
        '''
        Función para borrar un Caso.
        '''
        ventana = VentanaListarCasos()
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        print(identificador)
        self.close()
    # fin _borrar

    def _ver(self):
        '''
        Función para ver un Caso.
        '''
        ventana = VentanaListarCasos()
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        print(identificador)
        self.close()
    # fin _ver

    def _editar(self):
        '''
        Función para editar un Caso.
        '''
        ventana = VentanaListarCasos()
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        print(identificador)
        self.close()
    # fin _editar

    def _crear(self):
        '''
        Función para crear un Caso.
        '''
        ventana = VentanaListarCasos()
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        print(identificador)
        self.close()
    # fin _crear
# fin VentanaCrudCaso


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ventana = VentanaCrudCaso()
    except:
        sys.exit("Error en el programa ...")
    else:
        ventana.exec_()
        print("Correcto ...")
    # fin try
# fin if test

# fin ventanaCrudCaso
