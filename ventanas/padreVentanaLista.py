# inicio padreVentanaLista

class PadreVentanaLista:
    '''
    Clase vacía y abstracta (Interface) que es el padre de una Ventana que lista unos registros
    '''

    def _tratarRegistro(self, identificador: int):
        '''
        Trata el registro con 'id' identificador
        '''
        raise NotImplementedError
    # fin _tratarRegistro
# fin PadreVentanaLista

# fin padreVentanaLista
