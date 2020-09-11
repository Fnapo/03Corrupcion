# inicio seleccionarCargos

from ventanas.prepararInputs import PrepararInputs
import mysql.connector as conMysql


class SeleccionarCargos:
    '''
    Clase estática que selecciona y retorna uno o más Cargos
    '''

    @staticmethod
    def obtenerCargo(conexion: conMysql.MySQLConnection, identificador: int) -> list:
        '''
        Dada una conexion tipo Mysql, selecciona y retorna, si existe, el Cargo con 'id' identificador
        '''
        cursor = conexion.cursor()
        consulta = f"SELECT * \
            FROM cargos \
            WHERE id_cargo = {identificador}"            
        cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
        lista = cursor.fetchall()
        cursor.close()
        conexion.close()

        return lista
    # fin obtenerCargo

    @staticmethod
    def obtenerTodosCargos(conexion: conMysql.MySQLConnection) -> list:
        '''
        Dada una conexion tipo Mysql, selecciona y retorna todos los Cargos
        '''
        cursor = conexion.cursor()
        consulta = f"SELECT * \
            FROM cargos"
        cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
        lista = cursor.fetchall()
        cursor.close()
        conexion.close()

        return lista
    # fin obtenerTodosCargos
# fin SeleccionarCargos

# fin seleccionarCargos
