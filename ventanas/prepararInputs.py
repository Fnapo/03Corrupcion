# inicio PrepararInputs

class PrepararInputs(object):
    '''
    Clase que prepara los inputs de un Formulario
    '''
    @staticmethod
    def prepararCadenaCap(cadena: str) -> str:
        '''
        Capitaliza Una Cadena
        '''
        cadena = PrepararInputs.__quitarEspaciosCentrales(cadena)

        return cadena.strip().title()
    # fin prepararCadenaCap

    @staticmethod
    def prepararCadenaMay(cadena: str) -> str:
        '''
        CONVIERTE A MAYÚSCULAS UNA CADENA
        '''
        cadena = PrepararInputs.__quitarEspaciosCentrales(cadena)

        return cadena.strip().upper()
    # fin prepararCadenaMay

    @staticmethod
    def __quitarEspaciosCentrales(cadena: str) -> str:
        lista = cadena.split()
        cadena = ''
        for item in lista:
            if len(cadena) == 0:
                cadena += item
            else:
                cadena += f" {item}"
        # fin for

        return cadena
    # fin __quitarEspaciosCentrales
# fin class PrepararInputs

# fin PrepararInputs
