# python 3
# Inicio caso.py

from random import *


class Caso(object):
    def __init__(self, cedula: str, identificador=1):
        self.identificador = identificador
        self.cedula = cedula
        self.montante = 50000 + randint(0, 500000)
# fin Caso
