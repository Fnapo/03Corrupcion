# inicio ventanaListarCasos

from ventanas.ventanaListarRegistros import VentanaListarRegistros
from PyQt5 import QtWidgets
from ventanas.caso.seleccionarCasos import SeleccionarCasos


class VentanaListarCasos(VentanaListarRegistros):
    '''
    Ventana que lista los Casos para elegir uno.
    '''

    def __init__(self):
        try:
            super(VentanaListarCasos, self).__init__()
        except ConnectionError:
            raise ConnectionError
        except ValueError:
            raise ValueError
        else:
            self.setWindowTitle("Selecionar un Caso")
            self.label.setText("Selecciona un Caso ...")
    # fin __init__

    @staticmethod
    def prepararCaso(caso: tuple) -> tuple:
        '''
        Prepara el Caso para insertarlo en el QComboBox.
        '''        
        return f"{caso[1]:<{VentanaListarRegistros._anchura}}", caso[0]
    # fin prepararCaso

    @staticmethod
    def _prepararItem(item: tuple) -> tuple:
        '''
        Prepara el item para insertarlo en el QComboBox.
        '''        
        return VentanaListarCasos.prepararCaso(item)
    # fin _prepararItem
    
    @staticmethod
    def _obtenerTodosRegistros() -> list:
        '''
        Obtiene todos los registros asociados.
        '''
        return SeleccionarCasos.obtenerTodosCasos(VentanaListarCasos._conexion)
    # fin _obtenerTodosRegistros
# fin VentanaListarCasos

if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ventana = VentanaListarCasos()
    except:
        sys.exit("Error en el programa ...")
    else:
        ventana.exec_()
        salida = ventana.verIDRegistro()
        print(salida)
    # fin try
# fin if test

# fin ventanaListarCasos
