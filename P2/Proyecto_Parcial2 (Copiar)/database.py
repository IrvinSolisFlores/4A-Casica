import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="POO_project_P2"
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None
    
if __name__ == "__main__":
    conexion = crear_conexion()

