# inicio conMysql.py

import mysql.connector as conMysql
from mysql.connector import Error, errorcode
from errorCampoModal import ErrorCampoModal as cEcm
from prepararInputs import PrepararInputs as cPi

# inicio class ConectarMysql


class ConectarMysql(object):
    '''
    Crea una conexión con una BBDD tipo Mysql y trabaja con dicha BBDD
    '''

    # atributos static
    _configuracion = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'politica'
    }

    def __init__(self):
        super().__init__()
        try:
            self._conectar()
        except:
            raise Exception
        else:
            self._conexion.close()
    # fin __init__

    def _accion(self):
        self._prepararCampos()
        errorNumero = 0
        if self._validarCampos():
            try:
                self._conexion.reconnect()
                consulta = self._crearConsulta()
                try:
                    self._ejecutar(consulta)
                except Exception as error:
                    errorCM = cEcm()
                    errorNumero = error.errno
                    if errorNumero == errorcode.ER_DUP_ENTRY:  # entrada duplicada
                        valor, campo = cPi.separarValorCampo(
                            error.msg)
                        errorCM.mostrar(
                            cPi.prepararMensajeDuplicado(valor, campo))
                    else:
                        errorCM.mostrar(error.msg)
                else:
                    self._correcto()
                finally:
                    if self._conexion.is_connected():
                        self._conexion.close()
                # fin try ejecutar
            except Exception:
                raise Exception
            # fin try conectar
            if errorNumero == 0:
                self.close()
        # fin if validar
    # fin _accion

    @staticmethod
    def errorConexion():
        errorCM = cEcm("Error en la conexión")
        errorCM.mostrar(
            f"Error en la conexión: Revisa los parámetros de la misma.")
    # fin

    def _obtenerCampos(self):
        '''
        Obtiene los valores de los campos Inputs
        '''
        pass

    def _correcto(self):
        errorCM = cEcm("Éxito en la operación")
        errorCM.mostrar("Operación correcta ...")

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto
        '''
        pass

    def _prepararCampos(self):
        '''
        Prepara el formato de los campos Inputs
        '''
        pass

    def _validarCampos(self) -> bool:
        '''
        Devuelve True si los campos son válidos
        '''
        pass

    def _conectar(self):
        '''
        Crea una conexión a una BBDD tipo MySQL
        '''
        try:
            self._conexion = conMysql.connect(**self._configuracion)
        except Exception as error:
            self.errorConexion()
            raise Exception
        else:
            pass
    # fin conectar

    def _ejecutarSelect(self, consulta):
        '''
        Ejecuta una sentencia tipo SELECT
        '''
        palabras = consulta.split()
        cursor = self._conexion.cursor()
        cursor.execute(consulta)
        self._conexion.commit()

    def _ejecutar(self, consulta: str) -> int:
        '''
        Ejecuta una consulta tipo CRUD (SIUD)
        '''
        palabras = consulta.split()
        cursor = self._conexion.cursor()
        cursor.execute(consulta)
        self._conexion.commit()
        cursor.close()
    # fin ejecutar
# fin class ConectarMysql


if __name__ == "__main__":
    conexion = ConectarMysql.conectar()

# fin conMysql.py
