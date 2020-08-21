# python 3
# Inicio caso.py

from random import *
montante = 50000 + randint(0, 500000)

class Caso(object):
    def __init__(self, cedula: str, montante: float, identificador=1):
        self.identificador = identificador
        self.cedula = cedula
        self.montante = montante

# fin Caso
