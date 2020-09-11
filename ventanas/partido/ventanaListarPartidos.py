# inicio ventanaListarPartidos

from ventanas.ventanaListarRegistros import VentanaListarRegistros
from PyQt5 import QtWidgets
from ventanas.partido.seleccionarPartidos import SeleccionarPartidos


class VentanaListarPartidos(VentanaListarRegistros):
    '''
    Ventana que lista los Partidos para elegir uno.
    '''

    def __init__(self):
        super(VentanaListarPartidos, self).__init__()
        self.setWindowTitle("Selecionar un Partido")
        self.label.setText("Selecciona un Partido ...")
    # fin __init__

    @staticmethod
    def prepararPartido(partido: tuple) -> tuple:
        '''
        Prepara el Partido para insertarlo en el QComboBox
        '''        
        return f"{partido[1]:<{VentanaListarRegistros._anchura}}", partido[0]
    # fin prepararPartido

    @staticmethod
    def _prepararItem(item: tuple) -> tuple:
        '''
        Prepara el item para insertarlo en el QComboBox
        '''        
        return VentanaListarPartidos.prepararPartido(item)
    # fin _prepararItem
    
    @staticmethod
    def _obtenerTodosRegistros() -> list:
        '''
        Obtiene todos los registros asociados
        '''
        return SeleccionarPartidos.obtenerTodosPartidos(VentanaListarPartidos._conexion)
    # fin _obtenerTodosRegistros
# fin VentanaListarPartidos

if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = VentanaListarPartidos()
    except:
        sys.exit("Error en el programa ...")
    else:
        ui.show()
        sys.exit(app.exec_())
    # fin try
# fin if test

# fin ventanaListarPartido
