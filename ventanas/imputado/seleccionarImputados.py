# inicio seleccionarImputados

from ventanas.prepararInputs import PrepararInputs
import mysql.connector as conMysql


class SeleccionarImputados:
    '''
    Clase estática que selecciona y retorna uno o más Imputados
    '''

    @staticmethod
    def obtenerImputado(conexion: conMysql.MySQLConnection, identificador: int) -> list:
        '''
        Dada una conexion tipo Mysql, selecciona y retorna, si existe, el Imputado con 'id' identificador
        '''
        cursor = conexion.cursor()
        consulta = f"SELECT * \
            FROM imputados \
            WHERE id_imputado = {identificador}"            
        cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
        lista = cursor.fetchall()
        cursor.close()
        conexion.close()

        return lista
    # fin obtenerImputado

    @staticmethod
    def obtenerTodosImputados(conexion: conMysql.MySQLConnection) -> list:
        '''
        Dada una conexion tipo Mysql, selecciona y retorna todos los Imputados
        '''
        cursor = conexion.cursor()
        consulta = f"SELECT * \
            FROM imputados"
        cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
        lista = cursor.fetchall()
        cursor.close()
        conexion.close()

        return lista
    # fin obtenerTodosImputados
# fin SeleccionarImputados

# fin seleccionarImputados
