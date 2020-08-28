# inicio ventanaInsertarCaso

from PyQt5 import QtCore, QtGui, QtWidgets
from caso.insertarCaso import Ui_VentanaCaso
from clases.conectarMysql import ConectarMysql
from prepararInputs import PrepararInputs
from errorCampoModal import ErrorCampoModal


class VentanaInsertarCaso(QtWidgets.QDialog, Ui_VentanaCaso, ConectarMysql):
    '''
    Ventana para insertar un Caso
    '''

    def __init__(self):
        try:
            QtWidgets.QDialog.__init__(self)
            ConectarMysql.__init__(self)
            self.setupUi(self)
        except:
            raise Exception
        else:
            self.botonAceptar.clicked.connect(self._accion)
            self.botonResetear.clicked.connect(self._resetear)
        # fin try conectar
    # fin __init__

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto
        '''
        credencial, montante = self._obtenerCampos()
        consulta = f"INSERT INTO casos \
            (credencial, montante) \
            VALUES ('{credencial}', '{montante}')"

        return PrepararInputs.quitarEspaciosCentrales(consulta)
    # fin _crearConsulta

    def _validarCampos(self) -> bool:
        '''
        Devuelve True si los campos son válidos
        '''
        credencial, montante = self._obtenerCampos()
        errorCM = ErrorCampoModal()
        minimo = 4
        valorMinimo = 50000
        if len(credencial) < 4:
            errorCM.mostrar(
                f"Campo vacío o muy corto: 'Credencial'\nMínimo {minimo} Caracteres")
            return False
        elif len(montante) == 0:
            errorCM.mostrar(
                "Campo vacío: 'Montante'")
            return False
        else:
            try:
                montante = float(montante)
            except:
                errorCm = ErrorCampoModal()
                errorCm.mostrar("El campo 'Montante' debe ser un decimal")
                return False
            else:
                if montante < valorMinimo:
                    errorCM.mostrar(
                        f"Montante muy pequeño: {montante:,.2f}\nMínimo {valorMinimo:,.2f} €")
                    return False

                return True
        # fin try float
    # fin _validarCampos

    def _prepararCampos(self):
        '''
        Prepara el formato de los campos Inputs
        '''
        credencial, montante = self._obtenerCampos()
        self.inputCredencial.setText(
            PrepararInputs.prepararCadenaMay(credencial))
        try:
            self.inputMontante.setText(
                PrepararInputs.prepararComoMoneda(montante))
        except:
            pass
            # errorCm = ErrorCampoModal()
            # errorCm.mostrar("El campo 'Montante' debe ser un decimal")
            # self.inputMontante.setText("0.00")
        # fin try
    # fin _prepararCampos

    def _obtenerCampos(self):
        return self.inputCredencial.text(), self.inputMontante.text()
    # fin _obtenerCampos

    def _resetear(self):
        self.inputCredencial.setText("")
        self.inputMontante.setText("")
    # fin _resetear
# fin VentanaInsertarCaso


if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = VentanaInsertarCaso()
    except:
        pass
    else:
        ui.show()
        sys.exit(app.exec_())
# fin if test

# fin ventanaInsertarCaso
