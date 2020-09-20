# inicio ventanaListarImputados

from ventanas.ventanaListarRegistros import VentanaListarRegistros
from PyQt5 import QtWidgets
from ventanas.imputado.seleccionarImputados import SeleccionarImputados


class VentanaListarImputados(VentanaListarRegistros):
    '''
    Ventana que lista los Imputados para elegir uno.
    '''

    def __init__(self):
        try:
            super(VentanaListarImputados, self).__init__()
        except ConnectionError:
            raise ConnectionError
        except ValueError:
            raise ValueError
        else:
            self.setWindowTitle("Selecionar un Imputado")
            self.label.setText("Selecciona un Imputado ...")
    # fin __init__

    @staticmethod
    def prepararImputado(imputado: tuple) -> tuple:
        '''
        Prepara el Imputado para insertarlo en el QComboBox.
        '''
        apellidosNombre = f"{imputado[2]}, {imputado[1]}"
        return f"{apellidosNombre:<{VentanaListarRegistros._anchura}}", imputado[0]
    # fin prepararImputado

    @staticmethod
    def _prepararItem(item: tuple) -> tuple:
        '''
        Prepara el item para insertarlo en el QComboBox.
        '''        
        return VentanaListarImputados.prepararImputado(item)
    # fin _prepararItem
    
    @staticmethod
    def _obtenerTodosRegistros() -> list:
        '''
        Obtiene todos los registros asociados.
        '''
        return SeleccionarImputados.obtenerTodosImputados(VentanaListarImputados._conexion)
    # fin _obtenerTodosRegistros
# fin VentanaListarImputados

if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ventana = VentanaListarImputados()
    except:
        sys.exit("Error en el programa ...")
    else:
        ventana.exec_()
        salida = ventana.verIDRegistro()
        print(salida)
    # fin try
# fin if test

# fin ventanaListarImputados
