# inicio ventanaCrudCargo

from PyQt5 import QtWidgets
from ventanas.ventanaCrudRegistros import VentanaCrudRegistros
from ventanas.cargo.ventanaListarCargos import VentanaListarCargos
from ventanas.cargo.ventanaBorrarCargo import VentanaBorrarCargo
from ventanas.cargo.ventanaVerCargo import VentanaVerCargo
from ventanas.cargo.ventanaEditarCargo import VentanaEditarCargo, VentanaInsertarCargo


class VentanaCrudCargo(VentanaCrudRegistros):
    '''
    Ventana para realizar una acción CRUD relacionada con un Cargo.
    '''

    def __init__(self):
        try:
            super(VentanaCrudCargo, self).__init__()
        except ConnectionError:
            raise ConnectionError
        else:
            self.crearRegistro.setFocus()
            self.crearRegistro.setText("Insertar un Cargo")
            self.editarRegistro.setText("Editar un Cargo")
            self.verRegistro.setText("Ver un Cargo")
            self.borrarRegistro.setText("Borrar un Cargo")
        # fin try
    # fin __init__

    def _borrar(self):
        '''
        Función para borrar un Cargo.
        '''
        ventana = VentanaListarCargos()
        cadena = ventana.label.text()
        cadena = cadena.replace("...", "para borrarlo")
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        if identificador > 0:
            ventanaBorrar = VentanaBorrarCargo(identificador)
            ventanaBorrar.exec_()
        self.close()
    # fin _borrar

    def _ver(self):
        '''
        Función para ver un Cargo.
        '''
        ventana = VentanaListarCargos()
        cadena = ventana.label.text()
        cadena = cadena.replace("...", "para verlo")
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        if identificador > 0:
            ventanaVer = VentanaVerCargo(identificador)
            ventanaVer.exec_()
        self.close()
    # fin _ver

    def _editar(self):
        '''
        Función para editar un Cargo.
        '''
        ventana = VentanaListarCargos()
        cadena = ventana.label.text()
        cadena = cadena.replace("...", "para editarlo")
        ventana.label.setText(cadena)
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        if identificador > 0:
            ventanaEditar = VentanaEditarCargo(identificador)
            ventanaEditar.exec_()
        self.close()
    # fin _editar

    def _crear(self):
        '''
        Función para crear un Cargo.
        '''
        ventanaInsertar = VentanaInsertarCargo()
        ventanaInsertar.exec_()
        self.close()
    # fin _crear
# fin VentanaCrudCargo


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ventana = VentanaCrudCargo()
    except:
        sys.exit("Error en el programa ...")
    else:
        ventana.exec_()
        print("Correcto ...")
    # fin try
# fin if test

# fin ventanaCrudCargo
