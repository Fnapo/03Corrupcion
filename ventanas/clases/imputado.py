# python 3
# Inicio imputado

from datetime import date


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

# fin imputado
