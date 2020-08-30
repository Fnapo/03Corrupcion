# inicio conMysql.py

import mysql.connector as conMysql
from mysql.connector import errorcode
from errorCampoModal import ErrorCampoModal
from prepararInputs import PrepararInputs


class ConectarMysql(object):
    '''
    Crea una conexión, no propia o general, con una BBDD tipo Mysql y trabaja con dicha BBDD
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
            conexion = self.conectar()
        except:
            raise Exception
        else:
            conexion.close()
    # fin __init__

    def _accion(self):
        self._prepararCampos()
        errorNumero = 0
        if self._validarCampos():
            try:
                conexion = self.conectar()
                consulta = self._crearConsulta()
                try:
                    self.ejecutar(conexion, consulta)
                except Exception as error:
                    errorCM = ErrorCampoModal()
                    errorNumero = error.errno
                    if errorNumero == errorcode.ER_DUP_ENTRY:  # entrada duplicada
                        valor, campo = PrepararInputs.separarValorCampo(
                            error.msg)
                        errorCM.mostrar(
                            PrepararInputs.prepararMensajeDuplicado(valor, campo))
                    else:
                        errorCM.mostrar(error.msg)
                    # fin if entrada duplicada
                else:
                    self.correcto()
                finally:
                    if conexion.is_connected():
                        conexion.close()
                # fin try ejecutar
            except Exception:
                raise Exception
            # fin try conectar
            if errorNumero == 0:
                self.close()
        # fin if validar
    # fin _accion

    @staticmethod
    def errorNoRegistro(id: int):
        ventanaError = ErrorCampoModal("Error de registro")
        ventanaError.mostrar(f"El registro con 'id' = {id} no existe")
    # fin errorNoRegistro

    @staticmethod
    def errorConexion():
        errorCM = ErrorCampoModal("Error en la conexión")
        errorCM.mostrar(
            "Error en la conexión: Revisa los parámetros de la misma.")
    # fin errorConexion

    def _obtenerCampos(self):
        '''
        Obtiene los valores de los campos Inputs
        '''
        raise NotImplementedError
    # fin _obtenerCampos

    @staticmethod
    def correcto():
        errorCM = ErrorCampoModal("Éxito en la operación")
        errorCM.mostrar("Operación correcta ...")
    # fin correcto

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto
        '''
        raise NotImplementedError
    # fin _crearConsulta

    def _prepararCampos(self):
        '''
        Prepara el formato de los campos Inputs
        '''
        raise NotImplementedError
    # fin _prepararCampos

    def _validarCampos(self) -> bool:
        '''
        Devuelve True si los campos son válidos
        '''
        raise NotImplementedError
    # fin _validarCampos

    @staticmethod
    def conectar():
        '''
        Crea una conexión a una BBDD tipo MySQL
        '''
        try:
            conexion = conMysql.connect(**ConectarMysql._configuracion)
        except Exception as error:
            ConectarMysql.errorConexion()
            raise Exception
        else:
            return conexion
    # fin _conectar

    @staticmethod
    def ejecutar(conexion, consulta: str):
        '''
        Ejecuta una consulta tipo CRUD (SIUD)
        '''
        cursor = conexion.cursor()
        cursor.execute(consulta)
        conexion.commit()
        cursor.close()
    # fin ejecutar
# fin class ConectarMysql


if __name__ == "__main__":
    conexion = ConectarMysql.conectar()
    conexion.close()
# fin if test

# fin conMysql.py
