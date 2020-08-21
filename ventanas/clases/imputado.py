# python 3
# Inicio imputado.cy

from datetime import *
from random import *

partidos = [0 for i in range(7)] + [1 for i in range(7)] + \
    [2 for i in range(3)] + [3 for i in range(3)] + [4]
partido = randint(0, len(partidos) - 1)
partido = partidos[partido]


class Imputado(object):
    def __init__(
            self, nombre: str, apellidos: str, fecha_nacimiento: date, grupo_sangre: str, partido: int, cargo=1, identificador=1):
        self.identificador = identificador
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.grupo_sangre = grupo_sangre
        self.cargo = cargo
        self.partido = partido

    # fin __init__

# fin imputado.cy
