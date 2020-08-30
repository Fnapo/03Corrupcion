# inicio padreVentanaLista

class PadreVentanaLista:
    '''
    Clase que llama a una ventana que lista unos registros
    '''

    def __init__(self):
        super(PadreVentanaLista, self).__init__()

    def _tratarRegistro(self, identificador: int):
        '''
        Trata el registro con 'id' identificador
        '''
        raise NotImplementedError
        print(f"Identificador número {identificador}")
    # fin _tratarRegistro
# fin padreVentanaLista
