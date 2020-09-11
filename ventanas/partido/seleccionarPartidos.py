# inicio seleccionarPartidos

from ventanas.clases.conectarMysql import ConectarMysql
from ventanas.prepararInputs import PrepararInputs
import mysql.connector as conMysql 


class SeleccionarPartidos:
    '''
    Clase estática que selecciona y retorna uno o más Partidos
    '''

    @staticmethod
    def obtenerPartido(conexion: conMysql.MySQLConnection, identificador: int) -> list:
        '''
        Dada una conexion tipo Mysql, selecciona y retorna, si existe, el Partido con 'id' identificador
        '''
        cursor = conexion.cursor()
        consulta = f"SELECT * \
            FROM partidos \
            WHERE id_partido = {identificador}"
        cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
        lista = cursor.fetchall()
        cursor.close()
        conexion.close()

        return lista
    # fin obtenerPartido

    @staticmethod
    def obtenerTodosPartidos(conexion: conMysql.MySQLConnection) -> list:
        '''
        Dada una conexion tipo Mysql, selecciona y retorna todos los Partidos
        '''
        cursor = conexion.cursor()
        consulta = "SELECT * \
            FROM partidos"
        cursor.execute(PrepararInputs.quitarEspaciosCentrales(consulta))
        lista = cursor.fetchall()
        cursor.close()
        conexion.close()

        return lista
    # fin obtenerTodosPartidos
# fin SeleccionarPartidos

# fin seleccionarPartidos
