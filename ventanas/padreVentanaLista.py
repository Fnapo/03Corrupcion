# inicio padreVentanaLista

class PadreVentanaLista:
    '''
    Clase vacía y abstracta (Interface) que es el padre de una Ventana que lista unos registros.
    '''

    def idRegistro(self, identificador: int = -1)->int:
        '''
        Devuelve el 'id' del registro seleccionado
        '''
        return identificador
    # fin idRegistro
# fin PadreVentanaLista

# fin padreVentanaLista
