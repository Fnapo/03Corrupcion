# inicio ventanaListarPartidos

from ventanaListarRegistros import VentanaListarRegistros
from PyQt5 import QtWidgets
from editarPartido import VentanaEditarPartido
from padreVentanaLista import PadreVentanaLista


class VentanaListarPartidos(VentanaListarRegistros):
    '''
    Ventana que lista los partidos para elegir uno
    '''

    def __init__(self, padre: PadreVentanaLista):
        try:
            super(VentanaListarPartidos, self).__init__(padre)
        except:
            raise Exception
        else:
            self.setWindowTitle("Selecionar un Partido")
            self.label.setText("Selecciona un Partido ...")
        # fin try
    # fin __init__

    @staticmethod
    def _prepararItem(item: tuple) -> str:
        '''
        Prepara el item para insertarlo en el QComboBox
        '''        
        return f"{item[1]:<50} ({item[0]})"
    
    @staticmethod
    def _obtenerTodosRegistros() -> list:
        '''
        Obtiene todos los registros asociados
        '''
        return VentanaEditarPartido.obtenerTodosPartidos()
    # fin _obtenerTodosRegistros

# fin VentanaListaPartidos

if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        padre = PadreVentanaLista()
        ui = VentanaListarPartidos(padre)
    except:
        pass
    else:
        ui.show()
        sys.exit(app.exec_())
    # fin try
# fin if test

# fin ventanaListarPartido
