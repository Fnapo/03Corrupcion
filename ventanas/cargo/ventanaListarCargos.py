# inicio ventanaListarCargos

from ventanas.ventanaListarRegistros import VentanaListarRegistros
from PyQt5 import QtWidgets
from ventanas.cargo.seleccionarCargos import SeleccionarCargos


class VentanaListarCargos(VentanaListarRegistros):
    '''
    Ventana que lista los Cargos para elegir uno.
    '''

    def __init__(self):
        try:
            super(VentanaListarCargos, self).__init__()
        except ConnectionError:
            raise ConnectionError
        except ValueError:
            raise ValueError
        else:
            self.setWindowTitle("Selecionar un Cargo")
            self.label.setText("Selecciona un Cargo ...")
    # fin __init__

    @staticmethod
    def prepararCargo(cargo: tuple) -> tuple:
        '''
        Prepara el Cargo para insertarlo en el QComboBox.
        '''        
        return f"{cargo[1]:<{VentanaListarRegistros._anchura}}", cargo[0]
    # fin prepararCargo

    @staticmethod
    def _prepararItem(item: tuple) -> tuple:
        '''
        Prepara el item para insertarlo en el QComboBox.
        '''        
        return VentanaListarCargos.prepararCargo(item)
    # fin _prepararItem
    
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
        ventana = VentanaListarCargos()
    except:
        sys.exit("Error en el programa ...")
    else:
        ventana.exec_()
        salida = ventana.verIDRegistro()
        print(salida)
    # fin try
# fin if test

# fin ventanaListarCargos
