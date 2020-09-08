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
    def _prepararItem(item: tuple) -> tuple:
        '''
        Prepara el item para insertarlo en el QComboBox
        '''        
        return f"{item[1]:<{VentanaListarRegistros._anchura}}", item[0]
    
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
