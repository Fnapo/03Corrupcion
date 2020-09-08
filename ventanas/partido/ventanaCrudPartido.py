# inicio ventanaCrudPartido

from PyQt5 import QtWidgets
from ventanas.ventanaCrudRegistros import VentanaCrudRegistros
from ventanas.partido.ventanaListarPartidos import VentanaListarPartidos


class VentanaCrudPartido(VentanaCrudRegistros):
    '''
    Ventana para realizar una acción CRUD relacionada con un Partido.
    '''

    def __init__(self):
        super(VentanaCrudPartido, self).__init__()
        self.crearRegistro.setText("Insertar un Partido")
        self.editarRegistro.setText("Editar un Partido")
        self.verRegistro.setText("Ver un Partido")
        self.borrarRegistro.setText("Borrar un Partido")
    # fin __init__

    def _borrar(self):
        '''
        Función para borrar un Partido.
        '''
        ventana = VentanaListarPartidos()
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        print(identificador)
        self.close()
    # fin _borrar

    def _ver(self):
        '''
        Función para ver un Partido.
        '''
        ventana = VentanaListarPartidos()
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        print(identificador)
        self.close()
    # fin _ver

    def _editar(self):
        '''
        Función para editar un Partido.
        '''
        ventana = VentanaListarPartidos()
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        print(identificador)
        self.close()
    # fin _editar

    def _crear(self):
        '''
        Función para crear un Partido.
        '''
        ventana = VentanaListarPartidos()
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        print(identificador)
        self.close()
    # fin _crear
# fin VentanaCrudPartido


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ventana = VentanaCrudPartido()
    except:
        sys.exit("Error en el programa ...")
    else:
        ventana.exec_()
        print("Correcto ...")
    # fin try
# fin if test

# fin ventanaCrudPartido
