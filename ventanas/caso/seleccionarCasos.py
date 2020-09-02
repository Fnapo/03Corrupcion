# inicio seleccionarCasos

from ventanas.prepararInputs import PrepararInputs
import mysql.connector as conMysql


class SeleccionarCasos:
    '''
    Clase estática que selecciona y retorna uno o más Casos
    '''

    @staticmethod
    def obtenerCaso(conexion: conMysql.MySQLConnection, identificador: int) -> list:
        '''
        Dada una conexion tipo Mysql, selecciona y retorna, si existe, el Caso con 'id' identificador
        '''
        cursor = conexion.cursor()
        consulta = f"SELECT credencial, montante \
            FROM casos \
            WHERE id_caso = {identificador}"            
        cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
        lista = cursor.fetchall()
        cursor.close()
        conexion.close()

        return lista
    # fin obtenerCaso

    @staticmethod
    def obtenerTodosCasos(conexion: conMysql.MySQLConnection) -> list:
        '''
        Dada una conexion tipo Mysql, selecciona y retorna todos los Casos
        '''
        cursor = conexion.cursor()
        consulta = f"SELECT id_caso, credencial, montante \
            FROM casos"
        cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
        lista = cursor.fetchall()
        cursor.close()
        conexion.close()

        return lista
    # fin obtenerTodosCasos
# fin SeleccionarCasos

# fin seleccionarCasos
