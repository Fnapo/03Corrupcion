# python 3
# Inicio partido.cy

class Partido(object):
    def __init__(self, nombre: str, siglas: str, logo: str, identificador=1):
        self.identificador = identificador
        self.nombre = nombre
        self.siglas = siglas
        self.logo = logo

# fin Partido
