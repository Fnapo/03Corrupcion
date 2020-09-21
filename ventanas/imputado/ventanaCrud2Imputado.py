# inicio ventanaCrud2Imputado

from PyQt5 import QtWidgets
from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.ventanaCrud2Registros import VentanaCrud2Registros
from ventanas.imputado.seleccionarImputados import SeleccionarImputados
from ventanas.imputado.ventanaListarImputados import VentanaListarImputados
from ventanas.imputado.ventanaBorrarImputado import VentanaBorrarImputado
from ventanas.imputado.ventanaVerImputado import VentanaVerImputado
from ventanas.imputado.ventanaEditarImputado import VentanaEditarImputado, VentanaInsertarImputado
from ventanas.imputado.ventanaBorrarImputadoCasos import VentanaInsertarImputadoCasos, VentanaBorrarImputadoCasos


class VentanaCrud2Imputado(VentanaCrud2Registros):
    '''
    Ventana para realizar una acción CRUD ampliada relacionada con un Imputado.
    '''

    # miembro static
    _listaCombos = ["Casos"]

    def __init__(self):
        try:
            super(VentanaCrud2Imputado, self).__init__()
        except ConnectionError:
            raise ConnectionError
        else:
            self.crearRegistro.setText("Insertar un Imputado")
            self.editarRegistro.setText("Editar un Imputado")
            self.verRegistro.setText("Ver un Imputado")
            self.borrarRegistro.setText("Borrar un Imputado")
        # fin try
    # fin __init__

    def _borrarMultiple(self):
        '''
        Función para borrar una relación múltiple.
        '''
        if self.comboCrear.currentText() == VentanaCrud2Imputado._listaCombos[0]:
            ventanaLista = VentanaListarImputados()
            ventanaLista.exec_()
            identificador = ventanaLista.verIDRegistro()
            if identificador > 0:
                ventana = VentanaBorrarImputadoCasos(identificador)
                ventana.exec_()
        self.close()
    # fin _borrarMultiple

    def _crearMultiple(self):
        '''
        Función para crear una relación múltiple.
        '''
        if self.comboCrear.currentText() == VentanaCrud2Imputado._listaCombos[0]:
            ventanaLista = VentanaListarImputados()
            ventanaLista.exec_()
            identificador = ventanaLista.verIDRegistro()
            if identificador > 0:
                ventana = VentanaInsertarImputadoCasos(identificador)
                ventana.exec_()
        self.close()
    # fin _crearMultiple

    def _llenarCombos(self):
        '''
        Rellena los combos de la ventana.
        '''
        for cadena in VentanaCrud2Imputado._listaCombos:
            self.comboBorrar.addItem(cadena)
            self.comboCrear.addItem(cadena)
        # fin for
    # fin _llenarCombos

    def _borrar(self):
        '''
        Función para borrar un Imputado.
        '''
        try:
            ventana = VentanaListarImputados()
        except ValueError:
            ErrorCampoModal.errorSinRegistros("Imputados")
        else:
            cadena = ventana.label.text()
            cadena = cadena.replace("...", "para borrarlo")
            ventana.exec_()
            identificador = ventana.verIDRegistro()
            if identificador > 0:
                ventanaBorrar = VentanaBorrarImputado(identificador)
                ventanaBorrar.exec_()
        finally:
            self.close()
    # fin _borrar

    def _ver(self):
        '''
        Función para ver un Imputado.
        '''
        try:
            ventana = VentanaListarImputados()
        except ValueError:
            ErrorCampoModal.errorSinRegistros("Imputados")
        else:
            cadena = ventana.label.text()
            cadena = cadena.replace("...", "para verlo")
            ventana.exec_()
            identificador = ventana.verIDRegistro()
            if identificador > 0:
                ventanaVer = VentanaVerImputado(identificador)
                ventanaVer.exec_()
        finally:
            self.close()
    # fin _ver

    def _editar(self):
        '''
        Función para editar un Imputado.
        '''
        try:
            ventana = VentanaListarImputados()
        except ValueError:
            ErrorCampoModal.errorSinRegistros("Imputados")
        else:
            cadena = ventana.label.text()
            cadena = cadena.replace("...", "para editarlo")
            ventana.label.setText(cadena)
            ventana.exec_()
            identificador = ventana.verIDRegistro()
            if identificador > 0:
                ventanaEditar = VentanaEditarImputado(identificador)
                ventanaEditar.exec_()
        finally:
            self.close()
    # fin _editar

    def _crear(self):
        '''
        Función para crear un Imputado.
        '''
        ventanaInsertar = VentanaInsertarImputado()
        ventanaInsertar.exec_()
        self.close()
    # fin _crear
# fin VentanaCrud2Imputado


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ventana = VentanaCrud2Imputado()
    except:
        sys.exit("Error en el programa ...")
    else:
        ventana.exec_()
        print("Correcto ...")
    # fin try
# fin if test

# fin ventanaCrud2Imputado
