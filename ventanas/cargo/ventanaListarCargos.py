# inicio ventanaListarCargos

from ventanas.ventanaListarRegistros import VentanaListarRegistros
from PyQt5 import QtWidgets
from ventanas.cargo.seleccionarCargos import SeleccionarCargos


class VentanaListarCargos(VentanaListarRegistros):
    '''
    Ventana que lista los Cargos para elegir uno.
    '''

    def __init__(self):
        super(VentanaListarCargos, self).__init__()
        self.setWindowTitle("Selecionar un Cargo")
        self.label.setText("Selecciona un Cargo ...")
    # fin __init__

    @staticmethod
    def _prepararItem(item: tuple) -> tuple:
        '''
        Prepara el item para insertarlo en el QComboBox.
        '''        
        return f"{item[1]:<{VentanaListarRegistros._anchura}}", item[0]
    
    @staticmethod
    def _obtenerTodosRegistros() -> list:
        '''
        Obtiene todos los registros asociados.
        '''
        return SeleccionarCargos.obtenerTodosCargos(VentanaListarCargos._conexion)
    # fin _obtenerTodosRegistros
# fin VentanaListarCargos

if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = VentanaListarCargos()
    except:
        sys.exit("Error en el programa ...")
    else:
        ui.exec_()
        salida = ui.verIDRegistro()
        print(salida)
    # fin try
# fin if test

# fin ventanaListarCargos
