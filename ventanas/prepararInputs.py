# inicio prepararInputs

import locale


class PrepararInputs:
    '''
    Clase estática que prepara los inputs de un Formulario.
    También la función estaValorEntre
    '''

    @staticmethod
    def estaValorEntre(valor: float, minimo: float, maximo: float):
        '''
        Devuelve True si valor está entre mínimo y máximo, ambos incluisve.
        En caso contrario False
        '''
        return valor >= minimo and valor <= maximo
    # fin estaValorEntre

    @staticmethod
    def pasarMonedaFloat(cadena: str) -> float:
        '''
        Pasa del formato moneda a float
        '''
        cadena = PrepararInputs.pasarFormatoAmericano(cadena)

        return float(cadena)
    # fin pasarMonedaFloat

    @staticmethod
    def pasarFormatoAmericano(cadena: str) -> str:
        '''
        Pasa un número, o valor monetario, al formato americano sin moneda
        '''
        ayuda = PrepararInputs.pasarFloatMoneda(1259.33)
        indexPunto = ayuda.find(".")
        indexComa = ayuda.find(",")
        if indexPunto > indexComa:
            # formato inglés o americano
            cadena = cadena.replace(",", "")
        else:
            cadena = cadena.replace(".", "").replace(",", ".")
        cadena = cadena.replace("€", "").strip()

        return cadena
    # fin pasarFormatoAmericano

    @staticmethod
    def pasarFloatMoneda(valor: float, simbolo: bool = True) -> str:
        '''
        Dado un float lo pasa a formato moneda
        '''
        locale.setlocale(locale.LC_ALL, '')

        return locale.currency(valor, grouping=True, symbol=simbolo)
    # fin pasarFloatMoneda

    @staticmethod
    def prepararComoMoneda(cadena: str, simbolo: bool = True) -> str:
        '''
        Prepara una cadena en formato moneda
        '''
        try:
            cadena = PrepararInputs.pasarFormatoAmericano(cadena)
            valor = float(cadena)
        except:
            valor = 0.0
        finally:
            locale.setlocale(locale.LC_ALL, '')
        # fin try float

        return locale.currency(valor, grouping=True, symbol=simbolo)
    # fin prepararComoMoneda

    @ staticmethod
    def separarValorCampo(mensaje: str) -> tuple:
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
    # fin separarValorCampo

    @ staticmethod
    def prepararMensajeDuplicado(valor, campo) -> str:
        '''
        Dado un valor duplicado y el campo correspondiente
        devuelve el mensaje de error asociado
        '''
        return f"Error: el valor {valor} ya está usado en el campo {campo}."
    # fin preparaMensajeDuplicado

    @ staticmethod
    def prepararCadenaCap(cadena: str) -> str:
        '''
        Capitaliza Una Cadena
        '''
        cadena = PrepararInputs.quitarEspaciosCentrales(cadena)

        return cadena.strip().title()
    # fin prepararCadenaCap

    @ staticmethod
    def prepararCadenaMay(cadena: str) -> str:
        '''
        CONVIERTE A MAYÚSCULAS UNA CADENA
        '''
        cadena = PrepararInputs.quitarEspaciosCentrales(cadena)

        return cadena.strip().upper()
    # fin prepararCadenaMay

    @ staticmethod
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
# fin PrepararInputs

# fin prepararInputs
