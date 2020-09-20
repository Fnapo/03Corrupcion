# inicio ventanaCrudPartido

from PyQt5 import QtWidgets
from ventanas.ventanaCrudRegistros import VentanaCrudRegistros
from ventanas.partido.ventanaListarPartidos import VentanaListarPartidos
from ventanas.partido.ventanaBorrarPartido import VentanaBorrarPartido
from ventanas.partido.ventanaVerPartido import VentanaVerPartido
from ventanas.partido.ventanaEditarPartido import VentanaEditarPartido, VentanaInsertarPartido


class VentanaCrudPartido(VentanaCrudRegistros):
    '''
    Ventana para realizar una acción CRUD relacionada con un Partido.
    '''

    def __init__(self):
        try:
            super(VentanaCrudPartido, self).__init__()
        except ConnectionError:
            raise ConnectionError
        else:
            self.crearRegistro.setText("Insertar un Partido")
            self.editarRegistro.setText("Editar un Partido")
            self.verRegistro.setText("Ver un Partido")
            self.borrarRegistro.setText("Borrar un Partido")
        # fin try
    # fin __init__

    def _borrar(self):
        '''
        Función para borrar un Partido.
        '''
        ventana = VentanaListarPartidos()
        cadena = ventana.label.text()
        cadena = cadena.replace("...", "para borrarlo")
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        if identificador > 0:
            ventanaBorrar = VentanaBorrarPartido(identificador)
            ventanaBorrar.exec_()
        self.close()
    # fin _borrar

    def _ver(self):
        '''
        Función para ver un Partido.
        '''
        ventana = VentanaListarPartidos()
        cadena = ventana.label.text()
        cadena = cadena.replace("...", "para verlo")
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        if identificador > 0:
            ventanaVer = VentanaVerPartido(identificador)
            ventanaVer.exec_()
        self.close()
    # fin _ver

    def _editar(self):
        '''
        Función para editar un Partido.
        '''
        ventana = VentanaListarPartidos()
        cadena = ventana.label.text()
        cadena = cadena.replace("...", "para editarlo")
        ventana.label.setText(cadena)
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        if identificador > 0:
            ventanaEditar = VentanaEditarPartido(identificador)
            ventanaEditar.exec_()
        self.close()
    # fin _editar

    def _crear(self):
        '''
        Función para crear un Partido.
        '''
        ventanaInsertar = VentanaInsertarPartido()
        ventanaInsertar.exec_()
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
