# inicio principal

from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.conexionMysql import ConexionMysql
from ventanas.caso.ventanaListarCasos import VentanaListarCasos
from PyQt5 import QtWidgets
from ventanas.usuario.ventanaEntradaUsuario import VentanaEntradaUsuario
from ventanas.ventanaPrincipal import VentanaPrincipal
import sys


def main():
    '''
    Función principal e inicial.
    '''

    def salida(estado: int = 0):
        app.beep()
        print(f"Exit {estado}")
    # fin salida

    app = QtWidgets.QApplication([])
    try:
        estado = 1
        if not loginVeces():
            sys.exit(estado)
    except (ConnectionError, SystemExit):
        salida(estado)
    else:
        try:
            ventanaInicial = VentanaPrincipal()
            ventanaInicial.show()
            sys.exit(app.exec_())
        except SystemExit:
            salida()
        # fin ventanaInicial
    # fin loginVeces
# fin main

def loginVeces() -> bool:
    '''
    Función para hacer un login a la app.
    '''
    try:
        ventana = VentanaEntradaUsuario()
    except ConnectionError:
        ErrorCampoModal.errorConexion()
        raise ConnectionError
    else:
        total = 3
        salida = False
        veces = 0
        while veces in range(total) and not salida:
            ventana.resetear()
            ventana.inputUsuario.setFocus()
            ventana.exec_()
            salida = ventana.verCorrecto()
            veces += 1
            if not salida:
                errorEntrada = ErrorCampoModal("Error en el login")
                if veces != total:
                    mensaje = f"Error en los datos del Usuario\n\nTe quedan {total-veces} intentos"
                else:
                    mensaje = "¡¡¡AAAdiósss!!!"
                errorEntrada.mostrar(mensaje)
            # fin if
        # fin while

        return salida
    # fin try
# fin loginVeces

main()

# fin principal
