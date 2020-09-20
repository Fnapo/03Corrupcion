# inicio ventanaCrud2Caso

from PyQt5 import QtWidgets
from ventanas.ventanaCrud2Registros import VentanaCrud2Registros
from ventanas.caso.seleccionarCasos import SeleccionarCasos
from ventanas.caso.ventanaListarCasos import VentanaListarCasos
from ventanas.caso.ventanaBorrarCaso import VentanaBorrarCaso
from ventanas.caso.ventanaVerCaso import VentanaVerCaso
from ventanas.caso.ventanaEditarCaso import VentanaEditarCaso, VentanaInsertarCaso
from ventanas.caso.ventanaBorrarCasoImputados import VentanaInsertarCasoImputados, VentanaBorrarCasoImputados


class VentanaCrud2Caso(VentanaCrud2Registros):
    '''
    Ventana para realizar una acción CRUD ampliada relacionada con un Caso.
    '''

    # miembro static
    _listaCombos = ["Imputados"]

    def __init__(self):
        try:
            super(VentanaCrud2Caso, self).__init__()
        except ConnectionError:
            raise ConnectionError
        else:
            self.crearRegistro.setText("Insertar un Caso")
            self.editarRegistro.setText("Editar un Caso")
            self.verRegistro.setText("Ver un Caso")
            self.borrarRegistro.setText("Borrar un Caso")
        # fin try
    # fin __init__

    def _borrarMultiple(self):
        '''
        Función para borrar una relación múltiple.
        '''
        if self.comboCrear.currentText() == VentanaCrud2Caso._listaCombos[0]:
            ventanaLista = VentanaListarCasos()
            ventanaLista.exec_()
            identificador = ventanaLista.verIDRegistro()
            if identificador > 0:
                ventana = VentanaBorrarCasoImputados(identificador)
                ventana.exec_()
        self.close()
    # fin _borrarMultiple

    def _crearMultiple(self):
        '''
        Función para crear una relación múltiple.
        '''
        if self.comboCrear.currentText() == VentanaCrud2Caso._listaCombos[0]:
            ventanaLista = VentanaListarCasos()
            ventanaLista.exec_()
            identificador = ventanaLista.verIDRegistro()
            if identificador > 0:
                ventana = VentanaInsertarCasoImputados(identificador)
                ventana.exec_()
        self.close()
    # fin _crearMultiple

    def _llenarCombos(self):
        '''
        Rellena los combos de la ventana.
        '''
        for cadena in VentanaCrud2Caso._listaCombos:
            self.comboBorrar.addItem(cadena)
            self.comboCrear.addItem(cadena)
        # fin for
    # fin _llenarCombos

    def _borrar(self):
        '''
        Función para borrar un Caso.
        '''
        ventana = VentanaListarCasos()
        cadena = ventana.label.text()
        cadena = cadena.replace("...", "para borrarlo")
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        if identificador > 0:
            ventanaBorrar = VentanaBorrarCaso(identificador)
            ventanaBorrar.exec_()
        self.close()
    # fin _borrar

    def _ver(self):
        '''
        Función para ver un Caso.
        '''
        ventana = VentanaListarCasos()
        cadena = ventana.label.text()
        cadena = cadena.replace("...", "para verlo")
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        if identificador > 0:
            ventanaVer = VentanaVerCaso(identificador)
            ventanaVer.exec_()
        self.close()
    # fin _ver

    def _editar(self):
        '''
        Función para editar un Caso.
        '''
        ventana = VentanaListarCasos()
        cadena = ventana.label.text()
        cadena = cadena.replace("...", "para editarlo")
        ventana.label.setText(cadena)
        ventana.exec_()
        identificador = ventana.verIDRegistro()
        if identificador > 0:
            ventanaEditar = VentanaEditarCaso(identificador)
            ventanaEditar.exec_()
        self.close()
    # fin _editar

    def _crear(self):
        '''
        Función para crear un Caso.
        '''
        ventanaInsertar = VentanaInsertarCaso()
        ventanaInsertar.exec_()
        self.close()
    # fin _crear
# fin VentanaCrud2Caso


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ventana = VentanaCrud2Caso()
    except:
        sys.exit("Error en el programa ...")
    else:
        ventana.exec_()
        print("Correcto ...")
    # fin try
# fin if test

# fin ventanaCrud2Caso
