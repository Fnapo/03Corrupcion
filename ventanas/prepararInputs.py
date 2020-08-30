# inicio PrepararInputs

class PrepararInputs(object):
    '''
    Clase que prepara los inputs de un Formulario
    '''
    
    @staticmethod
    def prepararComoMoneda(cadena: str):
        '''
        Prepara una cadena como un número con 2 decimales
        '''
        try:
            valor = float(cadena)
        except:
            raise FloatingPointError
        else:
            return f"{valor:,.2f}"
        # fin try float
    # fin prepararMoneda
            
    @staticmethod
    def separarValorCampo(mensaje: str):
        '''
        Dado un mensaje de error tipo valor duplicado separa dicho valor y el campo donde se ha realizado dicha duplicación y los retorna
        '''
        inicioValor = mensaje.find("'")
        finValor = mensaje.find("'", inicioValor + 1)+1
        valor = mensaje[inicioValor:finValor]
        inicioCampo = mensaje.find("idx_")+4
        finCampo = mensaje.find("'", inicioCampo + 1)
        campo = f"'{mensaje[inicioCampo:finCampo].capitalize()}'"

        return valor, campo
    #fin separarValorCampo

    @staticmethod
    def prepararMensajeDuplicado(valor, campo):
        '''
        Dado un valor duplicado y el campo correspondiente
        devuelve el mensaje de error asociado
        '''
        return f"Error: el valor {valor} ya está usado en el campo {campo}."
    # fin preparaMensajeDuplicado

    @staticmethod
    def prepararCadenaCap(cadena: str) -> str:
        '''
        Capitaliza Una Cadena
        '''
        cadena = PrepararInputs.quitarEspaciosCentrales(cadena)

        return cadena.strip().title()
    # fin prepararCadenaCap

    @staticmethod
    def prepararCadenaMay(cadena: str) -> str:
        '''
        CONVIERTE A MAYÚSCULAS UNA CADENA
        '''
        cadena = PrepararInputs.quitarEspaciosCentrales(cadena)

        return cadena.strip().upper()
    # fin prepararCadenaMay

    @staticmethod
    def quitarEspaciosCentrales(cadena: str) -> str:
        lista = cadena.split()
        cadena = ''
        for item in lista:
            if len(cadena) == 0:
                cadena += item
            else:
                cadena += f" {item}"
        # fin for

        return cadena
    # fin quitarEspaciosCentrales
# fin class PrepararInputs

# fin PrepararInputs
