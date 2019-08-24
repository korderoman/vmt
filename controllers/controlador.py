import sqlite3
from sqlite3 import Error


class Controlador():
    def __init__(self):
        self.bbdd="bbdd.db"
    
    def consulta(self,consulta,parametros=()):
        try:
            #obtenemos la ruta a nuestra carpeta
            conexion=sqlite3.connect("./database/"+self.bbdd)
            cursor=conexion.cursor()
            result=cursor.execute(consulta,parametros)
            conexion.commit()
            filas=result.fetchall()
            return filas
        except Error as e:
            return e
        finally:
            conexion.close()

    def logear_usuario(self,usuario,clave):
        query=("SELECT  * FROM usuarios WHERE usuario=? AND clave=?")
        resultados=self.consulta(query,(usuario,clave))
        if resultados:            
            print(resultados[0])
            return True
        else:
            print("No existe el usuario")
            return False
    
    def agregar_incidencia(self,incidencia):
        data=(incidencia.operador,incidencia.puesto,incidencia.administrador,incidencia.fecha,incidencia.camara,incidencia.turno,incidencia.incidente,incidencia.descripcion,incidencia.area)
        query=("INSERT INTO datos VALUES (NULL,?,?,?,?,?,?,?,?,?)")
        resultado=self.consulta(query,data)
        print(resultado)#revisar que se envíe un mensaje de confirmación
    
    def mostrar_incidencias_totales(self):
        query="SELECT * FROM datos"
        resultados=self.consulta(query)
        return resultados