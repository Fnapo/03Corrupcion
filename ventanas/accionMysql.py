# inicio accionMysql

from mysql.connector import errorcode
from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.clases.conectarMysql import ConectarMysql
from ventanas.conexionMysql import ConexionMysql


class AccionMysql(ConexionMysql):
    '''
    Clase estática y abstracta con una conexión para realizar una acción Mysql, en una clase hija.
    '''

    def __init__(self):
        try:
            super(AccionMysql, self).__init__()
            self._revisar = True
        except:
            raise ConnectionError
    # fin __init__

    def _accion(self):
        validos = False
        if self._revisar:
            self._prepararCampos()
            validos = self._validarCampos()
        errorNumero = 0
        if validos or not self._revisar:
            self._conexion.reconnect()
            consulta = self._crearConsulta()
            try:
                ConectarMysql.ejecutar(self._conexion, consulta)
            except Exception as error:
                errorNumero = error.errno
                if errorNumero == errorcode.ER_DUP_ENTRY:
                    # entrada duplicada
                    ErrorCampoModal.errorDuplicado(error.msg)
                elif errorNumero == errorcode.ER_ROW_IS_REFERENCED_2:
                    # fk_id en uso
                    ErrorCampoModal.campoReferenciado(error.msg)
                else:
                    ErrorCampoModal.errorDesconocido(error.msg)
                # fin if entrada duplicada
            else:
                ErrorCampoModal.correcto()
            finally:
                self._conexion.close()
            # fin try ejecutar
            if errorNumero == 0:
                self.close()
        # fin if validos
    # fin _accion

    def _obtenerCampos(self):
        '''
        Obtiene los valores de los campos Inputs.
        '''
        raise NotImplementedError
    # fin _obtenerCampos

    def _crearConsulta(self) -> str:
        '''
        Crea una consulta SQL dependiendo del objeto.
        '''
        raise NotImplementedError
    # fin _crearConsulta

    def _prepararCampos(self):
        '''
        Prepara el formato de los campos Inputs.
        '''
        raise NotImplementedError
    # fin _prepararCampos

    def _validarCampos(self) -> bool:
        '''
        Devuelve True si los campos son válidos.
        '''
        raise NotImplementedError
    # fin _validarCampos
# fin AccionMysql

# fin accionMysql
